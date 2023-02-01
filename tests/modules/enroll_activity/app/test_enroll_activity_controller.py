

from src.modules.enroll_activity.app.enroll_activity_controller import EnrollActivityController
from src.modules.enroll_activity.app.enroll_activity_usecase import EnrollActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_EnrollActivityController:

    def test_enroll_activity_controller_enrolled(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)  

        request = HttpRequest(body={'code': repo.enrollments[8].activity_code, 'requester_user': {"sub": repo.users[3].user_id, "cognito:username": repo.users[3].name, "custom:role": repo.users[3].role.value}, 'requester_user': {"sub": repo.users[3].user_id, "cognito:username": repo.users[3].name, "custom:role": repo.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the enrollment was enrolled"
        assert response.body['activity_code'] == "COD1468"
        assert response.body['user']['user_id'] == "0355573c-a110-11ed-a8fc-0242ac120002"
        assert response.body['state'] == "ENROLLED"

    def test_enroll_activity_controller_in_queue(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)  

        request = HttpRequest(body={'code': repo.activities[0].code, 'requester_user': {"sub": repo.users[7].user_id, "cognito:username": repo.users[7].name, "custom:role": repo.users[7].role.value}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == "the enrollment was in queue"
        assert response.body['activity_code'] == repo.activities[0].code
        assert response.body['user']['user_id'] == repo.users[7].user_id
        assert response.body['state'] == "IN_QUEUE"

    def test_enroll_activity_controller_missing_user_id(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'code': repo.enrollments[8].activity_code, 'nao_eh_requester_user': {"sub": repo.users[3].user_id, "cognito:username": repo.users[3].name, "custom:role": repo.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'

    def test_enroll_activity_controller_missing_code(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'requester_user': {"sub": repo.users[3].user_id, "cognito:username": repo.users[3].name, "custom:role": repo.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is missing'

    def test_enroll_activity_controller_enrollment_already_enrolled(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'code': repo.enrollments[7].activity_code, 'requester_user': {"sub": repo.users[1].user_id, "cognito:username": repo.users[1].name, "custom:role": repo.users[1].role.value}})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this Enrollment'

    def test_enroll_activity_controller_forbidden_action_wrong_role(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'code': repo.enrollments[2].activity_code, 'requester_user': {"sub": repo.users[2].user_id, "cognito:username": repo.users[2].name, "custom:role": repo.users[2].role.value}})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this Enrollment'


    def test_enroll_activity_controller_activity_not_found(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'code':'CODIGO_INEXISTENTE', 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'No items found for Activity'

    def test_enroll_activity_controller_user_id_not_found(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'code':repo.enrollments[0].activity_code, 'requester_user': {"sub": "0000-0000-00000-000000-0000000-00000", "cognito:username": repo.users[3].name, "custom:role": repo.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'No items found for User'


    def test_enroll_activity_controller_invalid_user_id(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'code':repo.enrollments[2].activity_code, 'requester_user': {"sub": "1", "cognito:username": repo.users[3].name, "custom:role": repo.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field user_id is not valid'


    def test_enroll_activity_controller_invalid_code(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        controller = EnrollActivityController(usecase)

        request = HttpRequest(body={'code': 123, 'requester_user': {"sub": repo.users[3].user_id, "cognito:username": repo.users[3].name, "custom:role": repo.users[3].role.value}})

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is not valid'

    
