from src.modules.get_all_activities_logged.app.get_all_activities_logged_controller import \
    GetAllActivitiesLoggedController
from src.modules.get_all_activities_logged.app.get_all_activities_logged_usecase import GetAllActivitiesLoggedUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllActivitiesController:
    def test_get_all_activities_logged(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActivitiesLoggedUsecase(repo_activity)
        controller = GetAllActivitiesLoggedController(usecase)

        requester_user = repo_user.users[2]

        request = HttpRequest(headers={
            'requester_user': {"sub": requester_user.user_id, "name": requester_user.name,
                               "custom:role": requester_user.role.value}
        })

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['message'] == "the activities were retrieved to the user"
        assert len(response.body['all_activities_and_user_enrollments']) == len(repo_activity.activities)

    def test_get_all_activities_logged_missing_request_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetAllActivitiesLoggedUsecase(repo_activity)
        controller = GetAllActivitiesLoggedController(usecase)

        request = HttpRequest(headers={
            'invalid_requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name,
                               "custom:role": repo_user.users[0].role.value}
        })

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field requester_user is missing"
