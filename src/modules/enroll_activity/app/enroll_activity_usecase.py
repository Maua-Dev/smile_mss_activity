import abc
import datetime

from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.activity import Activity
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE

class EnrollActivityUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo
    

    def __call__(self, user_id: str, code: str) -> Enrollment:
        if not User.validate_user_id(user_id):
            raise EntityError('user_id')
    
        if type(code) is not str:
            raise EntityError('code')

        activity = self.repo.get_activity(code=code)
        enrollment = self.repo.get_enrollment(user_id=user_id, code=code)

        if type(enrollment) != None:
            if enrollment.state == ENROLLMENT_STATE.ENROLLED:
                raise ForbiddenAction('Enrollment')

            if activity.accepting_new_enrollments == True:

                if  activity.taken_slots >= activity.total_slots:

                    enrollment = Enrollment(
                        activity = self.repo.get_activity(code),
                        user = self.repo.get_user(user_id),
                        state = ENROLLMENT_STATE.IN_QUEUE,
                        date_subscribed = datetime.datetime.now()
                    )
                    return enrollment

                if  activity.taken_slots < activity.total_slots:

                    enrollment = Enrollment(
                        activity = self.repo.get_activity(code),
                        user = self.repo.get_user(user_id),
                        state = ENROLLMENT_STATE.ENROLLED,
                        date_subscribed = datetime.datetime.now()
                    )
                    return enrollment

        return self.repo.create_enrollment(enrollment)