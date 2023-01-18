from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class DeleteActivityUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, code: str) -> Activity:

        if type(code) != str:
            raise EntityError("code")

        activity, enrollments = self.repo.get_activity_with_enrollments(code)

        if activity is None:
            raise NoItemsFound("Activity")

        activity = self.repo.delete_activity(code)

        for enrollment in enrollments:
            self.repo.update_enrollment(user_id=enrollment.user.user_id, code=code, new_state=ENROLLMENT_STATE.ACTIVITY_CANCELLED)

        return activity

