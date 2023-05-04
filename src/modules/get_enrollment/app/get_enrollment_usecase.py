from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetEnrollmentUsecase:
    def __init__(self, repo: IActivityRepository, observability: IObservability):
        self.repo = repo
        self.observability = observability

    def __call__(self, user_id: str, code: str) -> Enrollment:
        self.observability.log_usecase_in()

        if not User.validate_user_id(user_id):
            raise EntityError("user_id")

        if not Activity.validate_activity_code(code):
            raise EntityError("code")

        enrollment = self.repo.get_enrollment(user_id, code)

        if enrollment is None:
            raise NoItemsFound("enrollment")
        self.observability.log_usecase_out()

        return enrollment
