from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class GetAllActivitiesAdminUsecase:

    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository, observability: IObservability):
        self.repo_activity = repo_activity
        self.repo_user = repo_user
        self.observability = observability

    def __call__(self, user: User) -> dict:
        self.observability.log_usecase_in()

        if user.role != ROLE.ADMIN:
            raise ForbiddenAction("get_all_activities_with_enrollments, only admins can do this")

        activities_with_enrollments = self.repo_activity.get_all_activities_admin()
        activities_with_enrollments.sort(key=lambda a: a[0].start_date)

        user_id_list = list()
        for activity, enrollments in activities_with_enrollments:
            user_id_list.extend([enrollment.user_id for enrollment in enrollments])

        set_user_id_list = set(user_id_list)

        users = self.repo_user.get_users_info(list(set_user_id_list))

        users_dict = {user.user_id: user for user in users}

        all_activities_dict = dict()
        for activity, enrollments in activities_with_enrollments:
            all_activities_dict[activity.code] = {
                "activity": activity,
                "enrollments": [
                    (enrollment, users_dict.get(enrollment.user_id, "NOT_FOUND")) for enrollment in enrollments
                ]
            }
            
        self.observability.log_usecase_out()
        return all_activities_dict
