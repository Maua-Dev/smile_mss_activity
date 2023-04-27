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

        list_user_id = ["6619c4ba-7807-4a50-98ec-93bb15bd8882", "fd139609-02b1-4ef6-bc25-278ff639a1fc"]
        users = user_repo_cognito.get_users_info(list_user_id)

        assert users[0].user_id == "6619c4ba-7807-4a50-98ec-93bb15bd8882"
        assert users[1].user_id == "fd139609-02b1-4ef6-bc25-278ff639a1fc"

    @pytest.mark.skip("Can't test it locally")
    def test_get_user_info(self):
        user_repo_cognito = UserRepositoryCognito()

        user = user_repo_cognito.get_user_info("5bc1af52-ac75-4d7c-9bd4-b276cd7ff968")

        assert user.user_id == "5bc1af52-ac75-4d7c-9bd4-b276cd7ff968"

    @pytest.mark.skip("Can't test it locally")
    def test_delete_user(self):
        user_repo_cognito = UserRepositoryCognito()

        deleted = user_repo_cognito.delete_user("checkz+in123+2@gmail.com")

        assert deleted == True


