import pytest
from freezegun import freeze_time

from src.modules.enroll_activity_admin.app.enroll_activity_admin_usecase import EnrollActivityAdminUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import UserAlreadyEnrolled, NoItemsFound, ClosedActivity, \
    UserAlreadyCompleted, UserNotAdmin
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_EnrollActivityAdmin:
    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_usecase_accepting_new_enrollments(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[0]

        taken_slots_old = repo_activity.activities[8].taken_slots
        enrollment_activity = usecase(requester_user, repo_user.users[6].user_id, repo_activity.activities[8].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user_id == repo_user.users[6].user_id
        assert enrollment_activity.activity_code == repo_activity.activities[8].code
        assert enrollment_activity.state == ENROLLMENT_STATE.ENROLLED
        assert taken_slots_old + 1 == repo_activity.activities[8].taken_slots

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_usecase_in_queue(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[0]
        enrollment_activity = usecase(requester_user, repo_user.users[8].user_id, repo_activity.activities[0].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user_id == repo_user.users[8].user_id
        assert enrollment_activity.activity_code == repo_activity.activities[0].code
        assert enrollment_activity.state == ENROLLMENT_STATE.IN_QUEUE

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_usecase_enrolled(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[0]
        taken_slots_old = repo_activity.activities[2].taken_slots
        enrollment_activity = usecase(requester_user, repo_user.users[3].user_id, repo_activity.activities[2].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user_id == repo_user.users[3].user_id
        assert enrollment_activity.activity_code == repo_activity.activities[2].code
        assert repo_activity.activities[2].taken_slots < repo_activity.activities[2].total_slots
        assert repo_activity.activities[2].accepting_new_enrollments == True
        assert taken_slots_old + 1 == repo_activity.activities[2].taken_slots
        assert enrollment_activity.state == ENROLLMENT_STATE.ENROLLED

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_usecase_not_admin(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[1]

        with pytest.raises(UserNotAdmin):
            usecase(requester_user, repo_user.users[6].user_id, repo_activity.activities[8].code)

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_usecase_invalid_user_id(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[0]

        with pytest.raises(EntityError):
            enrollment_activity = usecase(requester_user, 'usuario2345', 'code')

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_usecase_invalid_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[0]

        with pytest.raises(EntityError):
            enrollment_activity = usecase(requester_user, '0355535e-a110-11ed-a8fc-0242ac120002', 852)

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_usecase_user_already_enrolled(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[0]

        with pytest.raises(UserAlreadyEnrolled):
            enrollment_activity = usecase(requester_user, '0355535e-a110-11ed-a8fc-0242ac120002', 'ELET355')

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_usecase_activity_none(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[0]

        with pytest.raises(NoItemsFound):
            enrollment_activity = usecase(requester_user, repo_user.users[6].user_id, 'none')

    @freeze_time("2022-12-01")
    def test_enroll_activity_admin_usecase_not_accepting_new_enrollment(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[0]

        with pytest.raises(ClosedActivity):
            enrollment = usecase(requester_user, repo_user.users[5].user_id, repo_activity.activities[12].code)

    @freeze_time("2022-12-01")
    def test_enrollment_activity_usecase_already_completed(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = EnrollActivityAdminUsecase(repo_activity, repo_user)
        requester_user = repo_user.users[0]
        repo_activity.activities[12].accepting_new_enrollments = True

        with pytest.raises(UserAlreadyCompleted):
            enrollment_activity = usecase(requester_user, repo_user.users[3].user_id, repo_activity.activities[12].code)
