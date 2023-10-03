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
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, UnecessaryUpdate


class UpdateActivityUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository, observability: IObservability):
        self.repo_activity = repo_activity
        self.repo_user = repo_user
        self.observability = observability

    def __call__(self, code: str, new_title: Optional[str] = None, new_description: Optional[str] = None, new_activity_type: Optional[ACTIVITY_TYPE] = None,
                 new_is_extensive: Optional[bool] = None, new_delivery_model: Optional[DELIVERY_MODEL] = None,
                 new_start_date: Optional[int] = None, new_duration: Optional[int] = None, new_place: Optional[str] = None,
                 new_responsible_professors_user_id: Optional[List[str]] = None,
                 new_speakers: Optional[List[Speaker]] = None, new_total_slots: Optional[int] = None,
                 new_accepting_new_enrollments: Optional[bool] = None,
                 new_stop_accepting_new_enrollments_before: Optional[int] = None, user: Optional[User] = None, new_link: Optional[str] = None) -> Activity:
        self.observability.log_usecase_in()

        if user.role != ROLE.ADMIN:
            raise ForbiddenAction("update_activity, only admins can update activities")

        if not Activity.validate_activity_code(code):
            raise EntityError("code")
        activity = self.repo_activity.get_activity(code=code)

        if activity is None:
            raise NoItemsFound("Activity")

        if type(activity.taken_slots) != int:
            raise EntityError("taken_slots")
        
        new_activity = Activity(code=code,
                                title=activity.title,
                                description=activity.description,
                                activity_type=activity.activity_type,
                                is_extensive=activity.is_extensive,
                                delivery_model=activity.delivery_model,
                                start_date=activity.start_date,
                                duration=activity.duration,
                                link=activity.link,
                                place=activity.place,
                                responsible_professors=activity.responsible_professors,
                                speakers=activity.speakers,
                                total_slots=activity.total_slots,
                                taken_slots=activity.taken_slots,
                                accepting_new_enrollments=activity.accepting_new_enrollments,
                                stop_accepting_new_enrollments_before=activity.stop_accepting_new_enrollments_before,
                                confirmation_code=activity.confirmation_code)

        if new_title is not None:
            if type(new_title) != str:
                raise EntityError("title")

            if new_title == activity.title:
                raise UnecessaryUpdate("title")
            
            new_activity.title = new_title

        if new_description is not None:
            if type(new_description) != str:
                raise EntityError("description")

            if new_description == activity.description:
                raise UnecessaryUpdate("description")

            new_activity.description = new_description
        
        if new_activity_type is not None:
            if new_activity_type == activity.activity_type:
                raise UnecessaryUpdate("activity_type")
            
            new_activity.activity_type = new_activity_type
        
        if new_is_extensive is not None:
            if type(new_is_extensive) != bool:
                raise EntityError("is_extensive")

            if new_is_extensive == activity.is_extensive:
                raise UnecessaryUpdate("is_extensive")
            
            new_activity.is_extensive = new_is_extensive
        
        if new_delivery_model is not None:
            if new_delivery_model == activity.delivery_model:
                raise UnecessaryUpdate("delivery_model")
            
            new_activity.delivery_model = new_delivery_model
        
        if new_start_date is not None:
            if type(new_start_date) != int:
                raise EntityError("start_date")

            if new_start_date == activity.start_date:
                raise UnecessaryUpdate("start_date")
            
            new_activity.start_date = new_start_date
        
        if new_duration is not None:
            if type(new_duration) != int:
                raise EntityError("duration")

            if new_duration == activity.duration:
                raise UnecessaryUpdate("duration")
            
            new_activity.duration = new_duration

        if new_link is not None:
            if type(new_link) != str:
                raise EntityError("link")

            if new_link == activity.link:
                raise UnecessaryUpdate("link")
            
            new_activity.link = new_link
        
        if new_place is not None:
            if type(new_place) != str:
                raise EntityError("place")

            if new_place == activity.place:
                raise UnecessaryUpdate("place")
            
            new_activity.place = new_place

        if new_responsible_professors_user_id  is not None:
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

                if type(new_responsible_professors) != list:
                    raise EntityError("responsible_professors")

                elif not all([type(encharged_professor) == User for encharged_professor in
                            new_responsible_professors]):
                    raise EntityError("responsible_professors")

                elif not all([encharged_professor.role == ROLE.PROFESSOR for encharged_professor in
                            new_responsible_professors]):
                    raise EntityError("responsible_professors")
        
        if new_speakers is not None:
            if type(new_speakers) != list:
                raise EntityError("speakers")

            if not all([type(speaker) == Speaker for speaker in new_speakers]): 
                raise EntityError("speakers")

            if not all(speaker != new_speaker for speaker, new_speaker in zip(activity.speakers, new_speakers)):
                raise UnecessaryUpdate("speakers")   
            
            new_activity.speakers = new_speakers

        if new_total_slots is not None:
            if type(new_total_slots) != int:
                raise EntityError("total_slots")

            if new_total_slots == activity.total_slots:
                raise UnecessaryUpdate("total_slots")
            
            new_activity.total_slots = new_total_slots	

        if new_accepting_new_enrollments is not None:
            if type(new_accepting_new_enrollments) != bool:
                raise EntityError("accepting_new_enrollments")

            if new_accepting_new_enrollments == activity.accepting_new_enrollments:
                raise UnecessaryUpdate("accepting_new_enrollments")
            
            new_activity.accepting_new_enrollments = new_accepting_new_enrollments

        if new_stop_accepting_new_enrollments_before is not None:
            if type(new_stop_accepting_new_enrollments_before) != int:
                raise EntityError("stop_accepting_new_enrollments_before")

            if new_stop_accepting_new_enrollments_before == activity.stop_accepting_new_enrollments_before:
                raise UnecessaryUpdate("stop_accepting_new_enrollments_before")
            
            new_activity.stop_accepting_new_enrollments_before = new_stop_accepting_new_enrollments_before


        activity = self.repo_activity.update_activity(code=code,
                                         new_title=new_activity.title,
                                         new_description=new_activity.description,
                                         new_activity_type=new_activity.activity_type,
                                         new_is_extensive=new_activity.is_extensive,
                                         new_delivery_model=new_activity.delivery_model,
                                         new_start_date=new_activity.start_date,
                                         new_duration=new_activity.duration,
                                         new_link=new_activity.link,
                                         new_place=new_activity.place,
                                         new_responsible_professors=new_activity.responsible_professors,
                                         new_speakers=new_activity.speakers,
                                         new_total_slots=new_activity.total_slots,
                                         new_taken_slots=new_activity.taken_slots,
                                         new_accepting_new_enrollments=new_activity.accepting_new_enrollments,
                                         new_stop_accepting_new_enrollments_before=new_activity.stop_accepting_new_enrollments_before)

        self.observability.log_usecase_out()
        return activity