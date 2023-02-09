import pytest

from src.modules.get_activities_responsible_professor.app.get_activities_responsible_professor_usecase import \
    GetActivitiesResponsibleProfessorUsecase
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetActivitiesResponsibleProfessorUsecase:

    def test_get_activities_responsible_professor_usecase(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)

        requester_user = repo_user.users[2]

        specific_professor_activities_with_enrollments_dict = usecase(requester_user)

        assert len(specific_professor_activities_with_enrollments_dict) == 9
        for activity_code, activity_dict in specific_professor_activities_with_enrollments_dict.items():
            assert isinstance(activity_dict["activity"], Activity)
            assert activity_dict["activity"].code == activity_code
            assert requester_user in activity_dict["activity"].responsible_professors
            assert isinstance(activity_dict["enrollments"], list)
            for enrollment, user in activity_dict["enrollments"]:
                assert isinstance(enrollment, Enrollment)
                assert enrollment.user_id == user.user_id
                assert isinstance(user, User)

    def test_get_activities_responsible_professor_usecase_no_items(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)

        requester_user = repo_user.users[12]

        specific_professor_activities_with_enrollments_dict = usecase(requester_user)

        assert len(specific_professor_activities_with_enrollments_dict) == 0

    def test_get_activities_responsible_professor_usecase_with_invalid_requester_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)

        requester_user = repo_user.users[0]

        with pytest.raises(EntityError):
            specific_professor_activities_with_enrollments_dict = usecase(requester_user)

