from datetime import datetime
from typing import Tuple

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ClosedActivity, ActivityEnded, UserAlreadyEnrolled, \
    UserAlreadyCompleted, ForbiddenAction, UserNotAdmin


class EnrollActivityAdminUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository, observability: IObservability):
        self.repo_activity = repo_activity
        self.repo_user = repo_user
        self.observability = observability
    def __call__(self, requester_user: User,  user_id: str, code: str) -> Tuple[Enrollment, User]:
        self.observability.log_usecase_in()
        if requester_user.role != ROLE.ADMIN:
            raise UserNotAdmin('User')

        if not User.validate_user_id(user_id):
            raise EntityError('user_id')

        if not Activity.validate_activity_code(code):
            raise EntityError("code")

        enroll_user = self.repo_user.get_user(user_id=user_id)

        if enroll_user is None:
            raise NoItemsFound('User')

        activity = self.repo_activity.get_activity(code=code)
        if activity is None:
            raise NoItemsFound('Activity')

        # if not activity.accepting_new_enrollments:
        #     raise ClosedActivity("Activity")
        #
        # activity_end_time = activity.start_date + activity.duration * 60 * 1000
        #
        # if activity_end_time < datetime.now().timestamp() * 1000:
        #     raise ActivityEnded("Activity")

        enrollment = self.repo_activity.get_enrollment(user_id=user_id, code=code)

        if enrollment is not None:

            original_state = enrollment.state
            if original_state == ENROLLMENT_STATE.ENROLLED or original_state == ENROLLMENT_STATE.IN_QUEUE:
                raise UserAlreadyEnrolled('Enrollment')

            if original_state == ENROLLMENT_STATE.COMPLETED:
                raise UserAlreadyCompleted('Enrollment')

            raise ForbiddenAction('Enrollment')

        else:

            if activity.taken_slots >= activity.total_slots:
                enrollment = Enrollment(activity_code=activity.code, user_id=user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                                        date_subscribed=int(datetime.now().timestamp() * 1000))

            else:
                enrollment = Enrollment(activity_code=activity.code, user_id=user_id, state=ENROLLMENT_STATE.ENROLLED,
                                        date_subscribed=int(datetime.now().timestamp() * 1000))

        response = self.repo_activity.create_enrollment(enrollment), enroll_user
        self.observability.log_usecase_out()
        return response
