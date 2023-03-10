from src.shared.domain.entities.user import User
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

