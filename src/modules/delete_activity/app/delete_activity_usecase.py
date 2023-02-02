from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction


class DeleteActivityUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, code: str, user: User) -> Activity:

        if type(code) != str:
            raise EntityError("code")

        if user.role != ROLE.ADMIN:
            # raise ForbiddenAction("delete_activity, only admins can delete activities")
            pass

        activity, enrollments = self.repo.get_activity_with_enrollments(code)

        if activity is None:
            raise NoItemsFound("Activity")

        activity = self.repo.delete_activity(code)

        if len(enrollments) > 0:
            new_enrollemnts = self.repo.batch_update_enrollment(enrollments, ENROLLMENT_STATE.ACTIVITY_CANCELLED)

        return activity

