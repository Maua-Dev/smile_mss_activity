from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository


class GetAllActivitiesLoggedUsecase:
    def __init__(self, repo: IActivityRepository, observability: IObservability):
        self.repo = repo
        self.observability = observability

    def __call__(self, user_id: str) -> dict:
        self.observability.log_usecase_in()

        activities, user_enrollments = self.repo.get_all_activities_logged(user_id=user_id)
        activities.sort(key=lambda a: a.start_date)

        activities_logged = dict()

        for activity in activities:
            activities_logged[activity.code] = dict()
            activities_logged[activity.code]['activity'] = activity

        for enrollment in user_enrollments:
            activities_logged[enrollment.activity_code]['enrollment'] = enrollment
        self.observability.log_usecase_out()

        return activities_logged




