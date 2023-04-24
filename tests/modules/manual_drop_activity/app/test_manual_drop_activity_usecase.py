from src.modules.manual_drop_activity.app.manual_drop_activity_usecase import ManualDropActivityUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock
import pytest

observability = ObservabilityMock(module_name="manual_drop_activity")

class Test_ManualDropActivityUsecase:

    def test_manual_drop_activity_usecase_admin(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        old_activity = repo_activity.activities[1]
        requester_user = repo_user.users[0]

        activity_dict = usecase(repo_user.users[1].user_id, old_activity.code, requester_user=requester_user)

        assert type(activity_dict) == dict
        assert isinstance(activity_dict['activity'], Activity)
        assert isinstance(activity_dict['enrollments'], list)
        assert repo_activity.enrollments[7].state == ENROLLMENT_STATE.DROPPED
        assert activity_dict['activity'].taken_slots == 0

    def test_manual_drop_activity_usecase_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity, repo_user=repo_user, observability=observability)
        old_activity = repo_activity.activities[1]
        requester_user = repo_user.users[10]

        activity_dict = usecase(repo_user.users[1].user_id, old_activity.code, requester_user=requester_user)

        assert type(activity_dict) == dict
        assert isinstance(activity_dict['activity'], Activity)
        assert isinstance(activity_dict['enrollments'], list)
        assert repo_activity.enrollments[7].state == ENROLLMENT_STATE.DROPPED
        assert activity_dict['activity'].taken_slots == 0

    def test_drop_activity_usecase_with_queue(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        requester_user = repo_user.users[0]
        activity_dict = usecase(repo_user.users[2].user_id, repo_activity.activities[0].code, requester_user=requester_user)

        assert type(activity_dict) == dict
        assert isinstance(activity_dict['activity'], Activity)
        assert isinstance(activity_dict['enrollments'], list)
        assert activity_dict['activity'].taken_slots == 4

        assert repo_activity.enrollments[2].state == ENROLLMENT_STATE.DROPPED
        assert repo_activity.enrollments[4].state == ENROLLMENT_STATE.ENROLLED

    def test_drop_activity_already_in_queue(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        requester_user = repo_user.users[0]
        activity_dict = usecase(repo_user.users[2].user_id, repo_activity.activities[0].code, requester_user=requester_user)


        assert type(activity_dict) == dict
        assert isinstance(activity_dict['activity'], Activity)
        assert isinstance(activity_dict['enrollments'], list)
        assert activity_dict['activity'].taken_slots == 4

        assert repo_activity.enrollments[5].state == ENROLLMENT_STATE.IN_QUEUE
        assert repo_activity.enrollments[4].state == ENROLLMENT_STATE.ENROLLED

    def test_drop_activity_usecase_invalid_user_id(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        requester_user = repo_user.users[0]

        with pytest.raises(EntityError):
            activity_dict = usecase("0", "ELET355",
                                         requester_user=requester_user)

    def test_drop_activity_usecase_invalid_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        requester_user = repo_user.users[0]

        with pytest.raises(EntityError):
            activity_dict = usecase("0355535e-a110-11ed-a8fc-0242ac120002", 123, requester_user=requester_user)

    def test_drop_activity_usecase_no_activity_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        requester_user = repo_user.users[0]

        with pytest.raises(NoItemsFound):
            activity_dict = usecase("0355535e-a110-11ed-a8fc-0242ac120002", "CODIGO_INEXISTENTE",
                                         requester_user=requester_user)

    def test_drop_activity_usecase_no_enrollment_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = ManualDropActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        requester_user = repo_user.users[0]

        with pytest.raises(NoItemsFound):
            activity_dict = usecase("0000-0000-00000-000000-0000000-00000", "ELET355",
                                         requester_user=requester_user)
