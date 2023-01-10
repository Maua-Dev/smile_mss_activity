from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_ActivityRepositoryMock:
    def test_get_activity(self):
        repo = ActivityRepositoryMock()
        activity = repo.get_activity("CAFE")
        assert activity is not None

    def test_get_activity_not_exists(self):
        repo = ActivityRepositoryMock()
        activity = repo.get_activity("CODIGO_INEXISTENTE")
        assert activity is None
