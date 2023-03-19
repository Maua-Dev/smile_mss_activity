from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.role_enum import ROLE


class UserCognitoDTO:
    name: str
    role: ROLE
    user_id: str
    email: str
    phone: str
    accepted_notifications_sms: bool
    accepted_notifications_email: bool
    social_name: str
    certificate_with_social_name: bool

    def __init__(self, name: str, role: ROLE, user_id: str, email: str = None, phone: str = None, accepted_notifications_sms: bool = None, accepted_notifications_email: bool = None, social_name: str = None, certificate_with_social_name: bool = None):
        self.name = name
        self.role = role
        self.user_id = user_id
        self.email = email
        self.phone = phone
        self.accepted_notifications_sms = accepted_notifications_sms
        self.accepted_notifications_email = accepted_notifications_email
        self.social_name = social_name
        self.certificate_with_social_name = certificate_with_social_name

    @staticmethod
    def from_cognito(cognito_user: dict):

        custom_prefix = "custom:"
        user_data = {user_attribute["Name"].removeprefix(custom_prefix): user_attribute["Value"] for user_attribute in cognito_user["Attributes"]}

        return UserCognitoDTO(
            name=user_data["name"],
            role=ROLE(user_data["role"]),
            user_id=user_data["sub"],
            email=user_data["email"],
            phone=user_data.get("phone_number"),
            accepted_notifications_sms=eval(user_data["acceptedNotificSMS"].title()),
            accepted_notifications_email=eval(user_data["acceptedNotificMail"].title()),
            social_name=user_data.get("socialName"),
            certificate_with_social_name=eval(user_data["certWithSocialName"].title())
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
            email=self.email,
            phone=self.phone,
            accepted_notifications_sms=self.accepted_notifications_sms,
            accepted_notifications_email=self.accepted_notifications_email,
            social_name=self.social_name,
            certificate_with_social_name=self.certificate_with_social_name
        )

    def __eq__(self, other):
        return self.name == other.name and self.role == other.role and self.user_id == other.user_id and self.email == other.email
