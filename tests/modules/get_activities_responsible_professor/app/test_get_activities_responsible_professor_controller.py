from src.modules.get_activities_responsible_professor.app.get_activities_responsible_professor_controller import \
    GetActivitiesResponsibleProfessorController
from src.modules.get_activities_responsible_professor.app.get_activities_responsible_professor_usecase import \
    GetActivitiesResponsibleProfessorUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetActivitiesResponsibleProfessorController:

    def test_get_activities_responsible_professor_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)
        controller = GetActivitiesResponsibleProfessorController(usecase)

        requester_user = repo_user.users[2]

        request = HttpRequest(body={"requester_user": {
            "cognito:username": requester_user.name,
            "sub": requester_user.user_id,
            "custom:role": requester_user.role
        }})

        response = controller(request)

        assert response.status_code == 200
        assert len(response.body["specific_professor_activities_with_enrollments"]) == 9

    def test_get_activities_responsible_professor_controller_no_items(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)
        controller = GetActivitiesResponsibleProfessorController(usecase)

        requester_user = repo_user.users[12]

        request = HttpRequest(body={"requester_user": {
            "cognito:username": requester_user.name,
            "sub": requester_user.user_id,
            "custom:role": requester_user.role
        }})

        response = controller(request)

        assert response.status_code == 200
        assert len(response.body["specific_professor_activities_with_enrollments"]) == 0

    def test_get_activities_responsible_professor_controller_with_invalid_requester_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)
        controller = GetActivitiesResponsibleProfessorController(usecase)

        requester_user = repo_user.users[0]

        request = HttpRequest(body={"requester_user": {
            "cognito:username": requester_user.name,
            "sub": requester_user.user_id,
            "custom:role": requester_user.role
        }})

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "That action is forbidden for this requester_user, only professor can do that"





