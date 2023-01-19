from src.modules.get_enrollment.app.get_enrollment_viewmodel import GetEnrollmentViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetEnrollmentViewmodel:

    def test_get_enrollment_viewmodel(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[12]

        get_enrollment_viewmodel = GetEnrollmentViewmodel(enrollment).to_dict()

        expected = {'activity': {'code': 'CODIGO', 'title': 'Atividade da CÓDIGO',
                                 'description': 'Isso DEFINITIVAMENTE é uma atividade!',
                                 'activity_type': 'TECHNICAL_VISITS', 'is_extensive': False, 'delivery_model': 'ONLINE',
                                 'start_date': '2022-12-25T19:16:52.998305', 'duration': 60,
                                 'link': 'https://devmaua.com', 'place': None, 'responsible_professors': [
                {'name': 'Caio Toledo', 'user_id': 'd7f1', 'role': 'PROFESSOR'}],
                                 'speakers': [{'name': 'Vitor Briquez', 'bio': 'Incrível', 'company': 'Apple'},
                                              {'name': 'Lucas Soller', 'bio': 'Daora', 'company': 'Microsoft'},
                                              {'name': 'Daniel Romanato', 'bio': 'Buscando descobrir o mundo',
                                               'company': 'Samsung'}], 'total_slots': 15, 'taken_slots': 2,
                                 'accepting_new_enrollments': True,
                                 'stop_accepting_new_enrollments_before': '2022-12-22T19:16:52.998305'},
                    'user': {'name': 'Marcos Romanato', 'user_id': 'bea2', 'role': 'STUDENT'}, 'state': 'ENROLLED',
                    'date_subscribed': '2022-12-21T19:16:52.998305', 'message': 'the enrollment was retrieved'}

        assert get_enrollment_viewmodel == expected

    def test_get_enrollment_viewmodel_date_none(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[7]

        get_enrollment_viewmodel = GetEnrollmentViewmodel(enrollment).to_dict()

        expected = {'activity': {'code': 'ELET355', 'title': 'Atividade da ELET 355',
                                 'description': 'Isso é uma atividade, sério.', 'activity_type': 'LECTURES',
                                 'is_extensive': True, 'delivery_model': 'HYBRID',
                                 'start_date': '2022-12-21T19:16:52.998305', 'duration': 400,
                                 'link': 'https://devmaua.com', 'place': 'H332', 'responsible_professors': [
                {'name': 'Patricia Santos', 'user_id': 'c695', 'role': 'PROFESSOR'}],
                                 'speakers': [{'name': 'Lucas Soller', 'bio': 'Daora', 'company': 'Microsoft'}],
                                 'total_slots': 10, 'taken_slots': 1, 'accepting_new_enrollments': True,
                                 'stop_accepting_new_enrollments_before': None},
                    'user': {'name': 'Bruno Soller', 'user_id': 'b16f', 'role': 'STUDENT'}, 'state': 'ENROLLED',
                    'date_subscribed': '2022-12-19T19:16:52.998305', 'message': 'the enrollment was retrieved'}

        assert get_enrollment_viewmodel == expected
