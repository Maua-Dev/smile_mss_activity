from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE


class UserApiGatewayDTO:
    name: str
    role: ROLE
    user_id: str

    def __init__(self, name: str, role: ROLE, user_id: str):
        self.name = name
        self.role = role
        self.user_id = user_id

    @staticmethod
    def from_api_gateway(user_data: dict) -> 'UserApiGatewayDTO':
        """
        This method is used to convert the user data from the API Gateway to a UserApiGatewayDTO object.
        """

        return UserApiGatewayDTO(
            name=user_data['name'],
            role=ROLE(user_data['custom:role']),
            user_id=user_data['sub']
        )

    def to_entity(self) -> User:
        """
        This method is used to convert the UserApiGatewayDTO object to a User entity.
        """
        return User(
            name=self.name,
            role=self.role,
            user_id=self.user_id
        )

    def __eq__(self, other):
        return self.name == other.name and self.role == other.role and self.user_id == other.user_id

