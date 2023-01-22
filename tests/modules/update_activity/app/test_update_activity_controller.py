from src.modules.update_activity.app.update_activity_controller import UpdateActivityController
from src.modules.update_activity.app.update_activity_usecase import UpdateActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock

class Test_UpdateActivityController:
       
       def test_update_activity_missing_code(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)
              controller = UpdateActivityController(usecase)

              request = HttpRequest(body={})

              response = controller(request)

              assert response.status_code == 400
              assert response.body == 'Field code is missing'

       def test_update_activity_controller_activity_not_found(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)
              controller = UpdateActivityController(usecase)

              request = HttpRequest(body={"code": "CODIGO INEXISTENTE"})

              response = controller(request)

              assert response.status_code == 404
              assert response.body == 'No items found for Activity'

       def test_update_activity_controller_invalid_code(self):
              repo = ActivityRepositoryMock()
              usecase = UpdateActivityUsecase(repo)
              controller = UpdateActivityController(usecase)

              request = HttpRequest(body={"code": 2456})

              response = controller(request)

              assert response.status_code == 400
              assert response.body == 'Field code is not valid'