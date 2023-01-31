import pytest

from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class Test_User:
    def test_user(self):
        user = User(name="VITOR", role=ROLE.ADMIN, user_id="0355535e-a110-11ed-a8fc-0242ac120002")

        assert type(user) == User
        assert user.name == "VITOR"
        assert user.role == ROLE.ADMIN
        assert user.user_id == "0355535e-a110-11ed-a8fc-0242ac120002"

    def test_user_invalid_name(self):
        with pytest.raises(EntityError):
           user = User(name="V", role=ROLE.ADMIN, user_id="0355535e-a110-11ed-a8fc-0242ac120002")

    def test_user_invalid_role(self):
        with pytest.raises(EntityError):
           user = User(name="VITOR", role="ADMIN", user_id="0355535e-a110-11ed-a8fc-0242ac120002")

    def test_user_invalid_user_id(self):
        with pytest.raises(EntityError):
           user = User(name="VITOR", role=ROLE.ADMIN, user_id="b")

    def test_user_invalid_user_id_int(self):
        with pytest.raises(EntityError):
           user = User(name="VITOR", role=ROLE.ADMIN, user_id=1)

    def test_user_invalid_name_none(self):
        with pytest.raises(EntityError):
           user = User(name=None, role=ROLE.ADMIN, user_id="0355535e-a110-11ed-a8fc-0242ac120002")

    def test_user_invalid_role_none(self):
        with pytest.raises(EntityError):
           user = User(name="VITOR", role=None, user_id="0355535e-a110-11ed-a8fc-0242ac120002")

    def test_user_invalid_user_id_none(self):
        with pytest.raises(EntityError):
           user = User(name="VITOR", role=ROLE.ADMIN, user_id=None)

    def test_user_invalid_name_type(self):
        with pytest.raises(EntityError):
           user = User(name=1, role=ROLE.ADMIN, user_id="0355535e-a110-11ed-a8fc-0242ac120002")

