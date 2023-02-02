import pytest

from src.modules.get_all_activities_admin.app.get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetAllActivitiesAdminUsecase:
    def test_get_all_activities_admin(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo=repo)
        all_activities_dict = usecase(repo.users[0])

        assert len(all_activities_dict) == len(repo.activities)
        for activity_code, activity_dict in all_activities_dict.items():
            assert isinstance(activity_dict["activity"], Activity)
            assert isinstance(activity_dict["enrollments"], list)
            for enrollment, user in activity_dict["enrollments"]:
                assert isinstance(enrollment, Enrollment)
                assert enrollment.user_id == user.user_id
                assert isinstance(user, User)


    @pytest.mark.skip(reason="Still no ForbiddenAction exception")
    def test_get_all_activities_admin_forbidden_not_admin(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo=repo)

        with pytest.raises(ForbiddenAction):
            all_activities_with_enrollments = usecase(repo.users[1])
