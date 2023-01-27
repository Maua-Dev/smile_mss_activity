from src.modules.get_all_activities_admin.app.get_all_activities_admin_controller import GetAllActivitiesAdminController
from src.modules.get_all_activities_admin.app.get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetAllActivitiesAdminController:
    def test_get_all_activites_controller(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo)
        controller = GetAllActivitiesAdminController(usecase)

        request = HttpRequest(query_params={})

        response = controller(request=request)

        assert response.status_code == 200
        assert response.body['message'] == "the activities were retrieved by admin"

