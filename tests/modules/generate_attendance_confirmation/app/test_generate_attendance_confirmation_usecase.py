import pytest

from src.modules.generate_attendance_confirmation.app.generate_attendance_confirmation_usecase import \
    GenerateAttendanceConfirmationUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GenerateAttendanceConfirmationUsecase:
    def test_generate_attendance_confirmation_usecase(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GenerateAttendanceConfirmationUsecase(repo)

        requester_user = repo_user.users[2]

        confirmation_code = usecase(requester_user=requester_user, code=repo.activities[0].code)

        assert repo.activities[0].confirmation_code is not None
        assert confirmation_code == repo.activities[0].confirmation_code
        assert type(confirmation_code) == str
        assert len(confirmation_code) == 6
        assert confirmation_code.isnumeric()

    def test_generate_attendance_confirmation_usecase_wrong_code_type(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GenerateAttendanceConfirmationUsecase(repo)

        requester_user = repo_user.users[2]

        with pytest.raises(EntityError):
            usecase(requester_user=requester_user, code=123)

    def test_generate_attendance_confirmation_usecase_wrong_role(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GenerateAttendanceConfirmationUsecase(repo)

        requester_user = repo_user.users[0]

        with pytest.raises(ForbiddenAction):
            usecase(requester_user=requester_user, code=repo.activities[0].code)

    def test_generate_attendance_confirmation_usecase_wrong_user(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GenerateAttendanceConfirmationUsecase(repo)

        requester_user = repo_user.users[10]

        with pytest.raises(ForbiddenAction):
            usecase(requester_user=requester_user, code=repo.activities[0].code)

    def test_generate_attendance_confirmation_usecase_activity_not_found(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GenerateAttendanceConfirmationUsecase(repo)

        requester_user = repo_user.users[2]

        with pytest.raises(NoItemsFound):
            usecase(requester_user=requester_user, code="CODIGO_INEXISTENTE")

    def test_generate_attendance_confirmation_usecase_activity_already_has_confirmation_code(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GenerateAttendanceConfirmationUsecase(repo)

        requester_user = repo_user.users[2]

        with pytest.raises(ForbiddenAction):
            usecase(requester_user=requester_user, code=repo.activities[11].code)
