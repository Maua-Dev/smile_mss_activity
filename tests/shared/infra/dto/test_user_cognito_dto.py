from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.dto.user_cognito_dto import UserCognitoDTO


class Test_UserCognitoDTO:
    def test_from_cognito(self):
        cognito_user = {'Attributes': [{'Name': 'sub',
                                        'Value': "043a048d-1583-4725-bfd8-4661ea42cfbb"},
                                       {'Name': 'email_verified', 'Value': 'true'},
                                       {'Name': 'custom:ra', 'Value': '21014442'},
                                       {'Name': 'name', 'Value': "Bruno Vitor Vilardi Bueno"},
                                       {'Name': 'custom:role', 'Value': 'STUDENT'},
                                       {'Name': 'phone_number', 'Value': '+5511999999999'},
                                       {'Name': 'custom:acceptedNotificSMS', 'Value': 'True'},
                                       {'Name': 'custom:acceptedNotificMail', 'Value': 'True'},
                                       {'Name': 'email', 'Value': 'vgsoller@gmail.com'}],
                        'Enabled': True,
                        'UserStatus': 'UNCONFIRMED',
                        'Username': 'vgsoller@gmail.com'}

        user_dto = UserCognitoDTO.from_cognito(cognito_user=cognito_user)

        expected_user_dto = UserCognitoDTO(
            name="Bruno Vitor Vilardi Bueno",
            role=ROLE.STUDENT,
            user_id="043a048d-1583-4725-bfd8-4661ea42cfbb",
            email="vgsoller@gmail.com",
            phone="+5511999999999",
            accepted_notifications_sms=True,
            accepted_notifications_email=True
        )

        assert user_dto == expected_user_dto

    def test_to_entity(self):
        user_dto = UserCognitoDTO(
            name="Bruno Vitor Vilardi Bueno",
            role=ROLE.STUDENT,
            user_id="043a048d-1583-4725-bfd8-4661ea42cfbb"
        )

        user = user_dto.to_entity()

        expected_user = User(
            name="Bruno Vitor Vilardi Bueno",
            role=ROLE.STUDENT,
            user_id="043a048d-1583-4725-bfd8-4661ea42cfbb"
        )

        assert user == expected_user

    def test_from_cognito_to_entity(self):
        cognito_user = {'Attributes': [{'Name': 'sub',
                                        'Value': "043a048d-1583-4725-bfd8-4661ea42cfbb"},
                                       {'Name': 'email_verified', 'Value': 'true'},
                                       {'Name': 'custom:ra', 'Value': '21014442'},
                                       {'Name': 'name', 'Value': "Bruno Vitor Vilardi Bueno"},
                                       {'Name': 'custom:role', 'Value': 'STUDENT'},
                                       {'Name': 'phone_number', 'Value': '+5511999999999'},
                                       {'Name': 'custom:acceptedNotificSMS', 'Value': 'True'},
                                       {'Name': 'custom:acceptedNotificMail', 'Value': 'True'},
                                       {'Name': 'email', 'Value': 'vgsoller@mail.com'}],
                        'Enabled': True,
                        'UserStatus': 'UNCONFIRMED',
                        'Username': 'vgsoller@gmail.com'}

        user_dto = UserCognitoDTO.from_cognito(cognito_user=cognito_user)

        user = user_dto.to_entity()

        expected_user = User(
            name="Bruno Vitor Vilardi Bueno",
            role=ROLE.STUDENT,
            user_id="043a048d-1583-4725-bfd8-4661ea42cfbb"
        )

        assert user == expected_user

    def test_to_entity_info(self):
        user_dto = UserCognitoDTO(
            name="Bruno Vitor Vilardi Bueno",
            role=ROLE.STUDENT,
            user_id="043a048d-1583-4725-bfd8-4661ea42cfbb",
            email="vgsoller@gmail.com",
            phone="+5511999999999",
            accepted_notifications_sms=True,
            accepted_notifications_email=True)

        user_info = user_dto.to_entity_info()

        expected_user_info = UserInfo(
            name="Bruno Vitor Vilardi Bueno",
            role=ROLE.STUDENT,
            user_id="043a048d-1583-4725-bfd8-4661ea42cfbb",
            email="vgsoller@gmail.com",
            phone="+5511999999999",
            accepted_notifications_sms=True,
            accepted_notifications_email=True,)

        assert user_info == expected_user_info

    def test_from_cognito_to_entity_info(self):
        cognito_user = {'Attributes': [{'Name': 'sub',
                                        'Value': "043a048d-1583-4725-bfd8-4661ea42cfbb"},
                                       {'Name': 'email_verified', 'Value': 'true'},
                                       {'Name': 'custom:ra', 'Value': '21014442'},
                                       {'Name': 'name', 'Value': "Bruno Vitor Vilardi Bueno"},
                                       {'Name': 'custom:role', 'Value': 'STUDENT'},
                                       {'Name': 'phone_number', 'Value': '+5511999999999'},
                                       {'Name': 'custom:acceptedNotificSMS', 'Value': 'True'},
                                       {'Name': 'custom:acceptedNotificMail', 'Value': 'True'},
                                       {'Name': 'email', 'Value': 'vgsoller@gmail.com'}],
                        'Enabled': True,
                        'UserStatus': 'UNCONFIRMED',
                        'Username': 'vgsoller@gmail.com'}

        user_dto = UserCognitoDTO.from_cognito(cognito_user=cognito_user)

        user_info = user_dto.to_entity_info()

        assert type(user_info) == UserInfo

        expected_user_info = UserInfo(
            name="Bruno Vitor Vilardi Bueno",
            role=ROLE.STUDENT,
            user_id="043a048d-1583-4725-bfd8-4661ea42cfbb",
            email="vgsoller@gmail.com",
            phone="+5511999999999",
            accepted_notifications_sms=True,
            accepted_notifications_email=True)

        assert user_info == expected_user_info

    def test_from_cognito_to_entity_info_without_phone(self):

        cognito_user = {'Attributes': [{'Name': 'sub',
                                        'Value': "043a048d-1583-4725-bfd8-4661ea42cfbb"},
                                       {'Name': 'email_verified', 'Value': 'true'},
                                       {'Name': 'custom:ra', 'Value': '21014442'},
                                       {'Name': 'name', 'Value': "Bruno Vitor Vilardi Bueno"},
                                       {'Name': 'custom:role', 'Value': 'STUDENT'},
                                       {'Name': 'custom:acceptedNotificSMS', 'Value': 'True'},
                                       {'Name': 'custom:acceptedNotificMail', 'Value': 'True'},
                                       {'Name': 'email', 'Value': 'vgsoller@gmail.com'}],
                        'Enabled': True,
                        'UserStatus': 'UNCONFIRMED',
                        'Username': 'vgsoller@gmail.com'}

        user_dto = UserCognitoDTO.from_cognito(cognito_user=cognito_user)

        user_info = user_dto.to_entity_info()

        expected_user_info = UserInfo(
            name="Bruno Vitor Vilardi Bueno",
            role=ROLE.STUDENT,
            user_id="043a048d-1583-4725-bfd8-4661ea42cfbb",
            email="vgsoller@gmail.com",
            phone=None,
            accepted_notifications_sms=True,
            accepted_notifications_email=True)

        assert type(user_info) == UserInfo
        assert user_info == expected_user_info

