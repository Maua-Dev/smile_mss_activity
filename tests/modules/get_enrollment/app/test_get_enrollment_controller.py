from src.modules.get_enrollment.app.get_enrollment_controller import GetEnrollmentController
from src.modules.get_enrollment.app.get_enrollment_usecase import GetEnrollmentUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetEnrollmentController:
    def test_get_enrollment_controller(self):

        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetEnrollmentUsecase(repo)
        controller = GetEnrollmentController(usecase)
        request = HttpRequest(query_params={'code': repo.enrollments[0].activity_code}, body={'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['activity_code'] == repo.enrollments[0].activity_code
        assert response.body['user']['user_id'] == repo.enrollments[0].user_id
        assert response.body['state'] == repo.enrollments[0].state.value
        assert response.body['date_subscribed'] == repo.enrollments[0].date_subscribed
        assert response.body['message'] == "the enrollment was retrieved"

    def test_get_enrollment_missing_requester_user(self):

            repo = ActivityRepositoryMock()
            repo_user = UserRepositoryMock()
            usecase = GetEnrollmentUsecase(repo)
            controller = GetEnrollmentController(usecase)
            request = HttpRequest(query_params={'code': repo.enrollments[0].activity_code})

            response = controller(request)

            assert response.status_code == 400
            assert response.body == 'Field requester_user is missing'

    def test_get_enrrolment_missing_code(self):

                repo = ActivityRepositoryMock()
                repo_user = UserRepositoryMock()
                usecase = GetEnrollmentUsecase(repo)
                controller = GetEnrollmentController(usecase)
                request = HttpRequest(query_params={}, body={'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

                response = controller(request)

                assert response.status_code == 400
                assert response.body == 'Field code is missing'

    def test_get_enrollment_entity_error(self):

                    repo = ActivityRepositoryMock()
                    repo_user = UserRepositoryMock()
                    usecase = GetEnrollmentUsecase(repo)
                    controller = GetEnrollmentController(usecase)
                    request = HttpRequest(query_params={'code': repo.enrollments[0].activity_code}, body={'requester_user': {"sub": "repo_user.users[0].user_id", "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

                    response = controller(request)

                    assert response.status_code == 400
                    assert response.body == 'Field user_id is not valid'

    def test_get_enrollment_no_items_found_user_not_found(self):

                repo = ActivityRepositoryMock()
                repo_user = UserRepositoryMock()
                usecase = GetEnrollmentUsecase(repo)
                controller = GetEnrollmentController(usecase)
                request = HttpRequest(query_params={'code': 'ECM2345'}, body={'requester_user': {"sub": "0000-0000-00000-000000-0000000-00000", "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

                response = controller(request)

                assert response.status_code == 404
                assert response.body == 'No items found for enrollment'

    def test_get_enrollment_no_items_found_code_not_found(self):

                repo = ActivityRepositoryMock()
                repo_user = UserRepositoryMock()
                usecase = GetEnrollmentUsecase(repo)
                controller = GetEnrollmentController(usecase)
                request = HttpRequest(query_params={'code': 'ECM2341'}, body={'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

                response = controller(request)

                assert response.status_code == 404
                assert response.body == 'No items found for enrollment'

