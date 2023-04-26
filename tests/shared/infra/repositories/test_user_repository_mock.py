from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_UserRepositoryMock:

    def test_get_user(self):
        repo = UserRepositoryMock()
        user = repo.get_user('d61dbf66-a10f-11ed-a8fc-0242ac120002')
        assert type(user) == User

    def test_get_user_not_exists(self):
        repo = UserRepositoryMock()
        user = repo.get_user('NAO-EXISTE')
        assert user is None


    def test_get_users(self):
        repo = UserRepositoryMock()
        users = repo.get_users(["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"])
        assert type(users) == list
        assert all(type(user) == User for user in users)
        assert len(users) == 2

    def test_get_users_not_found(self):
        repo = UserRepositoryMock()
        users = repo.get_users(["000", "03555624-a110-11ed-a8fc-0242ac120002"])
        assert type(users) == list
        assert all(type(user) == User for user in users)
        assert len(users) == 1

    def test_get_users_info(self):
        repo = UserRepositoryMock()
        users = repo.get_users_info(["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"])
        assert type(users) == list
        assert all(type(user) == UserInfo for user in users)
        assert len(users) == 2

    def test_get_user_info(self):
        repo = UserRepositoryMock()
        user = repo.get_user_info("62cafdd4-a110-11ed-a8fc-0242ac120002")
        assert type(user) == UserInfo
        assert user.user_id == "62cafdd4-a110-11ed-a8fc-0242ac120002"
        assert user.name == "Rafael Santos"
        assert user.email == "teste@teste.com"
        assert user.phone == "+5511999999999"

    def test_get_user_info_not_found(self):
        repo = UserRepositoryMock()
        user = repo.get_user_info("000")
        assert user is None

    def test_delete_user(self):
        repo = UserRepositoryMock()
        len_before = len(repo.users)
        is_deleted = repo.delete_user("teste@teste.com")

        assert is_deleted is True
        assert len(repo.users) == len_before - 1
