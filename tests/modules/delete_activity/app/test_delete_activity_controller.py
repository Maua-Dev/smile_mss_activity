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
        request = HttpRequest(body={"code": repo.activities[11].code})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the activity_code was deleted"
        assert response.body['activity_code']['code'] == activity.code
        assert response.body['activity_code']['title'] == activity.title
        assert response.body['activity_code']['description'] == activity.description

    def test_delete_activity_missing_code(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is missing'


    def test_delete_activity_no_items_found(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={"code": "CODIGO_INEXISTENTE"})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'No items found for Activity'

    def test_delete_activity_wrong_code_type(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        controller = DeleteActivityController(usecase)
        request = HttpRequest(body={"code": 1234})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is not valid'




