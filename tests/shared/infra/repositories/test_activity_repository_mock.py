from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_ActivityRepositoryMock:

    def test_get_enrollment(self):
        repo = ActivityRepositoryMock()
        enrollment = repo.get_enrollment('db43', 'ECM2345')
        assert enrollment is not None

    def test_get_enrollment_not_exists(self):
        repo = ActivityRepositoryMock()
        enrollment = repo.get_enrollment('db43', 'CODIGO_INEXISTENTE')
        assert enrollment is None

    def test_get_activity(self):
        repo = ActivityRepositoryMock()
        activity = repo.get_activity("CAFE")
        assert activity is not None

    def test_get_activity_not_exists(self):
        repo = ActivityRepositoryMock()
        activity = repo.get_activity("CODIGO_INEXISTENTE")
        assert activity is None

    def test_update_enrollment(self):
        repo = ActivityRepositoryMock()
        enrollment = repo.update_enrollment(user_id="db43", code="ECM2345", state=ENROLLMENT_STATE.DROPPED)

        assert enrollment is not None
        assert enrollment.state == ENROLLMENT_STATE.DROPPED

    def test_get_activity_with_enrollments(self):
        repo = ActivityRepositoryMock()
        activity, enrollments = repo.get_activity_with_enrollments("2468")
        assert activity is not None
        assert enrollments is not None
