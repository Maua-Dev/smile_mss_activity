import pytest

from src.modules.get_all_activities_admin.app.get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetAllActivitiesAdminUsecase:
    def test_get_all_activities_admin(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo=repo)
        all_activities_with_enrollments = usecase(repo.users[0])

        assert type(all_activities_with_enrollments) == list
        assert type(all_activities_with_enrollments[0]) == tuple
        assert type(all_activities_with_enrollments[0][0]) == Activity
        assert all(all(type(enrollment) == Enrollment for enrollment in enrollments) for activity, enrollments in
                   all_activities_with_enrollments)
        assert len(all_activities_with_enrollments) == len(repo.activities)

    @pytest.mark.skip(reason="Still no ForbiddenAction exception")
    def test_get_all_activities_admin_forbidden_not_admin(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            all_activities_with_enrollments = usecase(repo.users[1])
