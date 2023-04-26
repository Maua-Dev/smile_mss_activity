from src.modules.delete_user.app.delete_user_controller import DeleteUserController
from src.modules.delete_user.app.delete_user_usecase import DeleteUserUsecase
from src.shared.domain.entities.user_info import UserInfo
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteUserController:
    def test_delete_user_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        usecase = DeleteUserUsecase(repo_activity, repo_user)
        controller = DeleteUserController(usecase)

        len_before = len(repo_user.users)
        requester_user = repo_user.users[13]

        request = HttpRequest(
            body={"requester_user": {"sub": requester_user.user_id, "custom:role": requester_user.role.value, "name": requester_user.name}})

        response = controller(request)

        assert len_before == len(repo_user.users) + 1

    def test_delete_user_controller_enrolled(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        usecase = DeleteUserUsecase(repo_activity, repo_user)
        controller = DeleteUserController(usecase)

        len_before = len(repo_user.users)
        requester_user = repo_user.users[1]

        request = HttpRequest(
            body={"requester_user": {"sub": requester_user.user_id, "custom:role": requester_user.role.value,
                                     "name": requester_user.name}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "Usuário '0355535e-a110-11ed-a8fc-0242ac120002' deletado com sucesso."

