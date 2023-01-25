import datetime
from typing import List, Dict

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound


class CreateActivityUsecase:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo

    def __call__(self, code: str, title: str, description: str, activity_type: ACTIVITY_TYPE, is_extensive: bool,
                 delivery_model: DELIVERY_MODEL, start_date: int, duration: int, link: str, place: str,
                 total_slots: int,
                 accepting_new_enrollments: bool, responsible_professors_user_id: List[str],
                 stop_accepting_new_enrollments_before: int, speakers: List[Speaker]) -> Activity:

        if type(code) != str:
            raise EntityError("code")

        if self.repo.get_activity(code=code) is not None:
            raise DuplicatedItem("code")

        if len(responsible_professors_user_id) == 0:
            raise EntityError("responsible_professors")

        if type(responsible_professors_user_id) != list:
            raise EntityError("responsible_professors")

        if not all(type(user_id) == str for user_id in responsible_professors_user_id):
            raise EntityError("responsible_professors")

        responsible_professors = self.repo.get_users(responsible_professors_user_id)

        if len(responsible_professors) != len(responsible_professors_user_id):
            raise NoItemsFound("responsible_professors")

        activity = Activity(
            code=code,
            title=title,
            description=description,
            activity_type=activity_type,
            is_extensive=is_extensive,
            delivery_model=delivery_model,
            start_date=start_date,
            duration=duration,
            link=link,
            place=place,
            responsible_professors=responsible_professors,
            speakers=speakers,
            total_slots=total_slots,
            taken_slots=0,
            accepting_new_enrollments=accepting_new_enrollments,
            stop_accepting_new_enrollments_before=stop_accepting_new_enrollments_before
        )

        return self.repo.create_activity(activity)
