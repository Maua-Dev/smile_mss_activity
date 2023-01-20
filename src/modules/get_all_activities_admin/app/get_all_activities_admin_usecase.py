from typing import List, Tuple

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository


class GetAllActivitiesAdminUsecase:

    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self) -> List[Tuple[Activity, List[Enrollment]]]:
        return self.repo.get_all_activities_admin()
