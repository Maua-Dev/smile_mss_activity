import pytest

from src.modules.delete_activity.app.delete_activity_usecase import DeleteActivityUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="delete_activity")

class Test_DeleteActivityUsecase:
    def test_delete_activity_usecase(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo, observability=observability)
        len_before = len(repo.activities)
        len_enrollments_before = len(repo.enrollments)  
        activity = usecase(code=repo.activities[11].code, user=repo_user.users[0])

        assert type(activity) == Activity
        assert len(repo.activities) == len_before - 1
        assert len(repo.enrollments) == len_enrollments_before - 5


    def test_delete_activity_usecase_no_enrollments(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        repo.activities.pop(7)
        usecase = DeleteActivityUsecase(repo, observability=observability)
        len_before = len(repo.activities)
        activity = usecase(code=repo.activities[1].code, user=repo_user.users[0])

        assert type(activity) == Activity
        assert len(repo.activities) == len_before - 1

    def test_delete_activity_usecase_not_exists(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo, observability=observability)
        with pytest.raises(NoItemsFound):
            activity = usecase(code="CODIGO_INEXISTENTE", user=repo_user.users[0])

    def test_delete_activity_usecase_wrong_code_type(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo, observability=observability)
        with pytest.raises(EntityError):
            activity = usecase(code=123, user=repo_user.users[0])

    def test_delete_activity_usecase_forbidden(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo, observability=observability)
        len_before = len(repo.activities)
        with pytest.raises(ForbiddenAction):
            activity = usecase(code=repo.activities[11].code, user=repo_user.users[1])
    
    def test_delete_activity_usecase_with_enrollments(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DeleteActivityUsecase(repo, observability=observability)
        len_before = len(repo.activities)
        len_enrollments_before = len(repo.enrollments)  
        activity = usecase(code=repo.activities[12].code, user=repo_user.users[0])

        assert type(activity) == Activity
        assert len(repo.activities) == len_before - 1
        assert len(repo.enrollments) == len_enrollments_before - 4

