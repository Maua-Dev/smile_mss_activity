

from src.modules.enroll_activity.app.enroll_activity_controller import EnrollActivityController
from src.modules.enroll_activity.app.enroll_activity_usecase import EnrollActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_EnrollActivityController:

    def test_enroll_activity_controller(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)  

        request = HttpRequest(body={'user_id': repo.enrollments[8].user.user_id, 'code': repo.enrollments[8].activity.code})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the enrollment has been done"
        assert response.body['activity']['code'] == "COD1468"
        assert response.body['user']['user_id'] == "80fb"
        assert response.body['state'] == "ENROLLED"
        assert response.body['activity']['stop_accepting_new_enrollments_before'] == None

    def test_enroll_activity_controller_missing_user_id(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'code': repo.enrollments[8].activity.code})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field user_id is missing'

    def test_enroll_activity_controller_missing_code(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'user_id': repo.enrollments[8].user.user_id})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is missing'


    def test_enroll_activity_controller_forbidden_action(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'user_id': repo.enrollments[2].user.user_id, 'code': repo.enrollments[2].activity.code})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this Enrollment'


    def test_enroll_activity_controller_activity_not_found(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'user_id': repo.enrollments[0].user.user_id, 'code':'CODIGO_INEXISTENTE'})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'No items found for Activity'



    def test_enroll_activity_controller_invalid_user_id(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'user_id' : 'inexistent_user', 'code':repo.enrollments[2].activity.code})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field user_id is not valid'


    def test_enroll_activity_controller_invalid_code(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'user_id':repo.enrollments[2].user.user_id, 'code': 123, })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is not valid'

    
    