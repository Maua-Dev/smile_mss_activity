import pytest

from src.modules.delete_activity.app.delete_activity_usecase import DeleteActivityUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_DeleteActivityUsecase:
    def test_delete_activity_usecase(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        len_before = len(repo.activities)
        activity = usecase(code=repo.activities[11].code)

        assert type(activity) == Activity
        assert len(repo.activities) == len_before - 1
        assert repo.enrollments[23].state == ENROLLMENT_STATE.ACTIVITY_CANCELLED
        assert repo.enrollments[24].state == ENROLLMENT_STATE.ACTIVITY_CANCELLED
        assert repo.enrollments[25].state == ENROLLMENT_STATE.ACTIVITY_CANCELLED
        assert repo.enrollments[26].state == ENROLLMENT_STATE.ACTIVITY_CANCELLED
        assert repo.enrollments[27].state == ENROLLMENT_STATE.ACTIVITY_CANCELLED

    def test_delete_activity_usecase_no_enrollments(self):
        repo = ActivityRepositoryMock()
        repo.activities.pop(7)
        usecase = DeleteActivityUsecase(repo)
        len_before = len(repo.activities)
        activity = usecase(code=repo.activities[1].code)

        assert type(activity) == Activity
        assert len(repo.activities) == len_before - 1

    def test_delete_activity_usecase_not_exists(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        with pytest.raises(NoItemsFound):
            activity = usecase(code="CODIGO_INEXISTENTE")

    def test_delete_activity_usecase_wrong_code_type(self):
        repo = ActivityRepositoryMock()
        usecase = DeleteActivityUsecase(repo)
        with pytest.raises(EntityError):
            activity = usecase(code=123)

