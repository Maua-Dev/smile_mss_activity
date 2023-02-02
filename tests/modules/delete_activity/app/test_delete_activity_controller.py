import pytest

from src.modules.delete_activity.app.delete_activity_controller import DeleteActivityController
from src.modules.delete_activity.app.delete_activity_usecase import DeleteActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_DeleteActivityController:
    def test_delete_activity_controller(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        activity = repo.activities[11]
        request = HttpRequest(body={"code": repo.activities[11].code, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the activity was deleted"
        assert response.body['activity']['code'] == activity.code
        assert response.body['activity']['title'] == activity.title
        assert response.body['activity']['description'] == activity.description

    def test_delete_activity_controller_missing_code(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is missing'


    def test_delete_activity_controller_no_items_found(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={"code": "CODIGO_INEXISTENTE", 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'No items found for Activity'

    def test_delete_activity_controller_wrong_code_type(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={"code": 1234, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is not valid'

    def test_delete_activity_controller_missing_request_user(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={"code": repo.activities[11].code})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'

    @pytest.mark.skip("Still no ForbiddenAction exception")
    def test_delete_activity_controller_forbidden_not_admin(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        activity = repo.activities[11]
        request = HttpRequest(body={"code": repo.activities[11].code, 'requester_user': {"sub": repo.users[1].user_id,
                                                                                         "cognito:username": repo.users[
                                                                                             1].name,
                                                                                         "custom:role": repo.users[
                                                                                             1].role.value}})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "That action is forbidden for this delete_activity, only admins can delete activities"
