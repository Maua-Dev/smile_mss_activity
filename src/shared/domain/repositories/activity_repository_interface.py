from abc import ABC, abstractmethod

from src.shared.domain.entities.enrollment import Enrollment


class IActivityRepository(ABC):

    @abstractmethod
    def get_enrollment(self, user_id: str, code: str) -> Enrollment:
        """
        If the user is enrolled in the activity, returns the enrollment.
        else returns None
        """
        pass
