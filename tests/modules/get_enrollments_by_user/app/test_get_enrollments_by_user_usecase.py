import pytest

from src.modules.get_enrollments_by_user.app.get_enrollments_by_user_usecase import GetEnrollmentsByUserUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
observability = ObservabilityMock(module_name="get_enrollments_by_user")


class Test_GetEnrollmentsByUserId:
    def test_get_enrollments_by_user_usecase(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetEnrollmentsByUserUsecase(repo, observability=observability)

        list_enrollments = usecase(user_id=repo_user.users[1].user_id)


        assert type(list_enrollments) == list
        assert len(list_enrollments) == 4
        assert all(type(enrollment) == Enrollment for enrollment in list_enrollments)
        assert all(enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE for enrollment in list_enrollments)
        assert all(enrollment.user_id == repo_user.users[1].user_id for enrollment in list_enrollments)

    def test_get_enrollments_by_user_usecase_invalid_user_id(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetEnrollmentsByUserUsecase(repo, observability=observability)

        with pytest.raises (EntityError):
            list_enrollments = usecase(user_id='INVALID_USER_ID')



