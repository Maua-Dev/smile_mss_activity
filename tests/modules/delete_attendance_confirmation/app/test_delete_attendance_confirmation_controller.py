from src.modules.delete_attendance_confirmation.app.delete_attendance_confirmation_controller import DeleteAttendanceConfirmationController
from src.modules.delete_attendance_confirmation.app.delete_attendance_confirmation_usecase import DeleteAttendanceConfirmationUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DeleteAttendanceConfirmationController:
       def test_delete_attendance_confirmation_controller(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo)
              controller = DeleteAttendanceConfirmationController(usecase)

              requester_user = repo_user.users[2]
              request = HttpRequest(body={"code": repo.activities[11].code}, headers={'requester_user': {"sub": requester_user.user_id, "name": requester_user.name, "custom:role": requester_user.role.value}})
              response = controller(request)

              assert response.status_code == 200
              assert response.body == {
                     "activity_code": repo.activities[11].code,
                     "confirmation_code": repo.activities[11].confirmation_code,
                     "message": "The confirmation code for the activity was deleted"
              }

       def test_delete_attendance_confirmation_controller_missing_code(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo)
              controller = DeleteAttendanceConfirmationController(usecase)

              requester_user = repo_user.users[2]
              request = HttpRequest(body={}, headers={'requester_user': {"sub": requester_user.user_id, "name": requester_user.name, "custom:role": requester_user.role.value}})
              response = controller(request)

              assert response.status_code == 400
              assert response.body == "Parâmetro ausente: code"

       def test_delete_attendance_confirmation_controller_missing_requester_user(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo)
              controller = DeleteAttendanceConfirmationController(usecase)

              requester_user = repo_user.users[2]
              request = HttpRequest(body={"code": repo.activities[11].code}, headers={})
              response = controller(request)

              assert response.status_code == 400
              assert response.body == "Parâmetro ausente: requester_user"

       def test_delete_attendance_confirmation_controller_invalid_activity_code(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo)
              controller = DeleteAttendanceConfirmationController(usecase)

              requester_user = repo_user.users[2]
              request = HttpRequest(body={"code": 1}, headers={'requester_user': {"sub": requester_user.user_id, "name": requester_user.name, "custom:role": requester_user.role.value}})
              response = controller(request)

              assert response.status_code == 400
              assert response.body == "Field activity_code is not valid"

       def test_delete_attendance_confirmation_controller_activity_not_found(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo)
              controller = DeleteAttendanceConfirmationController(usecase)

              requester_user = repo_user.users[2]
              request = HttpRequest(body={"code": "QUALQUER CODIGO"}, headers={'requester_user': {"sub": requester_user.user_id, "name": requester_user.name, "custom:role": requester_user.role.value}})
              response = controller(request)

              assert response.status_code == 404
              assert response.body == "No items found for activity"

       def test_delete_attendance_confirmation_controller_role_not_professor(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo)
              controller = DeleteAttendanceConfirmationController(usecase)

              requester_user = repo_user.users[0]
              request = HttpRequest(body={"code": repo.activities[11].code}, headers={'requester_user': {"sub": requester_user.user_id, "name": requester_user.name, "custom:role": requester_user.role.value}})
              response = controller(request)

              assert response.status_code == 403
              assert response.body == "That action is forbidden for this user, not professor"

       def test_delete_attendance_confirmation_controller_activity_dont_have_confirmation_code(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo)
              controller = DeleteAttendanceConfirmationController(usecase)

              requester_user = repo_user.users[2]
              request = HttpRequest(body={"code": repo.activities[0].code}, headers={'requester_user': {"sub": requester_user.user_id, "name": requester_user.name, "custom:role": requester_user.role.value}})
              response = controller(request)

              assert response.status_code == 403
              assert response.body == "That action is forbidden for this confirmation_code, do not exists"

       def test_delete_attendance_confirmation_controller_role_not_professor(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo)
              controller = DeleteAttendanceConfirmationController(usecase)

              requester_user = repo_user.users[10]
              request = HttpRequest(body={"code": repo.activities[11].code}, headers={'requester_user': {"sub": requester_user.user_id, "name": requester_user.name, "custom:role": requester_user.role.value}})
              response = controller(request)

              assert response.status_code == 403
              assert response.body == "That action is forbidden for this user, not professor of activity"
