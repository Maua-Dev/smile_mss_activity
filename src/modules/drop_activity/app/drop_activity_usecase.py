from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction


class DropActivityUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, user_id: str, code: str) -> Enrollment:
        if not User.validate_user_id(user_id):
            raise EntityError('user_id')

        if type(code) is not str:
            raise EntityError('code')

        activity = self.repo.get_activity(code)
        if activity is None:
            raise NoItemsFound('activity')
        taken_slots = activity.taken_slots
        enrollment = self.repo.get_enrollment(user_id, code)
        if enrollment is None:
            raise NoItemsFound('enrollment')

        if enrollment.state != ENROLLMENT_STATE.ENROLLED or enrollment != ENROLLMENT_STATE.IN_QUEUE:
            raise ForbiddenAction('enrollment')

        updated_enrollment = self.repo.update_enrollment(user_id=user_id, code=code, state=ENROLLMENT_STATE.DROPPED)

        if taken_slots >= activity.total_slots:
            activity, enrollments = self.repo.get_activity_with_enrollments(code)
            in_queue_enrollments = list(filter(lambda enrollment: enrollment.state == ENROLLMENT_STATE.IN_QUEUE, enrollments))
            if len(in_queue_enrollments) > 0:
                in_queue_enrollments.sort(key=lambda enrollment: enrollment.date_subscribed)
                oldest_enrollment = in_queue_enrollments[0]
                new_enrolled_enrollment = self.repo.update_enrollment(user_id=oldest_enrollment.user.user_id, code=code, state=ENROLLMENT_STATE.ENROLLED)

        return updated_enrollment
