from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository


class GetAllActivitiesUsecase:

    def __init__(self, repo: IActivityRepository, observability: IObservability):
        self.repo = repo
        self.observability = observability

    def __call__(self) -> List[Activity]:
        self.observability.log_usecase_in()
        
        activities = self.repo.get_all_activities()
        activities.sort(key=lambda x: x.start_date)

        self.observability.log_usecase_out()
        return activities
