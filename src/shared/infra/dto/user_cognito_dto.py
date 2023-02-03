from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE


class UserCognitoDTO:
    name: str
    role: ROLE
    user_id: str

    def __init__(self, name: str, role: ROLE, user_id: str):
        self.name = name
        self.role = role
        self.user_id = user_id

    @staticmethod
    def from_cognito(cognito_user: dict):

        user_data = {user_attribute["Name"]: user_attribute["Value"] for user_attribute in cognito_user["UserAttributes"]}

        return UserCognitoDTO(
            name=user_data["name"],
            role=ROLE(user_data["role"]),
            user_id=user_data["sub"]
        )

    def to_entity(self):
        return User(
            name=self.name,
            role=self.role,
            user_id=self.user_id
        )

    def __eq__(self, other):
        return self.name == other.name and self.role == other.role and self.user_id == other.user_id
