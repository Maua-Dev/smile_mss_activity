from freezegun import freeze_time

from src.modules.enroll_activity.app.enroll_activity_controller import EnrollActivityController
from src.modules.enroll_activity.app.enroll_activity_usecase import EnrollActivityUsecase
from src.modules.enroll_activity_admin.app.enroll_activity_admin_controller import EnrollActivityAdminController
from src.modules.enroll_activity_admin.app.enroll_activity_admin_usecase import EnrollActivityAdminUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="enroll_activity_admin")

class Test_EnrollActivityAdminController:

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_enrolled(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)

        requester_user = repo_user.users[0]

        request = HttpRequest(body={'code': repo.enrollments[8].activity_code,
                                    'user_id': repo_user.users[3].user_id,
                                    'requester_user': {"sub":  requester_user.user_id,
                                                       "name":  requester_user.name,
                                                       "custom:role":  requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the enrollment was enrolled"
        assert response.body['activity_code'] == "COD1468"
        assert response.body['user']['user_id'] == repo_user.users[3].user_id
        assert response.body['state'] == "ENROLLED"

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_not_admin(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)

        requester_user = repo_user.users[1]

        request = HttpRequest(body={'code': repo.enrollments[8].activity_code,
                                    'user_id': repo_user.users[3].user_id,
                                    'requester_user': {"sub":  requester_user.user_id,
                                                       "name":  requester_user.name,
                                                       "custom:role":  requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "Usuário não é administrador"

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_in_queue(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]

        request = HttpRequest(body={'code': repo.activities[0].code,
                                    'user_id': repo_user.users[7].user_id,
                                    'requester_user': {"sub": requester_user.user_id,
                                                       "name": requester_user.name,
                                                       "custom:role": requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the enrollment was in queue"
        assert response.body['activity_code'] == repo.activities[0].code
        assert response.body['user']['user_id'] == repo_user.users[7].user_id
        assert response.body['state'] == "IN_QUEUE"

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_missing_user_id(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]

        request = HttpRequest(body={'code': repo.enrollments[8].activity_code,
                                    "user_id": repo_user.users[3].user_id,
                                    'nao_eh_requester_user': {"sub": requester_user.user_id,
                                                              "name": requester_user.name,
                                                              "custom:role": requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: requester_user'

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_missing_user_id(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]

        request = HttpRequest(body={'code': repo.enrollments[8].activity_code,
                                    'requester_user': {"sub": requester_user.user_id,
                                                       "name": requester_user.name,
                                                       "custom:role": requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: user_id'

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_missing_code(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]

        request = HttpRequest(body={
            "user_id": repo_user.users[3].user_id,
            'requester_user': {"sub": requester_user.user_id, "name": requester_user.name,
                               "custom:role": requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: code'

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_enrollment_already_enrolled(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]

        request = HttpRequest(body={'code': repo.enrollments[7].activity_code,
                                    'user_id': repo_user.users[1].user_id,
                                    "user_id": '0355535e-a110-11ed-a8fc-0242ac120002',
                                    'requester_user': {"sub": requester_user.user_id,
                                                       "name": requester_user.name,
                                                       "custom:role": requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "Usuário já inscrito"

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_forbidden_action_wrong_role(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]

        request = HttpRequest(body={'code': repo.enrollments[4].activity_code,
                                    'user_id': repo_user.users[2].user_id,
                                    'requester_user': {"sub": requester_user.user_id,
                                                       "name": requester_user.name,
                                                       "custom:role": requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "Usuário já inscrito"

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_activity_not_found(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]

        request = HttpRequest(body={'code': 'ATIVIDADE_INEXISTENTE',
                                    "user_id": repo_user.users[0].user_id,
                                    'requester_user': {"sub": requester_user.user_id,
                                                         "name": requester_user.name,
                                                            "custom:role": requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'Atividade não encontrada'

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]

        request = HttpRequest(body={'code': repo.enrollments[2].activity_code,
                                    'user_id': 'user_id_invalido',
                                    'requester_user': {"sub": requester_user, "name": requester_user.name,
                                                       "custom:role": requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro inválido: user_id'

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_controller_invalid_code(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]

        request = HttpRequest(body={'code': 123,
                                    'user_id': repo_user.users[3].user_id,
                                    'requester_user': {"sub": requester_user.user_id,
                                                                    "name": requester_user.name,
                                                                    "custom:role": requester_user.role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro inválido: code'

    @freeze_time("2022-12-01")
    def test_drop_activity_already_completed(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo, repo_user, observability=observability)
        controller = EnrollActivityAdminController(usecase, observability=observability)
        requester_user = repo_user.users[0]
        repo.activities[12].accepting_new_enrollments = True

        request = HttpRequest(body={'code': repo.enrollments[30].activity_code,
                                    'user_id': repo.enrollments[30].user_id,
                                    'requester_user': {"sub": requester_user.user_id,
                                                       "name": requester_user.name,
                                                       "custom:role": requester_user.role.value}})

        reponse = controller(request)

        assert reponse.status_code == 403
        assert reponse.body == 'Usuário já completou a atividade'
