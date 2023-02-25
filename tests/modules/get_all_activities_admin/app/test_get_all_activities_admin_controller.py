import pytest

from src.modules.get_all_activities_admin.app.get_all_activities_admin_controller import GetAllActivitiesAdminController
from src.modules.get_all_activities_admin.app.get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllActivitiesAdminController:
    def test_get_all_activites_admin_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo_activity, repo_user)
        controller = GetAllActivitiesAdminController(usecase)

        request = HttpRequest(body={'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['message'] == "the activities were retrieved by admin"

    def test_get_all_activites_admin_missing_request_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo_activity, repo_user)
        controller = GetAllActivitiesAdminController(usecase)

        request = HttpRequest(body={'invalid_requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: requester_user"

    def test_get_all_activites_admin_forbidden_not_admin(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo_activity, repo_user)
        controller = GetAllActivitiesAdminController(usecase)

        request = HttpRequest(body={'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}})

        response = controller(request=request)

        assert response.status_code == 403
        assert response.body == "Apenas administradores podem realizar essa ação"
