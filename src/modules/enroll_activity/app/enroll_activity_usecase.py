import datetime

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ClosedActivity, \
    UserAlreadyEnrolled, UserAlreadyCompleted, ForbiddenAction, ActivityEnded, ImpossibleEnrollment


class EnrollActivityUsecase:
    def __init__(self, repo: IActivityRepository, observability: IObservability):
        self.repo = repo
        self.observability = observability

    def __call__(self, user_id: str, code: str) -> Enrollment:
        self.observability.log_usecase_in()
        if not User.validate_user_id(user_id):
            raise EntityError('user_id')
    
        if not Activity.validate_activity_code(code):
            raise EntityError("code")

        activity = self.repo.get_activity(code=code)
        if activity is None:
            raise NoItemsFound('Activity')
 
        if not activity.accepting_new_enrollments:
            raise ClosedActivity("Activity")


        if activity.end_date < datetime.datetime.now().timestamp() * 1000:
            raise ActivityEnded("Activity")

        enrollment = self.repo.get_enrollment(user_id=user_id, code=code)
        if enrollment is not None:

            original_state = enrollment.state
            if original_state == ENROLLMENT_STATE.ENROLLED or original_state == ENROLLMENT_STATE.IN_QUEUE:
                raise UserAlreadyEnrolled('Enrollment')

            if original_state == ENROLLMENT_STATE.COMPLETED:
                raise UserAlreadyCompleted('Enrollment')

            raise ForbiddenAction('Enrollment')

        else:
            enrollments = self.repo.get_enrollments_by_user_id(user_id=user_id)

            enrollmentes_filtered = list(filter(lambda enrollment: enrollment.state == ENROLLMENT_STATE.ENROLLED, enrollments))

            user_activities = self.repo.batch_get_activities([enrollment.activity_code for enrollment in enrollmentes_filtered])

            for user_activity in user_activities:
                if (activity.start_date - user_activity.end_date)/60000 > 15 and activity.start_date//86400000 == user_activity.start_date//86400000:
                    raise ImpossibleEnrollment("Activity")
                
            if activity.taken_slots >= activity.total_slots:
                enrollment = Enrollment(activity_code=activity.code, user_id=user_id, state=ENROLLMENT_STATE.IN_QUEUE,
                                    date_subscribed=int(datetime.datetime.now().timestamp() * 1000))

            else:
                enrollment = Enrollment(activity_code=activity.code, user_id=user_id, state=ENROLLMENT_STATE.ENROLLED,
                                        date_subscribed=int(datetime.datetime.now().timestamp() * 1000))

        enrollment_response = self.repo.create_enrollment(enrollment)
        self.observability.log_usecase_out()
        return enrollment_response

