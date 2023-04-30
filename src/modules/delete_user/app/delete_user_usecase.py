from datetime import datetime

from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository


class DeleteUserUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository, observability: IObservability):
        self.repo_activity = repo_activity
        self.repo_user = repo_user
        self.observability = observability

    def __call__(self, user: User) -> UserInfo:

        self.observability.log_usecase_in()
        user_info = self.repo_user.get_user_info(user.user_id)
        all_activities = self.repo_activity.get_all_activities()

        all_activities_dict = {activity.code: activity for activity in all_activities}

        user_enrollments = self.repo_activity.get_enrollments_by_user_id_with_dropped(user_info.user_id)

        for enrollment in user_enrollments:
            self.repo_activity.delete_enrollment(enrollment.user_id, enrollment.activity_code)
            
            self.observability._log_info(f"Enrollment deleted with user_id = {enrollment.user_id} and activity_code = {enrollment.activity_code}")       
            
            activity = all_activities_dict.get(enrollment.activity_code)
            if activity is None:
                continue
            if activity.taken_slots >= activity.total_slots and enrollment.state == ENROLLMENT_STATE.ENROLLED and datetime.now().timestamp()*1000 < activity.start_date:
                activity, enrollments = self.repo_activity.get_activity_with_enrollments(activity.code)
                in_queue_enrollments = list(
                    filter(lambda enrollment: enrollment.state == ENROLLMENT_STATE.IN_QUEUE, enrollments))

                if len(in_queue_enrollments) > 0:
                    in_queue_enrollments.sort(key=lambda enrollment: enrollment.date_subscribed)
                    oldest_enrollment = in_queue_enrollments[0]
                    new_enrolled_enrollment = self.repo_activity.update_enrollment(user_id=oldest_enrollment.user_id,
                                                                                    code=activity.code,
                                                                                    new_state=ENROLLMENT_STATE.ENROLLED)
                    user_to_enroll = self.repo_user.get_user_info(user_id=new_enrolled_enrollment.user_id)
                    sent_email = self.repo_activity.send_enrolled_email(user_to_enroll, activity)
                    
                    if not sent_email:
                        self.observability._log_info(f"Error sending email to user with email = {user_to_enroll.email}") 
                        print("Error sending email")# for debug purposes

        self.repo_activity.delete_certificates(email=user_info.email)
        self.observability._log_info(f"Certificates deleted with user_id = {user_info.user_id}")
        
        self.repo_user.delete_user(email=user_info.email)
        self.observability._log_info(f"User deleted with user_id = {user_info.user_id}")
        
        self.repo_activity.send_deleted_user_email(user_info)
        self.observability._log_info(f"Email was sent to deleted user with email = {user_info.email}")
        
        self.observability.log_usecase_out()
        return user_info


