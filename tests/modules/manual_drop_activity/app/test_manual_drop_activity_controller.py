from src.modules.manual_drop_activity.app.manual_drop_activity_controller import ManualDropActivityController
from src.modules.manual_drop_activity.app.manual_drop_activity_usecase import ManualDropActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ManualDropActivityController:

    def test_manual_drop_activity_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == 'the activity was retrieved by the professor'
    def test_manual_drop_activity_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 200
        assert response.body['message'] == 'the activity was retrieved by the professor'

    def test_manual_drop_activity_missing_code(self):

        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is missing'

    def test_manual_drop_activity_missing_code(self):

        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field user_id is missing'

    def test_manual_drop_activity_controller_missing_requester_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "user_id": enrollment.user_id},
                              headers={}
                              )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field requester_user is missing'

    def test_manual_drop_activity_controller_wrong_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[11]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this user: only responsible professors for this activity can do that'

    def test_manual_drop_activity_controller_wrong_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[1]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this user: only responsible professors can do that'

    def test_manual_drop_activity_controller_wrong_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": 'wrong enrollment',
                                    "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)
        assert response.body == 'No items found for Activity'
        assert response.status_code == 404
    def test_manual_drop_activity_controller_wrong_user_type(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": 1234,
                                    "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)
        assert response.body == 'Field code is not valid'
        assert response.status_code == 400

    def test_manual_drop_activity_controller_wrong_user_id(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[0]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "user_id": "wrong user_id"},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)
        assert response.body == 'Field user_id is not valid'
        assert response.status_code == 400

    def test_manual_drop_activity_controller_already_dropped(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user)
        controller = ManualDropActivityController(usecase)

        requester_user = repo_user.users[2]
        enrollment = repo_activity.enrollments[8]

        request = HttpRequest(body={"code": enrollment.activity_code,
                                    "user_id": enrollment.user_id},
                              headers={
                                  'requester_user': {"sub": requester_user.user_id,
                                                     "name": requester_user.name,
                                                     "custom:role": requester_user.role.value}
                              })

        response = controller(request)

        assert response.status_code == 403
        assert response.body == 'That action is forbidden for this Enrollment'
