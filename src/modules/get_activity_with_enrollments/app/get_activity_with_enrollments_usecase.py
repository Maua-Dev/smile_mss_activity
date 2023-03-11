from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound

class GetActivityWithEnrollmentsUsecase:

    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository):
        self.repo_activity = repo_activity
        self.repo_user = repo_user

    def __call__(self, user: User, code: str) -> dict:
        if user.role != ROLE.PROFESSOR and user.role != ROLE.ADMIN:
            raise ForbiddenAction("user: only responsible professors and admin can do that")

        if type(code) != str:
            raise EntityError('code')
        activity, all_enrollments = self.repo_activity.get_activity_with_enrollments(code=code)

        if activity is None:
            raise NoItemsFound('activity')

        if user.role == ROLE.PROFESSOR:
            if user not in activity.responsible_professors:
                raise ForbiddenAction('user')

        enrollments = [enrollment for enrollment in all_enrollments if enrollment.state in [ENROLLMENT_STATE.ENROLLED, ENROLLMENT_STATE.IN_QUEUE, ENROLLMENT_STATE.COMPLETED]]
        user_id_list = list()
        activity_with_enrollments = list()
        for enrollment in enrollments:
            user_id_list.append(enrollment.user_id)

        users = self.repo_user.get_users_info(user_id_list)

        users_dict = {user.user_id: user for user in users}

        activity_dict = dict()

        activity_dict = {

            "activity": activity,
            "enrollments": [
                (enrollment, users_dict.get(enrollment.user_id, "NOT_FOUND")) for enrollment in enrollments
                ]

            }
        return activity_dict
