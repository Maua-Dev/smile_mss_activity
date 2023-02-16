from src.modules.get_activity_with_enrollments.app.get_activity_with_enrollments_controller import \
    GetActivityWithEnrollmentsController
from src.modules.get_activity_with_enrollments.app.get_activity_with_enrollments_usecase import \
    GetActivityWithEnrollmentsUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
import pytest

class Test_GetActivityWithEnrollmentsController:
    def test_get_activity_with_enrollments_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        controller = GetActivityWithEnrollmentsController(usecase)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[2].user_id, "name": repo_user.users[2].name,
                                     "custom:role": repo_user.users[2].role.value}, 'code': 'ECM2345'})

        response = controller(request=request)
        assert response.body['message'] == 'the activity was retrieved by the professor'
        assert response.status_code == 200

    def test_get_activity_with_enrollments_controller_missing_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        controller = GetActivityWithEnrollmentsController(usecase)

        request = HttpRequest(
            body={'code': 'ECM2345'})

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'

    def test_get_activity_with_enrollments_controller_missing_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        controller = GetActivityWithEnrollmentsController(usecase)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[2].user_id, "name": repo_user.users[2].name,
                                     "custom:role": repo_user.users[2].role.value}})

        response = controller(request=request)
        assert response.status_code == 400
        assert response.body == 'Field code is missing'

    def test_get_activity_with_enrollments_controller_wrong_code_type(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        controller = GetActivityWithEnrollmentsController(usecase)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[2].user_id, "name": repo_user.users[2].name,
                                     "custom:role": repo_user.users[2].role.value}, 'code': 1234})

        response = controller(request=request)
        assert response.body == 'Field code is not valid'
        assert response.status_code == 400

    def test_get_activity_with_enrollments_controller_activity_is_none(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        controller = GetActivityWithEnrollmentsController(usecase)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[2].user_id, "name": repo_user.users[2].name,
                                     "custom:role": repo_user.users[2].role.value}, 'code': 'NÃO_EXISTE'})

        response = controller(request=request)
        assert response.body == 'No items found for activity'
        assert response.status_code == 404

    def test_get_activity_with_enrollments_controller_forbidden_non_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        controller = GetActivityWithEnrollmentsController(usecase)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name,
                                     "custom:role": repo_user.users[1].role.value}, 'code': 'ECM2345'})

        response = controller(request=request)
        assert response.body == 'That action is forbidden for this user: only responsible professors and admin can do that'
        assert response.status_code == 403

    def test_get_activity_with_enrollments_controller_forbidden_wrong_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        controller = GetActivityWithEnrollmentsController(usecase)

        request = HttpRequest(
            body={'requester_user': {"sub": repo_user.users[11].user_id, "name": repo_user.users[11].name,
                                     "custom:role": repo_user.users[11].role.value}, 'code': 'ECM2345'})

        response = controller(request=request)
        assert response.body == 'That action is forbidden for this user'
        assert response.status_code == 403


