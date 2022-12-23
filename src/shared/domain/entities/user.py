import abc
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class User(abc.ABC):
    name: str
    role: ROLE
    user_id: str
    MIN_NAME_LENGTH = 2
    USER_ID_LENGTH = 4

    def __init__(self, name: str, role: ROLE, user_id: str):
        if not User.validate_name(name):
            raise EntityError("name")
        self.name = name

        if type(role) != ROLE:
            raise EntityError("role")
        self.role = role

        if not User.validate_user_id(user_id):
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

    @staticmethod
    def validate_user_id(user_id: str) -> bool:
        if type(user_id) != str:
            return False
        if len(user_id) != User.USER_ID_LENGTH:
            return False
        return True

    def __repr__(self):
        return f"User(name={self.name}, role={self.role.value}, user_id={self.user_id})"

    def __eq__(self, other):
        return self.name == other.name and self.role == other.role and self.user_id == other.user_id
