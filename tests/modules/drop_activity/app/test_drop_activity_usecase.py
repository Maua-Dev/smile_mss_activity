import pytest

from src.modules.drop_activity.app.drop_activity_usecase import DropActivityUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_DropActivityUsecase:
    def test_drop_activity_usecase_no_queue(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        taken_slots_before = repo.activities[1].taken_slots
        dropped_enrollment = usecase(repo.users[1].user_id,  repo.activities[1].code)

        assert type(dropped_enrollment) == Enrollment
        assert dropped_enrollment.user.user_id == repo.users[1].user_id
        assert dropped_enrollment.activity_code.code == repo.activities[1].code
        assert dropped_enrollment.state == ENROLLMENT_STATE.DROPPED
        assert taken_slots_before - 1 == repo.activities[1].taken_slots

        assert repo.enrollments[7].state == ENROLLMENT_STATE.DROPPED

    def test_drop_activity_usecase_with_queue(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        taken_slots_before = repo.activities[1].taken_slots
        dropped_enrollment = usecase(repo.users[2].user_id, repo.activities[0].code)

        assert type(dropped_enrollment) == Enrollment
        assert dropped_enrollment.user.user_id == repo.users[2].user_id
        assert dropped_enrollment.activity_code.code == repo.activities[0].code
        assert dropped_enrollment.state == ENROLLMENT_STATE.DROPPED
        assert taken_slots_before == repo.activities[1].taken_slots

        assert repo.enrollments[2].state == ENROLLMENT_STATE.DROPPED
        assert repo.enrollments[4].state == ENROLLMENT_STATE.ENROLLED

    def test_drop_activity_already_in_queue(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)
        taken_slots_before = repo.activities[1].taken_slots

        dropped_enrollment = usecase(repo.enrollments[4].user.user_id, repo.enrollments[4].activity_code.code)

        assert type(dropped_enrollment) == Enrollment
        assert dropped_enrollment.user.user_id == repo.enrollments[4].user.user_id
        assert dropped_enrollment.activity_code.code == repo.enrollments[4].activity_code.code
        assert dropped_enrollment.state == ENROLLMENT_STATE.DROPPED
        assert taken_slots_before == repo.activities[1].taken_slots

        assert repo.enrollments[4].state == ENROLLMENT_STATE.DROPPED
        assert repo.enrollments[3].state == ENROLLMENT_STATE.ENROLLED
        assert repo.enrollments[5].state == ENROLLMENT_STATE.IN_QUEUE
        assert repo.enrollments[6].state == ENROLLMENT_STATE.IN_QUEUE

    def test_drop_activity_queue_has_one_already_dropped(self):
            repo = ActivityRepositoryMock()
            usecase = DropActivityUsecase(repo)
            taken_slots_before = repo.activities[11].taken_slots

            dropped_enrollment = usecase(repo.enrollments[23].user.user_id, repo.enrollments[23].activity_code.code)

            assert type(dropped_enrollment) == Enrollment
            assert dropped_enrollment.user.user_id == repo.enrollments[23].user.user_id
            assert dropped_enrollment.activity_code.code == repo.enrollments[23].activity_code.code
            assert dropped_enrollment.state == ENROLLMENT_STATE.DROPPED
            assert taken_slots_before == repo.activities[11].taken_slots

            assert repo.enrollments[23].state == ENROLLMENT_STATE.DROPPED
            assert repo.enrollments[24].state == ENROLLMENT_STATE.ENROLLED
            assert repo.enrollments[25].state == ENROLLMENT_STATE.DROPPED
            assert repo.enrollments[26].state == ENROLLMENT_STATE.ENROLLED
            assert repo.enrollments[27].state == ENROLLMENT_STATE.ENROLLED


    def test_drop_activity_usecase_already_rejected(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)

        with pytest.raises(ForbiddenAction):
            dropped_enrollment = usecase(repo.enrollments[10].user.user_id, repo.enrollments[10].activity_code.code)

    def test_drop_activity_usecase_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)

        with pytest.raises(EntityError):
            dropped_enrollment = usecase("0355535e-a110-11ed-a8fc-0242ac1200021", "ELET355")


    def test_drop_activity_usecase_invalid_code(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)

        with pytest.raises(EntityError):
            dropped_enrollment = usecase("0355535e-a110-11ed-a8fc-0242ac120002", 123)

    def test_drop_activity_usecase_no_activity_found(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)

        with pytest.raises(NoItemsFound):
            dropped_enrollment = usecase("0355535e-a110-11ed-a8fc-0242ac120002", "CODIGO_INEXISTENTE")


    def test_drop_activity_usecase_no_enrollment_found(self):
        repo = ActivityRepositoryMock()
        usecase = DropActivityUsecase(repo)

        with pytest.raises(NoItemsFound):
            dropped_enrollment = usecase("0000-0000-00000-000000-0000000-00000", "ELET355")


