from src.modules.get_all_activities_admin.app.get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock




class Test_GetAllActivitiesAdminUsecase:
    def test_get_all_activities_admin(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo=repo)
        all_activities_with_enrollments = usecase()

        assert type(all_activities_with_enrollments) == list
        assert type(all_activities_with_enrollments[0]) == tuple
        assert len(all_activities_with_enrollments) == len(repo.activities)
