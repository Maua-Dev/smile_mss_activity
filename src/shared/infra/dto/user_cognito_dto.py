from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.role_enum import ROLE


class UserCognitoDTO:
    name: str
    role: ROLE
    user_id: str
    email: str

    def __init__(self, name: str, role: ROLE, user_id: str, email: str = None):
        self.name = name
        self.role = role
        self.user_id = user_id
        self.email = email

    @staticmethod
    def from_cognito(cognito_user: dict):

        custom_prefix = "custom:"
        user_data = {user_attribute["Name"].removeprefix(custom_prefix): user_attribute["Value"] for user_attribute in cognito_user["Attributes"]}

        return UserCognitoDTO(
            name=user_data["name"],
            role=ROLE(user_data["role"]),
            user_id=user_data["sub"],
            email=user_data["email"]
        )

    def to_entity(self):
        return User(
            name=self.name,
            role=self.role,
            user_id=self.user_id
        )

    def to_entity_info(self):
        return UserInfo(
            name=self.name,
            role=self.role,
            user_id=self.user_id,
            email=self.email
        )

    def __eq__(self, other):
        return self.name == other.name and self.role == other.role and self.user_id == other.user_id and self.email == other.email
