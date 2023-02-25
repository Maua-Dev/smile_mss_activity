import datetime

from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class EnrollActivityUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, user_id: str, code: str) -> Enrollment:
        if not User.validate_user_id(user_id):
            raise EntityError('user_id')
    
        if type(code) is not str:
            raise EntityError('code')

        activity = self.repo.get_activity(code=code)
        if activity is None:
            raise NoItemsFound('Activity')

        enrollment = self.repo.get_enrollment(user_id=user_id, code=code)

        if enrollment is not None:
            raise ForbiddenAction('Enrollment')
                
        if not activity.accepting_new_enrollments:
            raise ForbiddenAction("Activity")

        else:

            if activity.taken_slots >= activity.total_slots:
                enrollment = Enrollment(activity_code=activity.code, user_id=user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                                        date_subscribed=int(datetime.datetime.now().timestamp() * 1000))

            else:
                enrollment = Enrollment(activity_code=activity.code, user_id=user_id, state=ENROLLMENT_STATE.ENROLLED,
                                        date_subscribed=int(datetime.datetime.now().timestamp() * 1000))

        return self.repo.create_enrollment(enrollment)
