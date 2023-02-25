import pytest

from src.modules.delete_activity.app.delete_activity_controller import DeleteActivityController
from src.modules.delete_activity.app.delete_activity_usecase import DeleteActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteActivityController:
    def test_delete_activity_controller(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        activity = repo.activities[11]
        request = HttpRequest(body={"code": repo.activities[11].code, 'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the activity was deleted"
        assert response.body['activity']['code'] == activity.code
        assert response.body['activity']['title'] == activity.title
        assert response.body['activity']['description'] == activity.description

    def test_delete_activity_controller_missing_code(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: code'


    def test_delete_activity_controller_no_items_found(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={"code": "CODIGO_INEXISTENTE", 'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'No items found for Activity'

    def test_delete_activity_controller_wrong_code_type(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={"code": 1234, 'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro inválido: code'

    def test_delete_activity_controller_missing_request_user(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={"code": repo.activities[11].code})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: requester_user'

    def test_delete_activity_controller_forbidden_not_admin(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        activity = repo.activities[11]
        request = HttpRequest(body={"code": repo.activities[11].code, 'requester_user': {"sub": repo_user.users[1].user_id,
                                                                                         "name": repo_user.users[
                                                                                             1].name,
                                                                                         "custom:role": repo_user.users[
                                                                                             1].role.value}})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "That action is forbidden for this delete_activity, only admins can delete activities"
