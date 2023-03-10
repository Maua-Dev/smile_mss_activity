from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class ConfirmAttendanceUsecase:

    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, user_id: str, code: str, confirmation_code: str) -> bool:

        if Activity.validate_confirmation_code(confirmation_code=confirmation_code) is False:
            raise EntityError('Confirmation Code')

        if type(code) is not str:
            raise EntityError('Activity Code')

        activity = self.repo.get_activity(code)

        if activity is None:
            raise NoItemsFound("activity")
        
        enrollment = self.repo.get_enrollment(
            user_id=user_id, code=code
        )

        if enrollment is None:
            raise ForbiddenAction("not_enrolled")
        
        if enrollment.state == ENROLLMENT_STATE.COMPLETED:
            raise ForbiddenAction("completed")
        
        if enrollment.state != ENROLLMENT_STATE.ENROLLED:
            raise ForbiddenAction("enrolled")
        
        if activity.confirmation_code == confirmation_code:
            enrollment.state = ENROLLMENT_STATE.COMPLETED
            enrollment_updated = self.repo.update_enrollment(
                user_id=user_id, code=code, new_state=ENROLLMENT_STATE.COMPLETED)
            if enrollment_updated is not None:
                return True
        else:
            raise ForbiddenAction("confirmation_code")

        return False
