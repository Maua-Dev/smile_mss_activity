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
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class UpdateActivityUsecase:
       def __init__(self, repo: IActivityRepository):
              self.repo = repo

       def __call__(self, code: str, new_title: str = None, new_description: str = None, new_activity_type: str = None,
                     new_is_extensive: bool = None, new_delivery_model: str = None,
                     new_start_date: datetime.datetime = None, new_duration: int = None,new_responsible_professors: List[User] = None,
                     new_speakers: List[Speaker] = None, new_total_slots: int = None, new_taken_slots: int = None,
                     new_accepting_new_enrollments: bool = None,
                     new_stop_accepting_new_enrollments_before: datetime.datetime = None, **kwargs) -> Activity:
              
              if type(code) is not str:
                     raise EntityError('code')
              
              if new_title != None and type(new_title) is not str:
                     raise EntityError('new_title')

              if new_description != None and type(new_description) is not str:
                     raise EntityError('new_description')

              if new_activity_type != None:
                     activity_types = [activity_type.value for activity_type in ACTIVITY_TYPE]
                     if new_activity_type not in activity_types:
                            raise EntityError('new_activity_type')
                     new_activity_type = ACTIVITY_TYPE[new_activity_type]

              if new_is_extensive != None and type(new_is_extensive) is not bool:
                     raise EntityError('new_is_extensive')

              if new_delivery_model != None:
                     delivery_models = [delivery_model.value for delivery_model in DELIVERY_MODEL]
                     if new_delivery_model not in delivery_models:
                            raise EntityError('new_delivery_model')
                     new_delivery_model = DELIVERY_MODEL[new_delivery_model]
              
              if new_start_date != None and type(new_start_date) is not datetime.datetime:
                     raise EntityError('new_start_date')

              if new_duration != None and type(new_duration) is not int:
                     raise EntityError('new_duration')
              
              if new_responsible_professors != None and new_responsible_professors is List:
                     for professor in new_responsible_professors:
                            if type(professor) is not User:
                                   raise EntityError('new_responsible_professors')
                            if professor.role != ROLE.PROFESSOR:
                                   raise ForbiddenAction('Professor')
                            return professor

              if new_speakers != None and new_speakers is List:
                     for speaker in new_speakers:
                            if type(speaker) is not Speaker:
                                   raise EntityError('new_speakers')
                            return speaker

              if new_total_slots != None and type(new_total_slots) is not int:
                     raise EntityError('new_total_slots')

              if new_taken_slots != None and type(new_taken_slots) is not int:
                     raise EntityError('new_taken_slots')

              if new_accepting_new_enrollments != None and type(new_accepting_new_enrollments) is not bool:
                     raise EntityError('new_accepting_new_enrollments')

              if new_stop_accepting_new_enrollments_before != None and type(new_stop_accepting_new_enrollments_before) is not datetime.datetime:
                     raise EntityError('new_stop_accepting_new_enrollments_before')

              activity = self.repo.get_activity(code)
              if activity is None:
                     raise NoItemsFound('Activity')

              return self.repo.update_activity(code, new_title, new_description, new_activity_type,
                     new_is_extensive, new_delivery_model,
                     new_start_date, new_duration,new_responsible_professors,
                     new_speakers, new_total_slots, new_taken_slots,
                     new_accepting_new_enrollments,
                     new_stop_accepting_new_enrollments_before)

