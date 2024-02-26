from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction

class DownloadActivityUsecase:
    def __init__(self, repo: IActivityRepository, observability: IObservability):
        self.repo = repo
        self.observability = observability
    def __call__(self, code: str, requester_user: User) -> str:
        self.observability.log_usecase_in()
        if not Activity.validate_activity_code(code):
            raise EntityError("code")
        
        if requester_user.role != ROLE.PROFESSOR and requester_user.role != ROLE.ADMIN:
            raise ForbiddenAction("user")
        
        activity = self.repo.get_activity(code)
        if activity is None:
            raise NoItemsFound("activity")
        
        if requester_user.role == ROLE.PROFESSOR:
            if requester_user.user_id not in [professor.user_id for professor in activity.responsible_professors]:
                raise ForbiddenAction("user")
            
        download_link = self.repo.download_activities(code)

        self.observability.log_usecase_out()
        return download_link