from src.shared.domain.repositories.activity_repository_interface import IActivityRepository


class GetAllActivitiesLoggedUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, user_id: str) -> dict:

        activities, user_enrollments = self.repo.get_all_activities_logged(user_id=user_id)

        activities_logged = dict()

        for activity in activities:
            activities_logged[activity.code] = dict()
            activities_logged[activity.code]['activity'] = activity

        for enrollment in user_enrollments:
            activities_logged[enrollment.activity_code]['enrollment'] = enrollment

        return activities_logged




