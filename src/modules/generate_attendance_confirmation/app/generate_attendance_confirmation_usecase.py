from random import randint

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction


class GenerateAttendanceConfirmationUsecase:
    def __init__(self, repo: IActivityRepository, observability: IObservability):
        self.repo = repo
        self.observability = observability

    def __call__(self, code: str, requester_user: User) -> str:
        self.observability.log_usecase_in()
        if not Activity.validate_activity_code(code):
            raise EntityError("activity_code")

        if requester_user.role != ROLE.PROFESSOR and requester_user.role != ROLE.ADMIN:
            raise ForbiddenAction("user, not professor")

        activity = self.repo.get_activity(code)

        if activity is None:
            raise NoItemsFound("activity")

        if activity.confirmation_code is not None:
            raise ForbiddenAction("confirmation_code")

        if requester_user.role == ROLE.PROFESSOR:
            if requester_user.user_id not in [professor.user_id for professor in activity.responsible_professors]:
                raise ForbiddenAction("user")

        confirmation_code = self.generate_confirmation_code()

        update_activity = self.repo.update_activity(code=code,
                                         new_title=activity.title,
                                         new_description=activity.description,
                                         new_activity_type=activity.activity_type,
                                         new_is_extensive=activity.is_extensive,
                                         new_delivery_model=activity.delivery_model,
                                         new_start_date=activity.start_date,
                                         new_duration=activity.duration,
                                         new_link=activity.link,
                                         new_place=activity.place,
                                         new_responsible_professors=activity.responsible_professors,
                                         new_speakers=activity.speakers,
                                         new_total_slots=activity.total_slots,
                                         new_taken_slots=activity.taken_slots,
                                         new_accepting_new_enrollments=activity.accepting_new_enrollments,
                                         new_stop_accepting_new_enrollments_before=activity.stop_accepting_new_enrollments_before,
                                         new_confirmation_code=confirmation_code,)

        self.observability.log_usecase_out()
        return confirmation_code

    @staticmethod
    def generate_confirmation_code() -> str:
        confirmation_code = "".join([str(randint(0, 9)) for _ in range(6)])

        return confirmation_code
