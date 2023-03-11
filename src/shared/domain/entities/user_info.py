import re

from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class UserInfo(User):
    email: str
    def __init__(self, user_id: str, name: str, role: ROLE, email: str):
        super().__init__(name, role, user_id)

        if not UserInfo.validate_email(email):
            raise EntityError("email")
        self.email = email

    def __repr__(self):
        return f"UserInfo(name={self.name}, role={self.role.value}, user_id={self.user_id}, email={self.email})"

    def __eq__(self, other):
        return self.name == other.name and self.role == other.role and self.user_id == other.user_id and self.email == other.email

    @staticmethod
    def validate_email(email) -> bool:
        if email is None:
            return False

        regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        return bool(re.fullmatch(regex, email))
