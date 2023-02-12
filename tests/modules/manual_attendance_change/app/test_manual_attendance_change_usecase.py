from src.modules.manual_attendance_change.app.manual_attendance_change_usecase import ManualAttendanceChangeUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
import pytest


class Test_ManualAttendanceChangeUsecase:

    def test_manual_attendance_change_usecase(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0] #old one
        requester_user = repo_user.users[2]

        activity_dict = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                 user_id=enrollment.user_id,
                                 new_state=ENROLLMENT_STATE.COMPLETED)


        assert repo_activity.enrollments[0].state == ENROLLMENT_STATE.COMPLETED
        assert isinstance(activity_dict["activity"], Activity)
        assert activity_dict["activity"] == repo_activity.activities[0]

        for enrollment in activity_dict["enrollments"]:
            assert type(enrollment[0]) == Enrollment
            assert type(enrollment[1]) == User
            assert (enrollment[0].state == ENROLLMENT_STATE.ENROLLED) or \
                   (enrollment[0].state == ENROLLMENT_STATE.COMPLETED)


    def test_manual_attendance_change_usecase_disconfirming(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[29]  # old one
        requester_user = repo_user.users[2]

        activity_dict = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                 user_id=enrollment.user_id,
                                 new_state=ENROLLMENT_STATE.ENROLLED)

        assert repo_activity.enrollments[29].state == ENROLLMENT_STATE.ENROLLED
        for enrollment in activity_dict["enrollments"]:
            assert type(enrollment[0]) == Enrollment
            assert type(enrollment[1]) == User
            assert (enrollment[0].state == ENROLLMENT_STATE.ENROLLED) or \
                   (enrollment[0].state == ENROLLMENT_STATE.COMPLETED)

    def test_manual_attendance_change_usecase_admin(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0]
        requester_user = repo_user.users[0]

        activity_dict = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                user_id=enrollment.user_id,
                                new_state=ENROLLMENT_STATE.COMPLETED)

        assert repo_activity.enrollments[0].state == ENROLLMENT_STATE.COMPLETED
        assert isinstance(activity_dict["activity"], Activity)
        assert activity_dict["activity"] == repo_activity.activities[0]

        for enrollment in activity_dict["enrollments"]:
            assert type(enrollment[0]) == Enrollment
            assert type(enrollment[1]) == User
            assert (enrollment[0].state == ENROLLMENT_STATE.ENROLLED) or \
                   (enrollment[0].state == ENROLLMENT_STATE.COMPLETED)

    def test_manual_attendance_change_usecase_no_enrollments(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0]  # old one
        requester_user = repo_user.users[2]

        with pytest.raises(NoItemsFound):
            usecase(requester_user=requester_user, code=enrollment.activity_code, user_id="0"*36,
                    new_state=ENROLLMENT_STATE.COMPLETED)


    def test_manual_attendance_change_usecase_wrong_type_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0] #old one
        requester_user = repo_user.users[2]

        with pytest.raises(EntityError):
            usecase(requester_user=requester_user, code=1234, user_id=enrollment.user_id,
                    new_state=ENROLLMENT_STATE.COMPLETED)

    def test_manual_attendance_change_usecase_invalid_user_id(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0] #old one
        requester_user = repo_user.users[2]

        with pytest.raises(EntityError):
            usecase(requester_user=requester_user, code=enrollment.activity_code, user_id=12345,
                    new_state=ENROLLMENT_STATE.COMPLETED)

    def test_manual_attendance_change_usecase_wrong_type_state(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0] #old one
        requester_user = repo_user.users[2]

        with pytest.raises(EntityError):
            activity_dict = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                     user_id=enrollment.user_id,
                                     new_state='completed')

    def test_manual_attendance_change_usecase_non_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0] #old one
        requester_user = repo_user.users[1]

        with pytest.raises(ForbiddenAction):
            activity_dict = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                     user_id=enrollment.user_id,
                                     new_state=ENROLLMENT_STATE.COMPLETED)

    def test_manual_attendance_change_usecase_non_professor_of_activity(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0]  # old one
        requester_user = repo_user.users[10]

        with pytest.raises(ForbiddenAction):
            activity_dict = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                    user_id=enrollment.user_id,
                                    new_state=ENROLLMENT_STATE.COMPLETED)



    def test_manual_attendance_change_usecase_new_state_not_completed_nor_enrolled(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[1] #old one
        requester_user = repo_user.users[2]

        with pytest.raises(NoItemsFound):
            activity_dict = usecase(code='CÓDIGO_INEXISTENTE', requester_user=requester_user,
                                     user_id=enrollment.user_id,
                                     new_state=ENROLLMENT_STATE.COMPLETED)


    def test_manual_attendance_change_usecase_not_enrolled_to_confirm(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[5] #old one
        requester_user = repo_user.users[2]

        with pytest.raises(ForbiddenAction):
            activity_dict = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                     user_id=enrollment.user_id,
                                     new_state=ENROLLMENT_STATE.COMPLETED)

    def test_manual_attendance_change_usecase_not_complete_to_disconfirm(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        enrollment = repo_activity.enrollments[0] #old one
        requester_user = repo_user.users[2]

        with pytest.raises(ForbiddenAction):
            activity_dict = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                     user_id=enrollment.user_id,
                                     new_state=ENROLLMENT_STATE.ENROLLED)

