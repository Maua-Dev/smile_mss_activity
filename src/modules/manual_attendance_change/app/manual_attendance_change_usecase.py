from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class ManualAttendanceChangeUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository):
        self.repo_activity = repo_activity
        self.repo_user = repo_user

    def __call__(self, code: str, requester_user: User, user_id: str, new_state: ENROLLMENT_STATE):

        if type(code) != str:
            raise EntityError('activity_code')

        if not User.validate_user_id(user_id):
            raise EntityError('user_id')

        if type(new_state) != ENROLLMENT_STATE:
            raise EntityError('new_state')

        if requester_user.role != ROLE.PROFESSOR and requester_user.role != ROLE.ADMIN:
            raise ForbiddenAction("user: only responsible professors can do that")

        if new_state != ENROLLMENT_STATE.COMPLETED and new_state != ENROLLMENT_STATE.ENROLLED:
            raise EntityError('state')

        activity, all_enrollments = self.repo_activity.get_activity_with_enrollments(code=code)

        if activity is None:
            raise NoItemsFound('activity')

        enrollment = next((enrollment for enrollment in all_enrollments if enrollment.user_id == user_id), None)

        if enrollment is None:
            raise NoItemsFound('enrollment')

        if new_state == ENROLLMENT_STATE.COMPLETED:
            if enrollment.state != ENROLLMENT_STATE.ENROLLED:
                raise ForbiddenAction("enrollment: can\'t confirm it")

        if new_state == ENROLLMENT_STATE.ENROLLED:
            if enrollment.state != ENROLLMENT_STATE.COMPLETED:
                raise ForbiddenAction('enrollment: can\'t be unconfirmed')

        if requester_user.role == ROLE.PROFESSOR:
            if requester_user not in activity.responsible_professors:
                raise ForbiddenAction("user: only responsible professors for this activity can do that")

        new_enrollment = self.repo_activity.update_enrollment(
            user_id=enrollment.user_id,
            code=enrollment.activity_code,
            new_state=new_state
        )

        for enrollment in all_enrollments:
            if enrollment.user_id == new_enrollment.user_id:
                enrollment.state = new_enrollment.state

        enrollments = [enrollment for enrollment in all_enrollments if enrollment.state == ENROLLMENT_STATE.ENROLLED or
                       enrollment.state == ENROLLMENT_STATE.COMPLETED]

        user_id_list = list()
        for enrollment in enrollments:
            user_id_list.append(enrollment.user_id)
        users = self.repo_user.get_users(user_id_list)
        users_dict = {user.user_id: user for user in users}
        activity_dict = {
            "activity": activity,
            "enrollments": [
                (enrollment, users_dict.get(enrollment.user_id, "NOT_FOUND")) for enrollment in enrollments
                ]
        }

        return activity_dict
