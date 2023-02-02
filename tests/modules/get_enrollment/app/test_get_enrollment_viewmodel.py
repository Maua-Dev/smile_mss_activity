from src.modules.get_enrollment.app.get_enrollment_viewmodel import GetEnrollmentViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetEnrollmentViewmodel:

    def test_get_enrollment_viewmodel(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[12]

        get_enrollment_viewmodel = GetEnrollmentViewmodel(enrollment, repo.users[6]).to_dict()

        expected = {'activity_code': 'CODIGO',
                    'user': {'name': 'Marcos Romanato', 'user_id': '38c3d7fe-a110-11ed-a8fc-0242ac120002', 'role': 'STUDENT'}, 'state': 'ENROLLED',
                    'date_subscribed': 1671661013000, 'message': 'the enrollment was retrieved'}

        assert get_enrollment_viewmodel == expected

    def test_get_enrollment_viewmodel_date_none(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[7]

        get_enrollment_viewmodel = GetEnrollmentViewmodel(enrollment, repo.users[1]).to_dict()

        expected = {'activity_code': 'ELET355',
                    'user': {'name': 'Bruno Soller', 'user_id': '0355535e-a110-11ed-a8fc-0242ac120002', 'role': 'STUDENT'}, 'state': 'ENROLLED',
                    'date_subscribed': 1671488213000, 'message': 'the enrollment was retrieved'}

        assert get_enrollment_viewmodel == expected
