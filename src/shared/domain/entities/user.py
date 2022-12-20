import abc
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class User(abc.ABC):
    name: str
    role: ROLE
    user_id: str
    MIN_NAME_LENGTH = 2

    def __init__(self, name: str, role: ROLE, user_id: str):
        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name

        if type(role) != ROLE:
            raise EntityError("role")
        self.role = role

        if type(user_id) != str:
            raise EntityError("user_id")
        if len(user_id) != 4:
            raise EntityError("user_id")

        self.user_id = user_id

    @staticmethod
    def validate_name(name: str) -> bool:
        if name is None:
            return False
        elif type(name) != str:
            return False
        elif len(name) < User.MIN_NAME_LENGTH:
            return False

        return True
