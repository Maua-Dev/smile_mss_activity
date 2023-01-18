import datetime
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
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

    def test_get_user(self):
        repo = ActivityRepositoryMock()
        user = repo.get_user('db43')
        assert type(user) == User  

    def test_get_user_not_exists(self):
        repo = ActivityRepositoryMock()
        user = repo.get_user('NAO-EXISTE')
        assert user is None

    def test_create_enrollment(self):
        repo = ActivityRepositoryMock()
        enrollment = Enrollment(
            repo.get_activity('ECM2345'),
            repo.get_user('db43'),
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=datetime.datetime(2022, 12, 16, 19, 16, 52, 998305)
        )

        len_before = len(repo.enrollments)
        enrollment_created = repo.create_enrollment(enrollment=enrollment)
        len_after = len(repo.enrollments)

        assert type(enrollment_created) == Enrollment
        assert repo.enrollments[0].activity == repo.get_activity('ECM2345')
        assert repo.enrollments[0].user == repo.get_user('db43')
        assert repo.enrollments[0].state == ENROLLMENT_STATE.ENROLLED
        assert repo.enrollments[0].date_subscribed == datetime.datetime(2022, 12, 16, 19, 16, 52, 998305)
        assert len_before == len_after - 1
