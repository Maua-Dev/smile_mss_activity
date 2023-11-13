from src.modules.download_activity.app.download_activity_controller import DownloadActivityController
from src.modules.download_activity.app.download_activity_usecase import DownloadActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="download_activity")

class TestDownloadActivityController:
    def test_download_activity_controller(self):
        repo_activities = ActivityRepositoryMock()
        repo_users = UserRepositoryMock()
        
        usecase = DownloadActivityUsecase(repo_activities, observability=observability)
        controller = DownloadActivityController(usecase, observability=observability)

        requester_user = repo_users.users[13]
        activity_code = repo_activities.activities[0].code

        request = HttpRequest(
            body={"requester_user": {"sub": requester_user.user_id, "custom:role": requester_user.role.value, "name": requester_user.name},
                  "code": activity_code})
        
        response = controller(request)

        assert response.status_code == 200
        assert response.body["message"] == f"Download da atividade '{activity_code}' realizado com sucesso."

    def test_download_activity_controller_with_invalid_code(self):
        repo_activities = ActivityRepositoryMock()
        repo_users = UserRepositoryMock()
        
        usecase = DownloadActivityUsecase(repo_activities, observability=observability)
        controller = DownloadActivityController(usecase, observability=observability)

        requester_user = repo_users.users[13]
        activity_code = "123"

        request = HttpRequest(
            body={"requester_user": {"sub": requester_user.user_id, "custom:role": requester_user.role.value, "name": requester_user.name},
                  "code": activity_code})
        
        response = controller(request)

        assert response.status_code == 404
        assert response.body == "Atividade não encontrada"
    
    def test_download_activity_controller_with_invalid_code(self):
        repo_activities = ActivityRepositoryMock()
        repo_users = UserRepositoryMock()

        usecase = DownloadActivityUsecase(repo_activities, observability=observability)
        controller = DownloadActivityController(usecase, observability=observability)

        requester_user = repo_users.users[1]
        activity_code = repo_activities.activities[0].code

        request = HttpRequest(
            body={"requester_user": {"sub": requester_user.user_id, "custom:role": requester_user.role.value, "name": requester_user.name},
                  "code": activity_code})
        
        response = controller(request)

        assert response.status_code == 404
        assert response.body == "Usuário não tem permissão para baixar essa atividade"


