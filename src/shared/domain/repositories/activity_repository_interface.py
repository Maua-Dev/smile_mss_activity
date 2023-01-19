from abc import ABC, abstractmethod
import datetime
from typing import List, Tuple

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE


class IActivityRepository(ABC):

    @abstractmethod
    def get_enrollment(self, user_id: str, code: str) -> Enrollment:
        """
        If the user is enrolled in the activity, returns the enrollment.
        else returns None

        Ignore dropped enrollments
        """
        pass

    @abstractmethod
    def get_activity(self, code:str) -> Activity:
        """
        If activity with the given code exists, returns it
        else returns None

        In dynamoRepo it needs to calculate the taken_slots
        """
        pass

    @abstractmethod
    def update_enrollment(self, user_id: str, code: str, new_state: ENROLLMENT_STATE) -> Enrollment:
        """
        If the user is enrolled in the activity, updates the state of enrollment.
        else returns None

        In dynamoRepo, does not need to call update_activity to change taken_slots
        """
        pass

    @abstractmethod
    def get_user(self, user_id:str) -> User:
        """
        If user with the given code exists, returns it
        else returns None
        """
        pass

    @abstractmethod 
    def get_activity_with_enrollments(self, code: str) -> Tuple[Activity, List[Enrollment]]:
        """
        If activity with the given code exists, returns it and the list of enrollments,
        else returns None, None
        """
        pass

    @abstractmethod
    def create_enrollment(self, enrollment:Enrollment) -> Enrollment:
        """
        If enrollment with the given attributes exists, returns it
        else returns None
        """
        pass

    @abstractmethod
    def update_activity(self, code: str, new_title: str = None, new_description: str = None, new_activity_type: ACTIVITY_TYPE = None, new_is_extensive: bool = None,
                 new_delivery_model: DELIVERY_MODEL = None, new_start_date: datetime.datetime = None, new_duration: int = None, new_link: str = None, new_place: str = None,
                 new_responsible_professors: List[User] = None, new_speakers: List[Speaker] = None, new_total_slots: int = None, new_taken_slots: int = None,
                 new_accepting_new_enrollments: bool = None, new_stop_accepting_new_enrollments_before: datetime.datetime = None) -> Activity:
        pass

