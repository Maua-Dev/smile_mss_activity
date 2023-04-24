from src.modules.get_all_activities_logged.app.get_all_activities_logged_usecase import GetAllActivitiesLoggedUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="get_all_activities_logged")

class Test_GetAllActivitiesLoggedUsecase:
    def test_get_all_activities_logged(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        requester_user = repo_user.users[2]

        usecase = GetAllActivitiesLoggedUsecase(repo_activity, observability=observability)

        activities_logged = usecase(requester_user.user_id)

        assert len(activities_logged) == 13
        for activity_code, activity_logged in activities_logged.items():
            assert type(activity_logged['activity']) == Activity
            assert activity_logged['activity'].code == activity_code
            if "enrollment" in activity_logged:
                assert type(activity_logged['enrollment']) == Enrollment
                assert activity_logged['enrollment'].user_id == requester_user.user_id
                assert activity_logged['enrollment'].activity_code == activity_code
                assert activity_logged['enrollment'].state == ENROLLMENT_STATE.IN_QUEUE or  activity_logged['enrollment'].state == ENROLLMENT_STATE.ENROLLED or activity_logged['enrollment'].state == ENROLLMENT_STATE.COMPLETED


