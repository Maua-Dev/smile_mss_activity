import re

from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class UserInfo(User):
    email: str
    phone: str
    accepted_notifications_sms: bool
    accepted_notifications_email: bool
    social_name: str
    certificate_with_social_name: bool

    def __init__(self, user_id: str, name: str, role: ROLE, email: str, phone: str, accepted_notifications_sms: bool, accepted_notifications_email: bool, social_name: str, certificate_with_social_name: bool):
        super().__init__(name, role, user_id)

        if not UserInfo.validate_email(email):
            raise EntityError("email")
        self.email = email

        if not UserInfo.validate_phone(phone) and phone is not None:
            raise EntityError("phone")
        self.phone = phone

        if type(accepted_notifications_sms) != bool:
            raise EntityError("accepted_notifications_sms")
        self.accepted_notifications_sms = accepted_notifications_sms

        if type(accepted_notifications_email) != bool:
            raise EntityError("accepted_notifications_email")
        self.accepted_notifications_email = accepted_notifications_email

        if social_name is not None:
            if not User.validate_name(social_name):
                raise EntityError("social_name")
            self.social_name = social_name.title()
        else:
            self.social_name = None

        if type(certificate_with_social_name) != bool:
            raise EntityError("certificate_with_social_name")
        self.certificate_with_social_name = certificate_with_social_name

    def __repr__(self):
        return f"UserInfo(name={self.name}, role={self.role.value}, user_id={self.user_id}, email={self.email})"

    def __eq__(self, other):
        return self.name == other.name and self.role == other.role and self.user_id == other.user_id and self.email == other.email and self.phone == other.phone and self.accepted_notifications_sms == other.accepted_notifications_sms and self.accepted_notifications_email == other.accepted_notifications_email

    @staticmethod
    def validate_email(email) -> bool:
        if email is None:
            return False

        regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

        return bool(re.fullmatch(regex, email))

    @staticmethod
    def validate_phone(phone: str) -> bool:
        if type(phone) != str:
            return False
        elif phone[0] != "+":
            return False
        elif phone[1:].isdecimal() is False:
            return False

        return True
