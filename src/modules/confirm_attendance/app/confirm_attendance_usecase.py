from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class ConfirmAttendanceUsecase:

    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, user_id: str, activity_code: str, confirmation_code: str) -> bool:

        activity = self.repo.get_activity(activity_code)

        if activity is None:
            raise ForbiddenAction("trying to confirm attendance in activity not found")
        
        enrollment = self.repo.get_enrollment(
            user_id=user_id, code=activity_code
        )

        if enrollment is None:
            raise ForbiddenAction("trying to confirm attendance in activity not enrolled")
        
        if enrollment.state == ENROLLMENT_STATE.COMPLETED:
            raise ForbiddenAction("enrollment already COMPLETED")
        
        if enrollment.state != ENROLLMENT_STATE.ENROLLED:
            raise ForbiddenAction("enrollment not in ENROLLED state to confirm attendance")
        
        if activity.confirmation_code == confirmation_code:
            enrollment.state = ENROLLMENT_STATE.COMPLETED
            enrollment_updated = self.repo.update_enrollment(
                user_id=user_id, code=activity_code, new_state=ENROLLMENT_STATE.COMPLETED)
            if enrollment_updated is not None:
                return True

        return False