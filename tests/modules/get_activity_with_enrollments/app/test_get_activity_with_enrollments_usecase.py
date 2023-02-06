from src.modules.get_activity_with_enrollments.app.get_activity_with_enrollments_usecase import \
    GetActivityWithEnrollmentsUsecase
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
from src.shared.domain.entities.activity import Activity
import pytest

class Test_GetActivityWithEnrollmentsUsecase:
    def test_get_activity_with_enrollments(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        activity_dict = usecase(user=repo_user.users[2], code=repo_activity.activities[0].code)

        assert isinstance(activity_dict["activity"], Activity)
        assert isinstance(activity_dict["enrollments"], list)

        for enrollment in activity_dict["enrollments"]:
            assert type(enrollment[0]) == Enrollment
            assert type(enrollment[1]) == User
    def test_get_activity_with_enrollments_wrong_type_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)

        with pytest.raises(EntityError):
            activity_dict = usecase(user=repo_user.users[2], code=1)

    def test_get_activity_with_enrollments_activity_not_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)

        with pytest.raises(NoItemsFound):
            activity_dict = usecase(user=repo_user.users[2], code="NÃO_EXISTE")

    @pytest.mark.skip(reason="Still no ForbiddenAction exception")
    def test_get_activity_with_enrollments_forbidden_non_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)

        with pytest.raises(ForbiddenAction):
            activity_with_enrollment = usecase(user=repo_user.users[1], code=repo_activity.activities[0].code)

    @pytest.mark.skip(reason="Still no ForbiddenAction exception")
    def test_get_activity_with_enrollments_forbidden_wrong_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)

        with pytest.raises(ForbiddenAction):
            activity_with_enrollment = usecase(user=repo_user.users[11], code=repo_activity.activities[0].code)

