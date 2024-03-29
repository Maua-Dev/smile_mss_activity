from src.modules.get_all_activities.app.get_all_activities_usecase import GetAllActivitiesUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock

observability = ObservabilityMock(module_name="get_all_activites")

class Test_GetAllActivitiesUsecase:
    def test_get_all_activities(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesUsecase(repo=repo, observability=observability)
        all_activities = usecase()

        assert type(all_activities) == list
        assert all(type(activity) == Activity for activity in all_activities)
        assert len(all_activities) == len(repo.activities)
