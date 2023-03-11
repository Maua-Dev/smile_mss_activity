import pytest

from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class Test_UserInfo:
    def test_user_info(self):
        user_info = UserInfo(
            user_id="a" * 36,
            name="test",
            role=ROLE.EXTERNAL,
            email="21.01444-2@maua.br")

        assert user_info.user_id == "a" * 36
        assert user_info.name == "test"
        assert user_info.role == ROLE.EXTERNAL
        assert user_info.email == "21.01444-2@maua.br"

    def test_user_info_invalid_email(self):

        with pytest.raises(EntityError):
            user_info = UserInfo(
                user_id="a" * 36,
                name="test",
                role=ROLE.EXTERNAL,
                email="21.01444-2maua.br")

