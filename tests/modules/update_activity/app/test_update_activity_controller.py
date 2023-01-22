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

              request = HttpRequest(body={"code": "CODIGO INEXISTENTE", "new_title": "qualquer titulo",
                                          "new_description": "qualquer descricao", "new_activity_type": "ACADEMIC_COMPETITION",
                                          "is_extensive": True, "delivery_model": "IN_PERSON",
                                          "start_date": "2023-11-22-18T16:52.998305", "duration": 120,
                                          "responsible_professors": repo.users[2], "speakers": repo.speakers[1], "total_slots": 50,
                                          "taken_slots": 10, "accepting_new_enrollments": True, "stop_accepting_new_enrollments_before": "2023-12-22-18T16:52.998305",})

              response = controller(request)

              assert response.status_code == 400
              assert response.body == 'No items found for Activity'