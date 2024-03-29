from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction


class DeleteActivityUsecase:
    def __init__(self, repo: IActivityRepository, observability: IObservability):
        self.repo = repo
        self.observability = observability

    def __call__(self, code: str, user: User) -> Activity:
        self.observability.log_usecase_in()
        if not Activity.validate_activity_code(code):
            raise EntityError("code")

        if user.role != ROLE.ADMIN:
            raise ForbiddenAction("delete_activity, only admins can delete activities")

        activity, enrollments = self.repo.get_activity_with_enrollments(code)

        if activity is None:
            raise NoItemsFound("Activity")

        activity = self.repo.delete_activity(code)

        if len(enrollments) > 0:
            self.repo.batch_delete_enrollments([enrollment.user_id for enrollment in enrollments], code)

        self.observability.log_usecase_out()
        return activity

