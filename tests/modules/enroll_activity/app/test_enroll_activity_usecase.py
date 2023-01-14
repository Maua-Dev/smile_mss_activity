import pytest

from src.modules.enroll_activity.app.enroll_activity_usecase import EnrollActivityUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.activity import Activity
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError


class Test_EnrollActivityUsecase:

    #teste user_id
    def test_enroll_activity_usecase_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)

        with pytest.raises(EntityError):
            enrollment_activity = usecase('usuario2345', 'code')

    def test_enroll_activity_usecase_invalid_code(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)

        with pytest.raises(EntityError):
            enrollment_activity = usecase('b16f', 852)

    def test_enroll_activity_usecase_is_not_none(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)

        with pytest.raises(ForbiddenAction):
            enrollment_activity = usecase(repo.users[1].user_id, repo.activities[11].code)

    def test_enroll_activity_usecase_accepting_new_enrollments(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        enrollment_activity = usecase(repo.users[1].user_id, repo.activities[1].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user.user_id == repo.users[1].user_id
        assert enrollment_activity.activity.code == repo.activities[1].code
        assert enrollment_activity.activity.accepting_new_enrollments == True
     
    def test_enroll_activity_usecase_in_queue(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        enrollment_activity = usecase(repo.users[1].user_id, repo.activities[0].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user.user_id == repo.users[1].user_id
        assert enrollment_activity.activity.code == repo.activities[0].code
        assert enrollment_activity.activity.taken_slots >= enrollment_activity.activity.total_slots

    def test_enroll_activity_usecase_enrolled(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        enrollment_activity = usecase(repo.users[1].user_id, repo.activities[1].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user.user_id == repo.users[1].user_id
        assert enrollment_activity.activity.code == repo.activities[1].code
        assert enrollment_activity.activity.taken_slots < enrollment_activity.activity.total_slots