from abc import ABC, abstractmethod
from typing import List

from src.shared.domain.entities.user import User


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

