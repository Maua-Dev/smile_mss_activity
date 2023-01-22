from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository


class GetAllActivitiesUsecase:

    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self) -> List[Activity]:
        return self.repo.get_all_activities()
