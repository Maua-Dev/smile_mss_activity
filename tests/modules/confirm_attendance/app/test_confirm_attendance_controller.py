from src.modules.confirm_attendance.app.confirm_attendance_controller import ConfirmAttendanceController
from src.modules.confirm_attendance.app.confirm_attendance_usecase import ConfirmAttendanceUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ConfirmAttendanceController:

    def test_confirm_attendance_controller(self):
        repo_user = UserRepositoryMock()
        repo_activity = ActivityRepositoryMock()
        usecase = ConfirmAttendanceUsecase(repo_activity)
        controller = ConfirmAttendanceController(usecase)
        request = HttpRequest(
            body={
                'code': repo_activity.activities[11].code, 
                'requester_user': {
                    "sub": repo_user.users[5].user_id, 
                    "name": repo_user.users[5].name, 
                    "custom:role": repo_user.users[5].role.value}, 
                    'requester_user': {"sub": repo_user.users[5].user_id, 
                    "name": repo_user.users[5].name, 
                    "custom:role": repo_user.users[5].role.value
                    },
                'confirmation_code': repo_activity.activities[11].confirmation_code
                }
            )

        response = controller(request)

        assert response.status_code == 200
        assert response.body == 'Success to Confirm Attendance!'

    def test_confirm_attendance_controller_invalid_activity_code(self):
        repo_user = UserRepositoryMock()
        repo_activity = ActivityRepositoryMock()
        usecase = ConfirmAttendanceUsecase(repo_activity)
        controller = ConfirmAttendanceController(usecase)
        request = HttpRequest(
            body={
                'code': 'invalid_code', 
                'requester_user': {
                    "sub": repo_user.users[5].user_id, 
                    "name": repo_user.users[5].name, 
                    "custom:role": repo_user.users[5].role.value}, 
                    'requester_user': {"sub": repo_user.users[5].user_id, 
                    "name": repo_user.users[5].name, 
                    "custom:role": repo_user.users[5].role.value
                    },
                'confirmation_code': repo_activity.activities[11].confirmation_code
                }
            )

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'Atividade não encontrada'

    def test_confirm_attendance_controller_invalid_confirmation_code(self):
        repo_user = UserRepositoryMock()
        repo_activity = ActivityRepositoryMock()
        usecase = ConfirmAttendanceUsecase(repo_activity)
        controller = ConfirmAttendanceController(usecase)
        request = HttpRequest(
            body={
                'code': repo_activity.activities[11].code, 
                'requester_user': {
                    "sub": repo_user.users[5].user_id, 
                    "name": repo_user.users[5].name, 
                    "custom:role": repo_user.users[5].role.value}, 
                    'requester_user': {"sub": repo_user.users[5].user_id, 
                    "name": repo_user.users[5].name, 
                    "custom:role": repo_user.users[5].role.value
                    },
                'confirmation_code': 'invalid_confirmation_code'
                }
            )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro inválido: Confirmation Code'

    def test_confirm_attendance_controller_invalid_user_id(self):
        repo_user = UserRepositoryMock()
        repo_activity = ActivityRepositoryMock()
        usecase = ConfirmAttendanceUsecase(repo_activity)
        controller = ConfirmAttendanceController(usecase)
        request = HttpRequest(
            body={
                'code': repo_activity.activities[11].code, 
                'requester_user': {
                    "sub": 'invalid_user_id', 
                    "name": repo_user.users[5].name, 
                    "custom:role": repo_user.users[5].role.value}, 
                    'requester_user': {"sub": 'invalid_user_id', 
                    "name": repo_user.users[5].name, 
                    "custom:role": repo_user.users[5].role.value
                    },
                'confirmation_code': repo_activity.activities[11].confirmation_code
                }
            )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro inválido: user_id'
    
    def test_confirm_attendance_controller_already_confirmed(self):
        repo_user = UserRepositoryMock()
        repo_activity = ActivityRepositoryMock()
        usecase = ConfirmAttendanceUsecase(repo_activity)
        controller = ConfirmAttendanceController(usecase)
        request = HttpRequest(
            body={
                'code': repo_activity.activities[12].code, 
                'requester_user': {
                    "sub": repo_user.users[3].user_id, 
                    "name": repo_user.users[3].name, 
                    "custom:role": repo_user.users[3].role.value}, 
                    'requester_user': {"sub": repo_user.users[3].user_id, 
                    "name": repo_user.users[3].name, 
                    "custom:role": repo_user.users[3].role.value
                    },
                'confirmation_code': repo_activity.activities[12].confirmation_code
                }
            )

        response = controller(request)

        assert response.status_code == 403
        assert response.body == 'Presença já confirmada'
