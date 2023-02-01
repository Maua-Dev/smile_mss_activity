from src.modules.get_enrollments_by_user_id.app.get_enrollments_by_user_id_controller import \
    GetEnrollmentsByUserIdController
from src.modules.get_enrollments_by_user_id.app.get_enrollments_by_user_id_usecase import GetEnrollmentsByUserIdUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetEnrollmentsByUserIdController:

    def test_get_enrollments_by_user_id_controller(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentsByUserIdUsecase(repo)
        controller = GetEnrollmentsByUserIdController(usecase)

        response = controller(HttpRequest(query_params={'user_id': repo.users[1].user_id}))

        assert response.status_code == 200

        assert response.body['enrollments'][0]['activity_code'] == repo.enrollments[1].activity_code
        assert response.body['enrollments'][0]['user']['user_id'] == repo.enrollments[1].user.user_id
        assert response.body['enrollments'][0]['state'] == repo.enrollments[1].state.value
        assert response.body['enrollments'][0]['date_subscribed'] == repo.enrollments[1].date_subscribed

    def test_get_enrollments_by_user_id_controller_missing_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentsByUserIdUsecase(repo)
        controller = GetEnrollmentsByUserIdController(usecase)

        response = controller(HttpRequest(query_params={'user_id': None}))

        assert response.status_code == 400
        assert response.body == 'Field user_id is missing'

    def test_get_enrollments_by_user_id_controller_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentsByUserIdUsecase(repo)
        controller = GetEnrollmentsByUserIdController(usecase)

        response = controller(HttpRequest(query_params={'user_id': 'invalid'}))

        assert response.status_code == 400
        assert response.body == 'Field user_id is not valid'
