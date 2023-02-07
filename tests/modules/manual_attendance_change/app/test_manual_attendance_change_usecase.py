from src.modules.manual_attendance_change.app.manual_attendance_change_usecase import ManualAttendanceChangeUsecase
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ManualAttendanceChangeUsecase:

    def test_manual_attendance_change_usecase(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0] #old one
        requester_user = repo_user.users[2]

        new_enrollment = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                 user_id=enrollment.user_id,
                                 new_state=ENROLLMENT_STATE.COMPLETED)

        assert new_enrollment.state == ENROLLMENT_STATE.COMPLETED
        assert repo_activity.enrollments[0].state == ENROLLMENT_STATE.COMPLETED
        assert new_enrollment == repo_activity.enrollments[0]
