import datetime
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction, UserAlreadyCompleted, ActivityEnded


class DropActivityUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository):
        self.repo_activity = repo_activity
        self.repo_user = repo_user

    def __call__(self, user_id: str, code: str) -> Enrollment:
        if not User.validate_user_id(user_id):
            raise EntityError('user_id')

        if not Activity.validate_activity_code(code):
            raise EntityError("code")

        activity = self.repo_activity.get_activity(code)
        if activity is None:
            raise NoItemsFound('Activity')

        activity_end_time = activity.start_date + activity.duration * 60 * 1000

        if activity_end_time < datetime.datetime.now().timestamp() * 1000:
            raise ActivityEnded('activity')

        taken_slots = activity.taken_slots
        original_enrollment = self.repo_activity.get_enrollment(user_id, code)
        if original_enrollment is None:
            raise NoItemsFound('Enrollment')

        original_state = original_enrollment.state

        if original_state == ENROLLMENT_STATE.COMPLETED:
            raise UserAlreadyCompleted('Enrollment')

        if original_state != ENROLLMENT_STATE.ENROLLED and original_state != ENROLLMENT_STATE.IN_QUEUE:
            raise ForbiddenAction('Enrollment')

        updated_enrollment = self.repo_activity.update_enrollment(user_id=user_id, code=code, new_state=ENROLLMENT_STATE.DROPPED)

        if taken_slots >= activity.total_slots and original_state == ENROLLMENT_STATE.ENROLLED:
            activity, enrollments = self.repo_activity.get_activity_with_enrollments(code)
            in_queue_enrollments = list(filter(lambda enrollment: enrollment.state == ENROLLMENT_STATE.IN_QUEUE, enrollments))
            if len(in_queue_enrollments) > 0:
                in_queue_enrollments.sort(key=lambda enrollment: enrollment.date_subscribed)
                oldest_enrollment = in_queue_enrollments[0]
                new_enrolled_enrollment = self.repo_activity.update_enrollment(user_id=oldest_enrollment.user_id, code=code,
                                                                      new_state=ENROLLMENT_STATE.ENROLLED)
                user = self.repo_user.get_user_info(user_id=new_enrolled_enrollment.user_id)

                sent_email = self.repo_activity.send_enrolled_email(user, activity)

                if not sent_email:
                    print('Error sending email to user: ' + user_id)

        return updated_enrollment
