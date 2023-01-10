from src.modules.drop_activity.app.drop_activity_viewmodel import DropActivityViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_DropActivityViewmodel:

    def test_drop_activity_viewmodel(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[12]

        dropActivityViewmodel = DropActivityViewmodel(enrollment).to_dict()

        expected = {'activity': {'code': 'CODIGO', 'title': 'Atividade da CÓDIGO',
                                 'description': 'Isso DEFINITIVAMENTE é uma atividade!',
                                 'activity_type': 'TECHNICAL_VISITS', 'is_extensive': False, 'delivery_model': 'ONLINE',
                                 'start_date': '2022-12-25T19:16:52.998305', 'duration': 60, 'responsible_professors': [
                {'name': 'Caio Toledo', 'user_id': 'd7f1', 'role': 'PROFESSOR'}],
                                 'speakers': [{'name': 'Vitor Briquez', 'bio': 'Incrível', 'company': 'Apple'},
                                              {'name': 'Lucas Soller', 'bio': 'Daora', 'company': 'Microsoft'},
                                              {'name': 'Daniel Romanato', 'bio': 'Buscando descobrir o mundo',
                                               'company': 'Samsung'}], 'total_slots': 15, 'taken_slots': 2,
                                 'accepting_new_enrollments': True,
                                 'stop_accepting_new_enrollments_before': '2022-12-22T19:16:52.998305'},
                    'user': {'name': 'Marcos Romanato', 'user_id': 'bea2', 'role': 'STUDENT'}, 'state': 'ENROLLED',
                    'date_subscribed': '2022-12-21T19:16:52.998305', 'message': 'the enrollment was dropped'}

        assert dropActivityViewmodel == expected
