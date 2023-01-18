from src.modules.get_enrollment.app.get_enrollment_controller import GetEnrollmentController
from src.modules.get_enrollment.app.get_enrollment_usecase import GetEnrollmentUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetEnrollmentController:
    def test_get_enrollment_controller(self):

        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentUsecase(repo)
        controller = GetEnrollmentController(usecase)
        request = HttpRequest(query_params={'user_id': repo.enrollments[0].user.user_id, 'code': repo.enrollments[0].activity.code})

        response = controller(request)

        assert response.status_code == 200
        assert response.body['activity']['code'] == repo.enrollments[0].activity.code
        assert response.body['user']['user_id'] == repo.enrollments[0].user.user_id
        assert response.body['state'] == repo.enrollments[0].state.value
        assert response.body['date_subscribed'] == repo.enrollments[0].date_subscribed.isoformat()
        assert response.body['message'] == "the enrollment was retrieved"

    def test_get_enrrolment_missing_user_id(self):

            repo = ActivityRepositoryMock()
            usecase = GetEnrollmentUsecase(repo)
            controller = GetEnrollmentController(usecase)
            request = HttpRequest(query_params={'code': repo.enrollments[0].activity.code})

            response = controller(request)

            assert response.status_code == 400
            assert response.body == 'Field user_id is missing'

    def test_get_enrrolment_missing_code(self):

                repo = ActivityRepositoryMock()
                usecase = GetEnrollmentUsecase(repo)
                controller = GetEnrollmentController(usecase)
                request = HttpRequest(query_params={'user_id': repo.enrollments[0].user.user_id})

                response = controller(request)

                assert response.status_code == 400
                assert response.body == 'Field code is missing'

    def test_get_enrollment_entity_error(self):

                    repo = ActivityRepositoryMock()
                    usecase = GetEnrollmentUsecase(repo)
                    controller = GetEnrollmentController(usecase)
                    request = HttpRequest(query_params={'user_id': 'invalid_user_id', 'code': 'ECM2345'})

                    response = controller(request)

                    assert response.status_code == 400
                    assert response.body == 'Field user_id is not valid'

    def test_get_enrollment_no_items_found_user_not_found(self):

                repo = ActivityRepositoryMock()
                usecase = GetEnrollmentUsecase(repo)
                controller = GetEnrollmentController(usecase)
                request = HttpRequest(query_params={'user_id': 'db41', 'code': 'ECM2345'})

                response = controller(request)

                assert response.status_code == 404
                assert response.body == 'No items found for enrollment'
    def test_get_enrollment_no_items_found_code_not_found(self):

                repo = ActivityRepositoryMock()
                usecase = GetEnrollmentUsecase(repo)
                controller = GetEnrollmentController(usecase)
                request = HttpRequest(query_params={'user_id': 'db43', 'code': 'ECM2341'})

                response = controller(request)

                assert response.status_code == 404
                assert response.body == 'No items found for enrollment'

