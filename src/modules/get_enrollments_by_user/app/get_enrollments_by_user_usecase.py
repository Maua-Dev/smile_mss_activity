from typing import List

from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError


class GetEnrollmentsByUserUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, user_id: str) -> List[Enrollment]:

        if not User.validate_user_id(user_id=user_id):
            raise EntityError('user_id')

        return self.repo.get_enrollments_by_user_id(user_id=user_id)
