from src.modules.drop_activity.app.drop_activity_controller import DropActivityController
from src.modules.drop_activity.app.drop_activity_usecase import DropActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_DropActivityController:

    def test_drop_activity_controller(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'user_id': repo.enrollments[7].user.user_id, 'code': repo.enrollments[7].activity.code})

        reponse = controller(request)

        assert reponse.status_code == 200
        assert reponse.body['message'] == "the enrollment was dropped"
        assert reponse.body['activity']['code'] == "ELET355"
        assert reponse.body['user']['user_id'] == "b16f"
        assert reponse.body['state'] == "DROPPED"
        assert reponse.body['activity']['stop_accepting_new_enrollments_before'] == None

    def test_drop_activity_controller_missing_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'code': repo.enrollments[7].activity.code})

        reponse = controller(request)

        assert reponse.status_code == 400
        assert reponse.body == 'Field user_id is missing'

    def test_drop_activity_controller_missing_code(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'user_id': repo.enrollments[7].user.user_id})

        reponse = controller(request)

        assert reponse.status_code == 400
        assert reponse.body == 'Field code is missing'

    def test_drop_activity_controller_forbbiden_action(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'user_id': repo.enrollments[8].user.user_id, 'code': repo.enrollments[8].activity.code})

        reponse = controller(request)

        assert reponse.status_code == 400
        assert reponse.body == 'That action is forbidden for this enrollment'

    def test_drop_activity_controller_activity_not_found(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'user_id': repo.enrollments[7].user.user_id, 'code': 'CODIGO_INEXISTENTE'})

        reponse = controller(request)

        assert reponse.status_code == 404
        assert reponse.body == 'No items found for activity'

    def test_drop_activity_controller_no_enrollment_found(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'user_id': '0000', 'code': repo.enrollments[7].activity.code})

        reponse = controller(request)

        assert reponse.status_code == 404
        assert reponse.body == 'No items found for enrollment'

    def test_drop_activity_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'user_id': '1', 'code': repo.enrollments[7].activity.code})
        reponse = controller(request)

        assert reponse.status_code == 400
        assert reponse.body == 'Field user_id is not valid'

    def test_drop_activity_invalid_code(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        controller = DropActivityController(usecase)

        request = HttpRequest(body={'user_id': repo.enrollments[7].user.user_id, 'code': 1})
        reponse = controller(request)

        assert reponse.status_code == 400
        assert reponse.body == 'Field code is not valid'

