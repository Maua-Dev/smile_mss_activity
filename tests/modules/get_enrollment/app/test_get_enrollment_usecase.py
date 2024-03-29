import pytest

from src.modules.get_enrollment.app.get_enrollment_usecase import GetEnrollmentUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock

observability = ObservabilityMock(module_name="get_enrollment")

class Test_GetEnrollmentUsecase:

    def test_get_enrollment_usecase(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentUsecase(repo, observability=observability)

        enrollment = usecase(user_id=repo.enrollments[3].user_id, code=repo.enrollments[3].activity_code)

        assert enrollment == repo.enrollments[3]

    def test_get_enrollment_usecase_with_wrong_user_id(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentUsecase(repo, observability=observability)

        with pytest.raises(NoItemsFound):
            enrollment = usecase(user_id="0000-0000-00000-000000-0000000-00000", code=repo.enrollments[3].activity_code)

    def test_get_enrollment_usecase_with_wrong_code(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentUsecase(repo, observability=observability)

        with pytest.raises(NoItemsFound):
            enrollment = usecase(user_id=repo.enrollments[3].user_id, code="wrong_code")

    def test_get_enrollment_usecase_wrong_user_id_int(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentUsecase(repo, observability=observability)

        with pytest.raises(EntityError):
            enrollment = usecase(user_id=123, code=repo.enrollments[3].activity_code)

    def test_get_enrollment_usecase_wrong_code_int(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentUsecase(repo, observability=observability)

        with pytest.raises(EntityError):
            enrollment = usecase(user_id=repo.enrollments[3].user_id, code=123)


