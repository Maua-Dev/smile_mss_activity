from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class UpdateActivityUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository):
        self.repo_activity = repo_activity
        self.repo_user = repo_user

    def __call__(self, code: str, new_title: str, new_description: str, new_activity_type: ACTIVITY_TYPE,
                 new_is_extensive: bool, new_delivery_model: DELIVERY_MODEL,
                 new_start_date: int, new_duration: int, new_place: str,
                 new_responsible_professors_user_id: List[str],
                 new_speakers: List[Speaker], new_total_slots: int,
                 new_accepting_new_enrollments: bool,
                 new_stop_accepting_new_enrollments_before: int, user: User, new_link: str = None) -> Activity:

        if user.role != ROLE.ADMIN:
            raise ForbiddenAction("update_activity, only admins can update activities")

        if not Activity.validate_activity_code(code):
            raise EntityError("code")
        activity = self.repo_activity.get_activity(code=code)

        if activity is None:
            raise NoItemsFound("Activity")

        if type(new_responsible_professors_user_id) != list:
            raise EntityError("responsible_professors")

        if not all(type(user_id) == str for user_id in new_responsible_professors_user_id):
            raise EntityError("responsible_professors")

        old_responsible_professors = activity.responsible_professors

        old_responsible_professors_user_id = [professor.user_id for professor in old_responsible_professors]

        old_responsible_professors_user_id.sort()

        new_responsible_professors_user_id.sort()

        if old_responsible_professors_user_id != new_responsible_professors_user_id:
            new_responsible_professors = self.repo_user.get_users(new_responsible_professors_user_id)

            if len(new_responsible_professors) != len(new_responsible_professors_user_id):
                raise NoItemsFound("responsible_professors")

        else:
            new_responsible_professors = old_responsible_professors

        if type(new_title) != str:
            raise EntityError("title")

        if type(new_description) != str:
            raise EntityError("description")

        if type(new_activity_type) != ACTIVITY_TYPE:
            raise EntityError("activity_type")

        if type(new_is_extensive) != bool:
            raise EntityError("is_extensive")

        if type(new_delivery_model) != DELIVERY_MODEL:
            raise EntityError("delivery_model")

        if type(new_start_date) != int:
            raise EntityError("start_date")

        if type(new_duration) != int:
            raise EntityError("duration")

        if new_link is None and new_place is None:
            raise EntityError("link or place")

        if type(new_link) != str and new_link is not None:
            raise EntityError("link")

        if type(new_place) != str and new_place is not None:
            raise EntityError("place")


        if type(new_responsible_professors) != list:
            raise EntityError("responsible_professors")

        elif not all([type(encharged_professor) == User for encharged_professor in
                      new_responsible_professors]):  # check if all elements are User
            raise EntityError("responsible_professors")

        elif not all([encharged_professor.role == ROLE.PROFESSOR for encharged_professor in
                      new_responsible_professors]):  # check if all elements are professors
            raise EntityError("responsible_professors")


        if type(new_speakers) != list:
            raise EntityError("speakers")

        if not all([type(speaker) == Speaker for speaker in new_speakers]):  # check if all elements are Speaker
            raise EntityError("speakers")

        if type(new_total_slots) != int:
            raise EntityError("total_slots")

        if type(activity.taken_slots) != int:
            raise EntityError("taken_slots")

        if type(new_accepting_new_enrollments) != bool:
            raise EntityError("accepting_new_enrollments")

        if type(new_stop_accepting_new_enrollments_before) != int and new_stop_accepting_new_enrollments_before is not None:
            raise EntityError("stop_accepting_new_enrollments_before")

        return self.repo_activity.update_activity(code=code,
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
