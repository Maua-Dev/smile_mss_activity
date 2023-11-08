import pytest

from src.modules.download_activity.app.download_activity_usecase import DownloadActivityUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.usecase_errors import ConflictingInformation, ForbiddenAction, NoItemsFound, UnecessaryUpdate
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="download_activity")

class TestDownloadActivityUsecase:
    def test_download_activity_usecase(self):
        repo = ActivityRepositoryMock()
        repo_users = UserRepositoryMock()
        
        usecase = DownloadActivityUsecase(repo, observability=observability)
        
        requester_user = repo_users.users[13]
        activity_code = repo.activities[0].code
        
        activity = usecase(activity_code, requester_user)
        
        assert activity.code == activity_code
        assert activity.title == "Atividade da ECM 2345"
        assert activity.description == "Isso é uma atividade"
        assert activity.activity_type == ACTIVITY_TYPE.COURSES
        assert activity.is_extensive == False
        assert activity.delivery_model == DELIVERY_MODEL.IN_PERSON
        assert activity.start_date == 1671747413000
        assert activity.end_date == 1671754613000
        assert activity.place == "H332"
        assert activity.responsible_professors == [User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")]
        assert activity.speakers == [Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")]
        assert activity.total_slots == 4
        assert activity.taken_slots == 4
        assert activity.accepting_new_enrollments == True
        assert activity.stop_accepting_new_enrollments_before == 1671743812000
    
    def test_download_activity_usecase_with_invalid_code(self):
        repo = ActivityRepositoryMock()
        repo_users = UserRepositoryMock()
        
        usecase = DownloadActivityUsecase(repo, observability=observability)
        
        requester_user = repo_users.users[13]
        activity_code = "123"
        
        with pytest.raises(NoItemsFound):
            usecase(activity_code, requester_user)
    
    def test_download_activity_usecase_with_invalid_user(self):
        repo = ActivityRepositoryMock()
        repo_users = UserRepositoryMock()
        
        usecase = DownloadActivityUsecase(repo, observability=observability)
        
        requester_user = repo_users.users[1]
        activity_code = repo.activities[0].code
        
        with pytest.raises(ForbiddenAction):
            usecase(activity_code, requester_user)
    
    def test_download_activity_usecase_with_invalid_professor(self):
        repo = ActivityRepositoryMock()
        repo_users = UserRepositoryMock()
        
        usecase = DownloadActivityUsecase(repo, observability=observability)
        
        requester_user = repo_users.users[10]
        activity_code = repo.activities[0].code
        
        with pytest.raises(ForbiddenAction):
            usecase(activity_code, requester_user)



