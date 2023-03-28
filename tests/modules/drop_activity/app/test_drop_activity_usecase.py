import pytest

from src.modules.drop_activity.app.drop_activity_usecase import DropActivityUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction, UserAlreadyCompleted
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from freezegun import freeze_time


class Test_DropActivityUsecase:

    @freeze_time("2022-12-20")
    def test_drop_activity_usecase_no_queue(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        taken_slots_before = repo_activity.activities[1].taken_slots
        dropped_enrollment = usecase(repo_user.users[1].user_id, repo_activity.activities[1].code)

        assert type(dropped_enrollment) == Enrollment
        assert dropped_enrollment.user_id == repo_user.users[1].user_id
        assert dropped_enrollment.activity_code == repo_activity.activities[1].code
        assert dropped_enrollment.state == ENROLLMENT_STATE.DROPPED
        assert taken_slots_before - 1 == repo_activity.activities[1].taken_slots

        assert repo_activity.enrollments[7].state == ENROLLMENT_STATE.DROPPED

    @freeze_time("2022-12-20")
    def test_drop_activity_usecase_with_queue(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        taken_slots_before = repo_activity.activities[1].taken_slots
        dropped_enrollment = usecase(repo_user.users[2].user_id, repo_activity.activities[0].code)

        assert type(dropped_enrollment) == Enrollment
        assert dropped_enrollment.user_id == repo_user.users[2].user_id
        assert dropped_enrollment.activity_code == repo_activity.activities[0].code
        assert dropped_enrollment.state == ENROLLMENT_STATE.DROPPED
        assert taken_slots_before == repo_activity.activities[1].taken_slots

        assert repo_activity.enrollments[2].state == ENROLLMENT_STATE.DROPPED
        assert repo_activity.enrollments[4].state == ENROLLMENT_STATE.ENROLLED

    @freeze_time("2022-12-20")
    def test_drop_activity_already_in_queue(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        taken_slots_before = repo_activity.activities[1].taken_slots

        dropped_enrollment = usecase(repo_activity.enrollments[4].user_id, repo_activity.enrollments[4].activity_code)

        assert type(dropped_enrollment) == Enrollment
        assert dropped_enrollment.user_id == repo_activity.enrollments[4].user_id
        assert dropped_enrollment.activity_code == repo_activity.enrollments[4].activity_code
        assert dropped_enrollment.state == ENROLLMENT_STATE.DROPPED
        assert taken_slots_before == repo_activity.activities[1].taken_slots

        assert repo_activity.enrollments[4].state == ENROLLMENT_STATE.DROPPED
        assert repo_activity.enrollments[3].state == ENROLLMENT_STATE.ENROLLED
        assert repo_activity.enrollments[5].state == ENROLLMENT_STATE.IN_QUEUE
        assert repo_activity.enrollments[6].state == ENROLLMENT_STATE.IN_QUEUE

    @freeze_time("2022-12-20")
    def test_drop_activity_queue_has_one_already_dropped(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)
        taken_slots_before = repo_activity.activities[11].taken_slots

        dropped_enrollment = usecase(repo_activity.enrollments[23].user_id, repo_activity.enrollments[23].activity_code)

        assert type(dropped_enrollment) == Enrollment
        assert dropped_enrollment.user_id == repo_activity.enrollments[23].user_id
        assert dropped_enrollment.activity_code == repo_activity.enrollments[23].activity_code
        assert dropped_enrollment.state == ENROLLMENT_STATE.DROPPED
        assert taken_slots_before == repo_activity.activities[11].taken_slots

        assert repo_activity.enrollments[23].state == ENROLLMENT_STATE.DROPPED
        assert repo_activity.enrollments[24].state == ENROLLMENT_STATE.ENROLLED
        assert repo_activity.enrollments[25].state == ENROLLMENT_STATE.DROPPED
        assert repo_activity.enrollments[26].state == ENROLLMENT_STATE.ENROLLED
        assert repo_activity.enrollments[27].state == ENROLLMENT_STATE.ENROLLED

    @freeze_time("2022-12-20")
    def test_drop_activity_usecase_already_rejected(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)

        with pytest.raises(ForbiddenAction):
            dropped_enrollment = usecase(repo_activity.enrollments[10].user_id, repo_activity.enrollments[10].activity_code)

    @freeze_time("2022-12-01")
    def test_drop_activity_usecase_already_completed(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)

        with pytest.raises(UserAlreadyCompleted):
            dropped_enrollment = usecase(repo_activity.enrollments[30].user_id, repo_activity.enrollments[30].activity_code)

    @freeze_time("2022-12-20")
    def test_drop_activity_usecase_invalid_user_id(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)

        with pytest.raises(EntityError):
            dropped_enrollment = usecase("0355535e-a110-11ed-a8fc-0242ac1200021", "ELET355")

    @freeze_time("2022-12-20")
    def test_drop_activity_usecase_invalid_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)

        with pytest.raises(EntityError):
            dropped_enrollment = usecase("0355535e-a110-11ed-a8fc-0242ac120002", 123)

    @freeze_time("2022-12-20")
    def test_drop_activity_usecase_no_activity_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)

        with pytest.raises(NoItemsFound):
            dropped_enrollment = usecase("0355535e-a110-11ed-a8fc-0242ac120002", "CODIGO_INEXISTENTE")

    @freeze_time("2022-12-20")
    def test_drop_activity_usecase_no_enrollment_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = DropActivityUsecase(repo_activity, repo_user)

        with pytest.raises(NoItemsFound):
            dropped_enrollment = usecase("0000-0000-00000-000000-0000000-00000", "ELET355")
