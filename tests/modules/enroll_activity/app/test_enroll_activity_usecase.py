import pytest

from src.modules.enroll_activity.app.enroll_activity_usecase import EnrollActivityUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError


class Test_EnrollActivityUsecase:


    def test_enroll_activity_usecase_accepting_new_enrollments(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)

        taken_slots_old = repo.activities[8].taken_slots
        enrollment_activity = usecase(repo.users[6].user_id, repo.activities[8].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user_id == repo.users[6].user_id
        assert enrollment_activity.activity_code == repo.activities[8].code
        assert enrollment_activity.state == ENROLLMENT_STATE.ENROLLED
        assert taken_slots_old + 1 == repo.activities[8].taken_slots

    def test_enroll_activity_usecase_in_queue(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        enrollment_activity = usecase(repo.users[8].user_id, repo.activities[0].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user_id == repo.users[8].user_id
        assert enrollment_activity.activity_code == repo.activities[0].code
        assert enrollment_activity.state == ENROLLMENT_STATE.IN_QUEUE

    def test_enroll_activity_usecase_enrolled(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)
        taken_slots_old = repo.activities[2].taken_slots
        enrollment_activity = usecase(repo.users[3].user_id, repo.activities[2].code)

        assert type(enrollment_activity) == Enrollment
        assert enrollment_activity.user_id == repo.users[3].user_id
        assert enrollment_activity.activity_code == repo.activities[2].code
        assert repo.activities[2].taken_slots < repo.activities[2].total_slots
        assert repo.activities[2].accepting_new_enrollments == True
        assert taken_slots_old + 1 == repo.activities[2].taken_slots
        assert enrollment_activity.state == ENROLLMENT_STATE.ENROLLED
        
    def test_enroll_activity_usecase_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)   

        with pytest.raises(EntityError):
            enrollment_activity = usecase('usuario2345', 'code')

    def test_enroll_activity_usecase_invalid_code(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)

        with pytest.raises(EntityError):
            enrollment_activity = usecase('0355535e-a110-11ed-a8fc-0242ac120002', 852)

    def test_enroll_activity_usecase_user_already_enrolled(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)

        with pytest.raises(ForbiddenAction):
            enrollment_activity = usecase('0355535e-a110-11ed-a8fc-0242ac120002', 'ELET355')

    def test_enroll_activity_usecase_activity_none(self):

        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)  

        with pytest.raises(NoItemsFound):
            enrollment_activity = usecase(repo.users[6].user_id, '')

    def test_enroll_activity_usecase_not_accepting_new_enrollment(self):
        repo = ActivityRepositoryMock()
        usecase = EnrollActivityUsecase(repo)

        with pytest.raises(ForbiddenAction):
            enrollment = usecase(usecase(repo.users[4].user_id, repo.activities[12].code))
