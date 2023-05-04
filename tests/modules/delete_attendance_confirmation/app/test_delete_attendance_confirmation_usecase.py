import pytest

from src.modules.delete_attendance_confirmation.app.delete_attendance_confirmation_usecase import DeleteAttendanceConfirmationUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="delete_attendance_confirmation")

class Test_DeleteAttendanceConfirmationUsecase:
       def test_delete_attendance_confirmation_code_usecase(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo, observability=observability)

              requester_user = repo_user.users[2]

              delete_confirmation_code = usecase(code=repo.activities[11].code, requester_user=requester_user)

              assert repo.activities[11].confirmation_code == None
              assert delete_confirmation_code == None
              assert delete_confirmation_code == repo.activities[11].confirmation_code

       def test_delete_attendance_confirmation_code_usecase_wrong_code_type(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo, observability=observability)

              requester_user = repo_user.users[2]

              with pytest.raises(EntityError):
                     usecase(code=123, requester_user=requester_user)

       def test_delete_attendance_confirmation_code_usecase_wrong_role(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo, observability=observability)

              requester_user = repo_user.users[0]

              with pytest.raises(ForbiddenAction):
                     usecase(code=repo.activities[0].code, requester_user=requester_user)

       def test_delete_attendance_confirmation_code_usecase_wrong_user(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo, observability=observability)

              requester_user = repo_user.users[1]

              with pytest.raises(ForbiddenAction):
                     usecase(code=repo.activities[11].code, requester_user=requester_user)

       def test_delete_attendance_confirmation_code_activity_not_found(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo, observability=observability)

              requester_user = repo_user.users[2]

              with pytest.raises(NoItemsFound):
                     usecase(code="UM_CODIGO_QUALQUER", requester_user=requester_user)

       def test_delete_attendance_confirmation_code_activity_do_not_have_confirmation_code(self):
              repo = ActivityRepositoryMock()
              repo_user = UserRepositoryMock()
              usecase = DeleteAttendanceConfirmationUsecase(repo, observability=observability)

              requester_user = repo_user.users[2]

              with pytest.raises(ForbiddenAction):
                     usecase(code=repo.activities[0].code, requester_user=requester_user)  
