from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction

class DeleteAttendanceConfirmationUsecase:
       def __init__(self, repo: IActivityRepository):
              self.repo = repo

       def __call__(self, code: str, requester_user: User) -> str:
              if type(code) != str:
                     raise EntityError("activity_code")

              if requester_user.role != ROLE.PROFESSOR:
                     raise ForbiddenAction("user")

              activity = self.repo.get_activity(code)

              if activity is None:
                     raise NoItemsFound("activity")

              if activity.confirmation_code is None:
                     raise ForbiddenAction("confirmation_code")

              if requester_user not in activity.responsible_professors:
                     raise ForbiddenAction("user")

              delete_confirmation_code = None

              update_activity = self.repo.update_activity(
                     code=code,
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
                     new_confirmation_code=delete_confirmation_code,
              )

              return delete_confirmation_code
