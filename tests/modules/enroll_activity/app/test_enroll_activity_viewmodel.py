from src.modules.enroll_activity.app.enroll_activity_viewmodel import EnrollActivityViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_EnrollActivityViewmodel:

    def test_enroll_activity_viewmodel(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[1]

        enroll_activity_viewmodel = EnrollActivityViewmodel(enrollment).to_dict()

        expected = {
            'activity_code': 'ECM2345',
            'user': {'name': 'Bruno Soller', 'user_id': '0355535e-a110-11ed-a8fc-0242ac120002', 'role': 'STUDENT'}, 'state': 'ENROLLED',
            'date_subscribed': 1671315413000, 'message': 'the enrollment was enrolled'}

        assert enroll_activity_viewmodel == expected
