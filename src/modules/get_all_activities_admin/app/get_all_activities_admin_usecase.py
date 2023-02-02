from typing import List, Tuple, Dict

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class GetAllActivitiesAdminUsecase:

    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, user: User) -> dict:

        if user.role != ROLE.ADMIN:
            # raise ForbiddenAction("get_all_activities_with_enrollments, only admins can do this")
            pass

        activities_with_enrollments = self.repo.get_all_activities_admin()

        user_id_list = list()
        for activity, enrollments in activities_with_enrollments:
            user_id_list.extend([enrollment.user_id for enrollment in enrollments])

        set_user_id_list = set(user_id_list)

        users = self.repo.get_users(list(set_user_id_list))

        users_dict = {user.user_id: user for user in users}

        all_activities_dict = dict()
        for activity, enrollments in activities_with_enrollments:
            all_activities_dict[activity.code] = {
                "activity": activity,
                "enrollments": [
                    (enrollment, users_dict.get(enrollment.user_id, "NOT_FOUND")) for enrollment in enrollments
                ]
            }

        return all_activities_dict
