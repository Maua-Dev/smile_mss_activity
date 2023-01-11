import pytest

class Test_EnrollActivityUsecase:
    def test_enroll_activity_usecase_invalid_user_id(self):
        repo = ActivityRepositoryMock()