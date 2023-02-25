from src.modules.get_enrollments_by_user.app.get_enrollments_by_user_controller import \
    GetEnrollmentsByUserController
from src.modules.get_enrollments_by_user.app.get_enrollments_by_user_usecase import GetEnrollmentsByUserUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetEnrollmentsByUserIdController:

    def test_get_enrollments_by_user_controller(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetEnrollmentsByUserUsecase(repo)
        controller = GetEnrollmentsByUserController(usecase)

        response = controller(HttpRequest(query_params={'user_id': repo_user.users[1].user_id}, body={'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}}))

        assert response.status_code == 200

        assert response.body['enrollments'][0]['activity_code'] == repo.enrollments[1].activity_code
        assert response.body['user']['user_id'] == repo.enrollments[1].user_id
        assert response.body['enrollments'][0]['state'] == repo.enrollments[1].state.value
        assert response.body['enrollments'][0]['date_subscribed'] == repo.enrollments[1].date_subscribed

    def test_get_enrollments_by_user_controller_missing_user_id(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetEnrollmentsByUserUsecase(repo)
        controller = GetEnrollmentsByUserController(usecase)

        response = controller(HttpRequest(body={'invalid_requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}}))

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: requester_user'

    def test_get_enrollments_by_user_controller_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetEnrollmentsByUserUsecase(repo)
        controller = GetEnrollmentsByUserController(usecase)

        response = controller(HttpRequest(body={'requester_user': {"sub": "1", "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}}))

        assert response.status_code == 400
        assert response.body == 'Field user_id is not valid'
