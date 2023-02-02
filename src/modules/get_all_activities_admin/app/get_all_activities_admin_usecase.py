from typing import List, Tuple

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class GetAllActivitiesAdminUsecase:

    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, user: User) -> List[Tuple[Activity, List[Enrollment]]]:

        if user.role != ROLE.ADMIN:
            # raise ForbiddenAction("get_all_activities_with_enrollments, only admins can do this")
            pass

        return self.repo.get_all_activities_admin()
