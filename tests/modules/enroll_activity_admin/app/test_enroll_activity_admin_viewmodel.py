from src.modules.enroll_activity.app.enroll_activity_viewmodel import EnrollActivityViewmodel
from src.modules.enroll_activity_admin.app.enroll_activity_admin_viewmodel import EnrollActivityAdminViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_EnrollActivityViewmodel:

    def test_enroll_activity_viewmodel(self):
        repo = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        enrollment = repo.enrollments[1]

        enroll_activity_viewmodel = EnrollActivityAdminViewmodel(enrollment, repo_user.users[1]).to_dict()

        expected = {
            'activity_code': 'ECM2345',
            'user': {'name': 'Bruno Soller', 'user_id': '0355535e-a110-11ed-a8fc-0242ac120002', 'role': 'STUDENT'}, 'state': 'ENROLLED',
            'date_subscribed': 1671315413000, 'message': 'the enrollment was enrolled'}

        assert enroll_activity_viewmodel == expected
