from src.modules.get_activity_with_enrollments.app.get_activity_with_enrollments_controller import \
    GetActivityWithEnrollmentsController
from src.modules.get_activity_with_enrollments.app.get_activity_with_enrollments_usecase import \
    GetActivityWithEnrollmentsUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
import pytest

observability = ObservabilityMock(module_name="get_activity_with_enrollments")

class Test_GetActivityWithEnrollmentsController:
    def test_get_activity_with_enrollments_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = GetActivityWithEnrollmentsController(usecase, observability=observability)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[2].user_id, "name": repo_user.users[2].name,
                                     "custom:role": repo_user.users[2].role.value}, 'code': 'ECM2345'})

        response = controller(request=request)
        assert response.body['message'] == 'the activity was retrieved by the professor'
        assert response.status_code == 200

    def test_get_activity_with_enrollments_controller_missing_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = GetActivityWithEnrollmentsController(usecase, observability=observability)

        request = HttpRequest(
            body={'code': 'ECM2345'})

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: requester_user'

    def test_get_activity_with_enrollments_controller_missing_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = GetActivityWithEnrollmentsController(usecase, observability=observability)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[2].user_id, "name": repo_user.users[2].name,
                                     "custom:role": repo_user.users[2].role.value}})

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: code'

    def test_get_activity_with_enrollments_controller_wrong_code_type(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = GetActivityWithEnrollmentsController(usecase, observability=observability)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[2].user_id, "name": repo_user.users[2].name,
                                     "custom:role": repo_user.users[2].role.value}, 'code': 1234})

        response = controller(request=request)
        assert response.body == 'Parâmetro inválido: code'
        assert response.status_code == 400

    def test_get_activity_with_enrollments_controller_activity_is_none(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = GetActivityWithEnrollmentsController(usecase, observability=observability)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[2].user_id, "name": repo_user.users[2].name,
                                     "custom:role": repo_user.users[2].role.value}, 'code': 'NÃO_EXISTE'})

        response = controller(request=request)
        assert response.body == 'Atividade não encontrada'
        assert response.status_code == 404

    def test_get_activity_with_enrollments_controller_forbidden_non_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = GetActivityWithEnrollmentsController(usecase, observability=observability)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name,
                                     "custom:role": repo_user.users[1].role.value}, 'code': 'ECM2345'})

        response = controller(request=request)
        assert response.body == 'Apenas professores responsáveis da atividade e administradores podem fazer isso'
        assert response.status_code == 403

    def test_get_activity_with_enrollments_controller_forbidden_wrong_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = GetActivityWithEnrollmentsController(usecase, observability=observability)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[11].user_id, "name": repo_user.users[11].name,
                                     "custom:role": repo_user.users[11].role.value}, 'code': 'ECM2345'})

        response = controller(request=request)
        assert response.body == "Apenas professores responsáveis da atividade e administradores podem fazer isso"
        assert response.status_code == 403


