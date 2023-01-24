from typing import List
import datetime
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, DuplicatedItem


class UpdateActivityUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, code: str, new_title: str, new_description: str, new_activity_type: ACTIVITY_TYPE,
                 new_is_extensive: bool, new_delivery_model: DELIVERY_MODEL,
                 new_start_date: int, new_duration: int, new_link: str, new_place: str,
                 new_responsible_professors_user_id: List[str],
                 new_speakers: List[Speaker], new_total_slots: int,
                 new_accepting_new_enrollments: bool,
                 new_stop_accepting_new_enrollments_before: int) -> Activity:

        if type(code) != str:
            raise EntityError("code")
        activity = self.repo.get_activity(code=code)

        if activity is None:
            raise NoItemsFound("Activity")

        if not all(type(user_id) == str for user_id in new_responsible_professors_user_id):
            raise EntityError("responsible_professors")

        new_responsible_professors = self.repo.get_users(new_responsible_professors_user_id)

        if len(new_responsible_professors) != len(new_responsible_professors_user_id):
            raise NoItemsFound("responsible_professors")

        new_activity = Activity(
            code=code,
            title=new_title,
            description=new_description,
            activity_type=new_activity_type,
            is_extensive=new_is_extensive,
            delivery_model=new_delivery_model,
            start_date=new_start_date,
            duration=new_duration,
            link=new_link,
            place=new_place,
            responsible_professors=new_responsible_professors,
            speakers=new_speakers,
            total_slots=new_total_slots,
            taken_slots=activity.taken_slots,
            accepting_new_enrollments=new_accepting_new_enrollments,
            stop_accepting_new_enrollments_before=new_stop_accepting_new_enrollments_before
        )

        return self.repo.update_activity(code=code,
                                         new_title=new_title,
                                         new_description=new_description,
                                         new_activity_type=new_activity_type,
                                         new_is_extensive=new_is_extensive,
                                         new_delivery_model=new_delivery_model,
                                         new_start_date=new_start_date,
                                         new_duration=new_duration,
                                         new_link=new_link,
                                         new_place=new_place,
                                         new_responsible_professors=new_responsible_professors,
                                         new_speakers=new_speakers,
                                         new_total_slots=new_total_slots,
                                         new_taken_slots=activity.taken_slots,
                                         new_accepting_new_enrollments=new_accepting_new_enrollments,
                                         new_stop_accepting_new_enrollments_before=new_stop_accepting_new_enrollments_before)
