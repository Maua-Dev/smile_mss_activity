from src.modules.manual_attendance_change.app.manual_attendance_change_controller import \
    ManualAttendanceChangeController
from src.modules.manual_attendance_change.app.manual_attendance_change_usecase import ManualAttendanceChangeUsecase
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ManualAttendanceChangeController:


    def test_manual_attendance_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 200
        assert repo_activity.enrollments[0].state == ENROLLMENT_STATE.COMPLETED
        assert response.body['message'] == 'the activity was retrieved by the professor'

    def test_manual_attendance_controller_disconfirming(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[29]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.ENROLLED.value, "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 200
        assert repo_activity.enrollments[29].state == ENROLLMENT_STATE.ENROLLED
        assert response.body['message'] == 'the activity was retrieved by the professor'

    def test_manual_attendance_controller_missing_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Par??metro ausente: code'

    def test_manual_attendance_controller_missing_requester_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": enrollment.user_id},
                              headers={

                              })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Par??metro ausente: requester_user'

    def test_manual_attendance_controller_missing_user_id(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.body == 'Par??metro ausente: user_id'



    def test_manual_attendance_controller_missing_new_state(self):
            repo_activity = ActivityRepositoryMock()
            repo_user = UserRepositoryMock()
            usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
            controller = ManualAttendanceChangeController(usecase)

            requester_user = repo_user.users[2]
            enrollment = repo_activity.enrollments[0]

            request = HttpRequest(body={"code": enrollment.activity_code, "user_id": enrollment.user_id},
                                  headers={
                                      'requester_user': {"sub": requester_user.user_id,
                                                         "name": requester_user.name,
                                                         "custom:role": requester_user.role.value}
                                  })

            response = controller(request)

            assert response.status_code == 400
            assert response.body == 'Par??metro ausente: new_state'

    def test_manual_attendance_controller_wrong_enum(self):

        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": 'wrong enum', "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                      "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Par??metro inv??lido: new_state'



    def test_manual_attendance_controller_invalid_activity_code(self):

        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": 1,
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Par??metro inv??lido: activity_code'



    def test_manual_attendance_controller_invalid_user_id(self):

        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": "CODIGO_INVALIDO"},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Par??metro inv??lido: user_id"

    def test_manual_attendance_controller_forbidden_not_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[3]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "Apenas professores respons??veis da atividade e administradores podem gerar c??ddigo de confirma????o para atividade"

    def test_manual_attendance_controller_forbidden_not_professor_of_activity(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[10]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "Apenas professores respons??veis da atividade e administradores podem gerar c??ddigo de confirma????o para atividade"

    def test_manual_attendance_controller_activity_not_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": 'wrong_enrollment',
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'Atividade n??o encontrada'

    def test_manual_attendance_controller_enrollment_not_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": "0"*36},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'Inscri????o n??o encontrada'

    def test_manual_attendance_controller_not_valid_enrollment_status(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[5]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.COMPLETED.value, "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 403
        assert response.body == 'N??o ?? poss??vel confirmar presen??a deste usu??rio'

    def test_manual_attendance_controller_not_completed(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity, repo_user)
        controller = ManualAttendanceChangeController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "new_state": ENROLLMENT_STATE.ENROLLED.value, "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 403
        assert response.body == 'N??o ?? poss??vel cancelar presen??a deste usu??rio'



    





