from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction


class ManualDropActivityUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository):
        self.repo_activity = repo_activity
        self.repo_user = repo_user

    def __call__(self, user_id: str, code: str, requester_user: User) -> object:

        if not User.validate_user_id(user_id):
            raise EntityError('user_id')

        if not Activity.validate_activity_code(code):
            raise EntityError("code")

        if requester_user.role != ROLE.PROFESSOR and requester_user.role != ROLE.ADMIN:
            raise ForbiddenAction("user: only responsible professors can do that")

        activity, all_enrollments = self.repo_activity.get_activity_with_enrollments(code=code)

        if activity is None:
            raise NoItemsFound('Activity')

        if requester_user.role == ROLE.PROFESSOR:
            if requester_user not in activity.responsible_professors:
                raise ForbiddenAction("user: only responsible professors for this activity can do that")

        taken_slots = activity.taken_slots
        original_enrollment = next((enrollment for enrollment in all_enrollments if enrollment.user_id == user_id),
                                   None)

        if original_enrollment is None:
            raise NoItemsFound('Enrollment')

        original_state = original_enrollment.state
        if original_state != ENROLLMENT_STATE.ENROLLED and original_state != ENROLLMENT_STATE.IN_QUEUE:
            raise ForbiddenAction('enrollment')

        updated_enrollment = self.repo_activity.update_enrollment(user_id=user_id, code=code,
                                                                  new_state=ENROLLMENT_STATE.DROPPED)
        for enrollment in all_enrollments:
            if enrollment.user_id == updated_enrollment.user_id:
                enrollment.state = updated_enrollment.state

        if taken_slots >= activity.total_slots and original_state == ENROLLMENT_STATE.ENROLLED:

            in_queue_enrollments = list(filter(lambda enrollment: enrollment.state == ENROLLMENT_STATE.IN_QUEUE,
                                               all_enrollments))

            if len(in_queue_enrollments) > 0:
                in_queue_enrollments.sort(key=lambda enrollment: enrollment.date_subscribed)
                oldest_enrollment = in_queue_enrollments[0]
                new_enrolled_enrollment = self.repo_activity.update_enrollment(user_id=oldest_enrollment.user_id,
                                                                               code=code,
                                                                               new_state=ENROLLMENT_STATE.ENROLLED)

                user = self.repo_user.get_user_info(user_id=new_enrolled_enrollment.user_id)

                sent_email = self.repo_activity.send_enrolled_email(user, activity)

                if not sent_email:
                    print('Error sending email to user: ' + user_id)

                for enrollment in all_enrollments:
                    if enrollment.user_id == new_enrolled_enrollment.user_id:
                        enrollment.state = new_enrolled_enrollment.state

        new_activity, new_enrollments = self.repo_activity.get_activity_with_enrollments(code=code)

        enrollments = [enrollment for enrollment in new_enrollments if enrollment.state == ENROLLMENT_STATE.ENROLLED or
                       enrollment.state == ENROLLMENT_STATE.COMPLETED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE]

        user_id_list = list()
        for enrollment in enrollments:
            user_id_list.append(enrollment.user_id)
        users = self.repo_user.get_users_info(user_id_list)
        users_dict = {user.user_id: user for user in users}
        activity_dict = {
            "activity": new_activity,
            "enrollments": [
                (enrollment, users_dict.get(enrollment.user_id, "NOT_FOUND")) for enrollment in enrollments
            ]
        }
        return activity_dict
