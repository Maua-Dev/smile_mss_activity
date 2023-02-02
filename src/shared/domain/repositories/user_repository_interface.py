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


class IUserRepository(ABC):

    @abstractmethod
    def get_user(self, user_id:str) -> User:
        """
        If user_id with the given code exists, returns it
        else returns None
        """
        pass

    @abstractmethod
    def get_users(self, user_ids: List[str]) -> List[User]:
        """
        If user with the given user_id exists, returns it in a list
        else returns list without the user
        """
        pass

