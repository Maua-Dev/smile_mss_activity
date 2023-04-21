from freezegun import freeze_time

from src.modules.enroll_activity.app.enroll_activity_controller import EnrollActivityController
from src.modules.enroll_activity.app.enroll_activity_usecase import EnrollActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="enroll_activity")
 
class Test_EnrollActivityController:

    @freeze_time("2022-12-01")
    def test_enroll_activity_controller_enrolled(self):

        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)  

        request = HttpRequest(body={'code': repo.enrollments[8].activity_code, 'requester_user': {"sub": repo_user.users[3].user_id, "name": repo_user.users[3].name, "custom:role": repo_user.users[3].role.value}, 'requester_user': {"sub": repo_user.users[3].user_id, "name": repo_user.users[3].name, "custom:role": repo_user.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the enrollment was enrolled"
        assert response.body['activity_code'] == "COD1468"
        assert response.body['user']['user_id'] == "0355573c-a110-11ed-a8fc-0242ac120002"
        assert response.body['state'] == "ENROLLED"

    @freeze_time("2022-12-01")
    def test_enroll_activity_controller_in_queue(self):

        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)  

        request = HttpRequest(body={'code': repo.activities[0].code, 'requester_user': {"sub": repo_user.users[7].user_id, "name": repo_user.users[7].name, "custom:role": repo_user.users[7].role.value}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the enrollment was in queue"
        assert response.body['activity_code'] == repo.activities[0].code
        assert response.body['user']['user_id'] == repo_user.users[7].user_id
        assert response.body['state'] == "IN_QUEUE"

    @freeze_time("2022-12-01")
    def test_enroll_activity_controller_missing_user_id(self):

        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)

        request = HttpRequest(body={'code': repo.enrollments[8].activity_code, 'nao_eh_requester_user': {"sub": repo_user.users[3].user_id, "name": repo_user.users[3].name, "custom:role": repo_user.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: requester_user'

    @freeze_time("2022-12-01")
    def test_enroll_activity_controller_missing_code(self):

        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)

        request = HttpRequest(body={'requester_user': {"sub": repo_user.users[3].user_id, "name": repo_user.users[3].name, "custom:role": repo_user.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro ausente: code'

    @freeze_time("2022-12-01")
    def test_enroll_activity_controller_enrollment_already_enrolled(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)

        request = HttpRequest(body={'code': repo.enrollments[7].activity_code, 'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "Usuário já inscrito"

    @freeze_time("2022-12-01")
    def test_enroll_activity_controller_forbidden_action_wrong_role(self):

        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)

        request = HttpRequest(body={'code': repo.enrollments[4].activity_code, 'requester_user': {"sub": repo_user.users[2].user_id, "name": repo_user.users[2].name, "custom:role": repo_user.users[2].role.value}})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "Usuário já inscrito"


    @freeze_time("2022-12-01")
    def test_enroll_activity_controller_activity_not_found(self):

        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)

        request = HttpRequest(body={'code':'CODIGO_INEXISTENTE', 'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'Atividade não encontrada'

    @freeze_time("2022-12-01")
    def test_enroll_activity_controller_invalid_user_id(self):

        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)

        request = HttpRequest(body={'code':repo.enrollments[2].activity_code, 'requester_user': {"sub": "1", "name": repo_user.users[3].name, "custom:role": repo_user.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro inválido: user_id'


    @freeze_time("2022-12-01")
    def test_enroll_activity_controller_invalid_code(self):

        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)

        request = HttpRequest(body={'code': 123, 'requester_user': {"sub": repo_user.users[3].user_id, "name": repo_user.users[3].name, "custom:role": repo_user.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Parâmetro inválido: code'

    @freeze_time("2022-12-01")
    def test_drop_activity_already_completed(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        controller = EnrollActivityController(usecase, observability=observability)
        repo.activities[12].accepting_new_enrollments = True

        request = HttpRequest(body={'code': repo.enrollments[30].activity_code, 'requester_user': {"sub": repo_user.users[3].user_id, "name": repo_user.users[3].name, "custom:role": repo_user.users[3].role.value}, 'requester_user': {"sub": repo_user.users[3].user_id, "name": repo_user.users[3].name, "custom:role": repo_user.users[3].role.value}})

        reponse = controller(request)

        assert reponse.status_code == 403
        assert reponse.body == 'Usuário já completou a atividade'
