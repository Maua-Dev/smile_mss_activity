from src.modules.get_all_activities.app.get_all_activities_controller import GetAllActivitiesController
from src.modules.get_all_activities.app.get_all_activities_usecase import GetAllActivitiesUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetAllActivitiesController:
    def test_get_all_activites_controller(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesUsecase(repo)
        controller = GetAllActivitiesController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['message'] == "the activities were retrieved"
