from abc import ABC, abstractmethod

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE


class IActivityRepository(ABC):

    @abstractmethod
    def get_enrollment(self, user_id: str, code: str) -> Enrollment:
        """
        If the user is enrolled in the activity, returns the enrollment.
        else returns None
        """
        pass

    @abstractmethod
    def get_activity(self, code:str) -> Activity:
        """
        If activity with the given code exists, returns it
        else returns None
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
    def create_enrollment(self, enrollment:Enrollment) -> Enrollment:
        """
        If enrollment with the given attributes exists, returns it
        else returns None
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