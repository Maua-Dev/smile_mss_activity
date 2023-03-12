import pytest

from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.user_repository_cognito import UserRepositoryCognito

class Test_UserRepositoryCognito:
    @pytest.mark.skip("Can't test it locally")
    def test_get_user(self):
        user_repo_dynamo = UserRepositoryCognito()
        expected_user = User(
            user_id="c5a416c6-1662-46a8-8a70-68fa5897eba5",
            name="Vitor Guirão",
            role=ROLE.PROFESSOR,
        )
        user = user_repo_dynamo.get_user("c5a416c6-1662-46a8-8a70-68fa5897eba5")

        assert user == expected_user

    @pytest.mark.skip("Can't test it locally")
    def test_get_users(self):
        user_repo_dynamo = UserRepositoryCognito()
        expected_users = [
            User(
                user_id="c5a416c6-1662-46a8-8a70-68fa5897eba5",
                name="Vitor Guirão",
                role=ROLE.PROFESSOR,
            ),
            User(
                user_id="0d6738dc-b612-4dd6-99d1-1b6414d23d2f",
                name="Bruninho",
                role=ROLE.PROFESSOR,
            ),
        ]
        expected_users.sort(key=lambda x: x.user_id)

        list_user_id = [expected_users[0].user_id, expected_users[1].user_id]
        users = user_repo_dynamo.get_users(list_user_id)

        users.sort(key=lambda x: x.user_id)

        assert users == expected_users


    @pytest.mark.skip("Can't test it locally")
    def test_get_users_user_not_found(self):
        user_repo_dynamo = UserRepositoryCognito()
        expected_users = [
            User(
                user_id="c5a416c6-1662-46a8-8a70-68fa5897eba5",
                name="Vitor Guirão",
                role=ROLE.PROFESSOR,
            ),
        ]
        expected_users.sort(key=lambda x: x.user_id)

        list_user_id = [expected_users[0].user_id, "0d6738dc-b612-4dd6-88d1-1b6414d23d2f"]
        users = user_repo_dynamo.get_users(list_user_id)

        users.sort(key=lambda x: x.user_id)

        assert users == expected_users

    @pytest.mark.skip("Can't test it locally")
    def test_get_users_info(self):
        user_repo_cognito = UserRepositoryCognito()
        expected_users = [
            UserInfo(
                user_id="aaa404d9-6ee9-48df-8c65-760777b94992",
                name="Brenudo Brenas",
                role=ROLE.STUDENT,
                email="bamorim.devmaua@gmail.com",
                phone=None,
                accepted_notifications_email=False,
                accepted_notifications_sms=False,
            ),
            UserInfo(
                user_id="30655fce-c069-4751-ab22-ec0ba92a6273",
                name="Carol Mota",
                role=ROLE.PROFESSOR,
                email="carol@mailna.co",
                phone="+5511991758098",
                accepted_notifications_email=True,
                accepted_notifications_sms=True,
            ),
        ]
        expected_users.sort(key=lambda x: x.user_id)

        list_user_id = ["aaa404d9-6ee9-48df-8c65-760777b94992", "30655fce-c069-4751-ab22-ec0ba92a6273"]
        users = user_repo_cognito.get_users_info(list_user_id)

        users.sort(key=lambda x: x.user_id)

        assert users == expected_users
