from typing import List, Optional

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound, ForbiddenAction, \
    ConflictingInformation


class CreateActivityUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository, observability: IObservability):
        self.repo_activity = repo_activity
        self.repo_user = repo_user
        self.observability = observability

    def __call__(self, code: str, title: str, description: Optional[str], activity_type: ACTIVITY_TYPE, is_extensive: bool,
                 delivery_model: DELIVERY_MODEL, start_date: int, end_date: int, link: str, place: str,
                 total_slots: int,
                 accepting_new_enrollments: bool,stop_accepting_new_enrollments_before: int,
                speakers: Optional[List[Speaker]], user: User,responsible_professors_user_id: Optional[List[str]]) -> Activity:

        self.observability.log_usecase_in()
        if not Activity.validate_activity_code(code):
            raise EntityError("code")

        if user.role != ROLE.ADMIN:
            raise ForbiddenAction("create_activity, only admins can create activities")

        if self.repo_activity.get_activity(code=code) is not None:
            raise DuplicatedItem("activity_code")
        
        responsible_professors = None  
        if responsible_professors_user_id is not None:
            if type(responsible_professors_user_id) != list:
                raise EntityError("responsible_professors")

            if len(responsible_professors_user_id) == 0:
                raise EntityError("responsible_professors")

            if type(responsible_professors_user_id) != list:
                raise EntityError("responsible_professors")

            if not all(type(user_id) == str for user_id in responsible_professors_user_id):
                raise EntityError("responsible_professors")

            responsible_professors = self.repo_user.get_users(responsible_professors_user_id)

            if len(responsible_professors) != len(responsible_professors_user_id):
                raise NoItemsFound("responsible_professors")

        if delivery_model == DELIVERY_MODEL.ONLINE and place is not None:
            raise ConflictingInformation('local')

        if delivery_model == DELIVERY_MODEL.IN_PERSON and link is not None:
            raise ConflictingInformation('link')

        if start_date >= end_date:
            raise ConflictingInformation('start_date')

        activity = Activity(
            code=code,
            title=title,
            description=description,
            activity_type=activity_type,
            is_extensive=is_extensive,
            delivery_model=delivery_model,
            start_date=start_date,
            end_date=end_date,
            link=link,
            place=place,
            responsible_professors=responsible_professors,
            speakers=speakers,
            total_slots=total_slots,
            taken_slots=0,
            accepting_new_enrollments=accepting_new_enrollments,
            stop_accepting_new_enrollments_before=stop_accepting_new_enrollments_before,
            confirmation_code=None,
        )
        activity = self.repo_activity.create_activity(activity)
        self.observability.log_usecase_out()
        return activity
