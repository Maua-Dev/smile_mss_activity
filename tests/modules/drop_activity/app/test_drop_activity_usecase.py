import pytest

from src.modules.drop_activity.app.drop_activity_usecase import DropActivityUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_DropActivityUsecase:
    def test_drop_activity_usecase_no_queue(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        taken_slots_before = repo.activities[1].taken_slots
        dropped_enrollment = usecase("b16f", "ELET355")

        assert type(dropped_enrollment) == Enrollment
        assert repo.enrollments[7].state == ENROLLMENT_STATE.DROPPED
        assert taken_slots_before - 1 == repo.activities[1].taken_slots

    def test_drop_activity_usecase_with_queue(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        taken_slots_before = repo.activities[1].taken_slots
        dropped_enrollment = usecase("d7f1", "ECM2345")

        assert type(dropped_enrollment) == Enrollment
        assert repo.enrollments[2].state == ENROLLMENT_STATE.DROPPED
        assert repo.enrollments[4].state == ENROLLMENT_STATE.ENROLLED
        assert  taken_slots_before == repo.activities[1].taken_slots

    def test_drop_activity_usecase_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)

        with pytest.raises(EntityError):
            dropped_enrollment = usecase("b16f1", "ELET355")


    def test_drop_activity_usecase_invalid_code(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)

        with pytest.raises(EntityError):
            dropped_enrollment = usecase("b16f", 123)

    def test_drop_activity_usecase_no_activity_found(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)

        with pytest.raises(NoItemsFound):
            dropped_enrollment = usecase("b16f", "CODIGO_INEXISTENTE")


    def test_drop_activity_usecase_no_enrollment_found(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)

        with pytest.raises(NoItemsFound):
            dropped_enrollment = usecase("0000", "ELET355")
