from src.modules.get_enrollment.app.get_enrollment_viewmodel import GetEnrollmentViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetEnrollmentViewmodel:

    def test_get_enrollment_viewmodel(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[12]

        getEnrollmentViewmodel = GetEnrollmentViewmodel(enrollment).to_dict()

        expected = {'activity': {'code': 'CODIGO', 'title': 'Atividade da CÓDIGO',
                                 'description': 'Isso DEFINITIVAMENTE é uma atividade!',
                                 'activity_type': 'TECHNICAL_VISITS', 'is_extensive': False, 'delivery_model': 'ONLINE',
                                 'start_date': '2022-12-25 19:16:52', 'duration': 60, 'responsible_professors': [
                {'name': 'Caio Toledo', 'user_id': 'd7f1', 'role': 'PROFESSOR'}],
                                 'speakers': [{'name': 'Vitor Briquez', 'bio': 'Incrível', 'company': 'Apple'},
                                              {'name': 'Lucas Soller', 'bio': 'Daora', 'company': 'Microsoft'},
                                              {'name': 'Daniel Romanato', 'bio': 'Buscando descobrir o mundo',
                                               'company': 'Samsung'}], 'total_slots': 15, 'taken_slots': 2,
                                 'accepting_new_subscriptions': True,
                                 'stop_accepting_new_subscriptions_before': '2022-12-22 19:16:52'},
                    'user': {'name': 'Marcos Romanato', 'user_id': 'bea2', 'role': 'STUDENT'}, 'state': 'ENROLLED',
                    'date_subscribed': '2022-12-21 19:16:52', 'message': 'the enrollment was retrieved'}

        assert getEnrollmentViewmodel == expected
