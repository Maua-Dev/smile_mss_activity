import pytest
from freezegun import freeze_time

from src.modules.enroll_activity.app.enroll_activity_usecase import EnrollActivityUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ClosedActivity, UserAlreadyEnrolled, \
    UserAlreadyCompleted
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="enroll_activity")

class Test_EnrollActivityUsecase:

    @freeze_time("2022-12-01")
    def test_enroll_activity_usecase_accepting_new_enrollments(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)

        taken_slots_old = repo.activities[8].taken_slots
        enrollment_activity = usecase(repo_user.users[6].user_id, repo.activities[8].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user_id == repo_user.users[6].user_id
        assert enrollment_activity.activity_code == repo.activities[8].code
        assert enrollment_activity.state == ENROLLMENT_STATE.ENROLLED
        assert taken_slots_old + 1 == repo.activities[8].taken_slots

    @freeze_time("2022-12-01")
    def test_enroll_activity_usecase_in_queue(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        enrollment_activity = usecase(repo_user.users[8].user_id, repo.activities[0].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user_id == repo_user.users[8].user_id
        assert enrollment_activity.activity_code == repo.activities[0].code
        assert enrollment_activity.state == ENROLLMENT_STATE.IN_QUEUE

    @freeze_time("2022-12-01")
    def test_enroll_activity_usecase_enrolled(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        taken_slots_old = repo.activities[2].taken_slots
        enrollment_activity = usecase(repo_user.users[3].user_id, repo.activities[2].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user_id == repo_user.users[3].user_id
        assert enrollment_activity.activity_code == repo.activities[2].code
        assert repo.activities[2].taken_slots < repo.activities[2].total_slots
        assert repo.activities[2].accepting_new_enrollments == True
        assert taken_slots_old + 1 == repo.activities[2].taken_slots
        assert enrollment_activity.state == ENROLLMENT_STATE.ENROLLED

    @freeze_time("2022-12-01")
    def test_enroll_activity_usecase_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)

        with pytest.raises(EntityError):
            enrollment_activity = usecase('usuario2345', 'code')

    @freeze_time("2022-12-01")
    def test_enroll_activity_usecase_invalid_code(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)

        with pytest.raises(EntityError):
            enrollment_activity = usecase('0355535e-a110-11ed-a8fc-0242ac120002', 852)

    @freeze_time("2022-12-01")
    def test_enroll_activity_usecase_user_already_enrolled(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)

        with pytest.raises(UserAlreadyEnrolled):
            enrollment_activity = usecase('0355535e-a110-11ed-a8fc-0242ac120002', 'ELET355')

    @freeze_time("2022-12-01")
    def test_enroll_activity_usecase_activity_none(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)

        with pytest.raises(NoItemsFound):
            enrollment_activity = usecase(repo_user.users[6].user_id, 'none')

    @freeze_time("2022-12-01")
    def test_enroll_activity_usecase_not_accepting_new_enrollment(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)

        with pytest.raises(ClosedActivity):
            enrollment = usecase(usecase(repo_user.users[5].user_id, repo.activities[12].code))

    @freeze_time("2022-12-01")
    def test_enrollment_activity_usecase_already_completed(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityUsecase(repo, observability=observability)
        repo.activities[12].accepting_new_enrollments = True
        with pytest.raises(UserAlreadyCompleted):
            enrollment_activity = usecase(usecase(repo_user.users[3].user_id, repo.activities[12].code))
