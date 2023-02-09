import pytest

from src.modules.get_activities_responsible_professor.app.get_activities_responsible_professor_usecase import \
    GetActivitiesResponsibleProfessorUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetActivitiesResponsibleProfessorUsecase:

    def test_get_activities_responsible_professor_usecase(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity)

        requester_user = repo_user.users[2]

        specific_professor_activities = usecase(requester_user)

        assert len(specific_professor_activities) == 9
        for activity in specific_professor_activities:
            assert requester_user in activity.responsible_professors

    def test_get_activities_responsible_professor_usecase_no_items(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity)

        requester_user = repo_user.users[12]

        specific_professor_activities = usecase(requester_user)

        assert len(specific_professor_activities) == 0

    def test_get_activities_responsible_professor_usecase_with_invalid_requester_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity)

        requester_user = repo_user.users[0]

        with pytest.raises(ForbiddenAction):
            specific_professor_activities = usecase(requester_user)

