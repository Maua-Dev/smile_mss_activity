from abc import ABC, abstractmethod
from typing import List, Tuple

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE


class IActivityRepository(ABC):

    @abstractmethod
    def get_enrollment(self, user_id: str, code: str) -> Enrollment:
        """
        If the user is enrolled in the activity, returns the enrollment.
        else returns None
        """
        pass

    def get_activity(self, code:str) -> Activity:
        """
        If activity with the given code exists, returns it
        else returns None
        """
        pass

    def update_enrollment(self, user_id: str, code: str, state: ENROLLMENT_STATE) -> Enrollment:
        """
        If the user is enrolled in the activity, update the state of enrollment.
        """
        pass

    def get_activity_with_enrollments(self, code: str) -> Tuple[Activity, List[Enrollment]]:
        """
        If activity with the given code exists, returns it and the list of enrollments,
        else returns None, None
        """
        pass
