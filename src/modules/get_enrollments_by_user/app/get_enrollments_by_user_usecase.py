from typing import List

from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError


class GetEnrollmentsByUserUsecase:
    def __init__(self, repo: IActivityRepository, observability: IObservability):
        self.repo = repo
        self.observability = observability

    def __call__(self, user_id: str) -> List[Enrollment]:
        self.observability.log_usecase_in()

        if not User.validate_user_id(user_id=user_id):
            raise EntityError('user_id')
        
        enrollments = self.repo.get_enrollments_by_user_id(user_id=user_id)
        self.observability.log_usecase_out()

        return enrollments
