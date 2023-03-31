from freezegun import freeze_time

from src.modules.drop_activity.app.drop_activity_controller import DropActivityController
from src.modules.drop_activity.app.drop_activity_usecase import DropActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_DropActivityController:

    @freeze_time("2022-12-20")
    def test_drop_activity_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'code': repo_activity.enrollments[7].activity_code, 'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}})
        reponse = controller(request)

        assert reponse.status_code == 200
        assert reponse.body['message'] == "the enrollment was dropped"
        assert reponse.body['activity_code'] == "ELET355"
        assert reponse.body['user']['user_id'] == "0355535e-a110-11ed-a8fc-0242ac120002"
        assert reponse.body['state'] == "DROPPED"

    @freeze_time("2022-12-20")
    def test_drop_activity_controller_missing_user_id(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'code': repo_activity.enrollments[7].activity_code})


        reponse = controller(request)

        assert reponse.status_code == 400
        assert reponse.body == 'Parâmetro ausente: requester_user'

    @freeze_time("2022-12-20")
    def test_drop_activity_controller_missing_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}})


        reponse = controller(request)

        assert reponse.status_code == 400
        assert reponse.body == 'Parâmetro ausente: code'

    @freeze_time("2022-12-20")
    def test_drop_activity_controller_forbbiden_action(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'code': repo_activity.enrollments[10].activity_code, 'requester_user': {"sub": repo_user.users[4].user_id, "name": repo_user.users[4].name, "custom:role": repo_user.users[4].role.value}})


        reponse = controller(request)

        assert reponse.status_code == 403
        assert reponse.body == "Impossível desinscrever usuário de atividade que não está inscrito"

    @freeze_time("2022-12-20")
    def test_drop_activity_controller_activity_not_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'code': 'CODIGO_INEXISTENTE', 'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}})


        reponse = controller(request)

        assert reponse.status_code == 404
        assert reponse.body == 'Atividade não encontrada'

    @freeze_time("2022-12-20")
    def test_drop_activity_controller_no_enrollment_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'code': repo_activity.enrollments[7].activity_code, 'requester_user': {"sub": "0000-0000-00000-000000-0000000-00000", "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}})


        reponse = controller(request)

        assert reponse.status_code == 404
        assert reponse.body == 'Inscrição não encontrada'

    @freeze_time("2022-12-20")
    def test_drop_activity_invalid_user_id(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'code': repo_activity.enrollments[7].activity_code, 'requester_user': {"sub": '1', "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}})

        reponse = controller(request)

        assert reponse.status_code == 400
        assert reponse.body == 'Parâmetro inválido: user_id'

    @freeze_time("2022-12-20")
    def test_drop_activity_invalid_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'user_id': repo_activity.enrollments[7].user_id, 'code': 1, 'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}})

        reponse = controller(request)

        assert reponse.status_code == 400
        assert reponse.body == 'Parâmetro inválido: code'

    @freeze_time("2022-12-01")
    def test_drop_activity_already_completed(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'code': repo_activity.enrollments[30].activity_code, 'requester_user': {"sub": repo_user.users[1].user_id, "name": repo_user.users[1].name, "custom:role": repo_user.users[1].role.value}})

        reponse = controller(request)

        assert reponse.status_code == 403
        assert reponse.body == 'Usuário já completou a atividade'
