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

    def test_update_enrollment_drop(self):
        repo = ActivityRepositoryMock()
        taken_slots_before = repo.activities[0].taken_slots
        enrollment = repo.update_enrollment(user_id="db43", code="ECM2345", state=ENROLLMENT_STATE.DROPPED)

        assert repo.activities[0].taken_slots == taken_slots_before - 1
        assert enrollment is not None
        assert enrollment.state == ENROLLMENT_STATE.DROPPED

    def test_update_enrollment_enroll(self):
        repo = ActivityRepositoryMock()
        taken_slots_before = repo.activities[0].taken_slots
        enrollment = repo.update_enrollment(user_id="9257", code="ECM2345", state=ENROLLMENT_STATE.ENROLLED)

        assert repo.activities[0].taken_slots == taken_slots_before + 1
        assert enrollment is not None
        assert enrollment.state == ENROLLMENT_STATE.ENROLLED

    def test_get_activity_with_enrollments(self):
        repo = ActivityRepositoryMock()
        activity, enrollments = repo.get_activity_with_enrollments("2468")
        assert activity is not None
        assert enrollments is not None

    def test_update_activity_title(self):
        repo = ActivityRepositoryMock()
        activity = repo.update_activity(code="2468", new_title="Novo título")
        assert activity is not None
        assert activity.title == "Novo título"

    def test_update_activity_taken_slots(self):
        repo = ActivityRepositoryMock()
        activity = repo.update_activity(code="2468", new_taken_slots=10)
        assert activity is not None
        assert activity.taken_slots == 10
