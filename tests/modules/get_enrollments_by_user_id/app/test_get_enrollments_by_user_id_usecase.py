import pytest

from src.modules.get_enrollments_by_user_id.app.get_enrollments_by_user_id_usecase import GetEnrollmentsByUserIdUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetEnrollmentsByUserId:
    def test_get_enrollments_by_user_id_usecase(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentsByUserIdUsecase(repo)

        list_enrollments = usecase(user_id=repo.users[1].user_id)


        assert type(list_enrollments) == list
        assert len(list_enrollments) == 4
        assert all(type(enrollment) == Enrollment for enrollment in list_enrollments)
        assert all(enrollment.state == ENROLLMENT_STATE.ENROLLED for enrollment in list_enrollments)
        assert all(enrollment.user_id == repo.users[1].user_id for enrollment in list_enrollments)

    def test_get_enrollments_by_user_id_usecase_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentsByUserIdUsecase(repo)

        with pytest.raises (EntityError):
            list_enrollments = usecase(user_id='INVALID_USER_ID')



