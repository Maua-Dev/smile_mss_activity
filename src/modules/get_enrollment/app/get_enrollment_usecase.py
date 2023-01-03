from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetEnrollmentUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, user_id: str, code: str) -> Enrollment:

        if not User.validate_user_id(user_id):
            raise EntityError("user_id")

        if type(code) is not str:
            raise EntityError("code")

        enrollment = self.repo.get_enrollment(user_id, code)

        if enrollment is None:
            raise NoItemsFound("enrollment")

        return enrollment
