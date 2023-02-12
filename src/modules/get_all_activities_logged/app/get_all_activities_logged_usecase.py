from src.shared.domain.entities.user import User
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository


class GetAllActivitiesLoggedUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, requester_user: User) -> dict:
        activities, enrollments = self.repo.get_all_activities_logged(user_id=requester_user.user_id)
