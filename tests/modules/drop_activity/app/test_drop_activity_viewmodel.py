from src.modules.drop_activity.app.drop_activity_viewmodel import DropActivityViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_DropActivityViewmodel:

    def test_drop_activity_viewmodel_in_queue(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[4]

        dropActivityViewmodel = DropActivityViewmodel(enrollment).to_dict()

        expected = {
            'activity': {'code': 'ECM2345', 'title': 'Atividade da ECM 2345', 'description': 'Isso é uma atividade',
                          'activity_type': 'COURSE', 'is_extensive': False, 'delivery_model': 'IN_PERSON',
                          'start_date': '2022-12-22T19:16:52.998305', 'duration': 120,
                          'responsible_professors': [{'name': 'Caio Toledo', 'user_id': 'd7f1', 'role': 'PROFESSOR'}],
                          'speakers': [{'name': 'Vitor Briquez', 'bio': 'Incrível', 'company': 'Apple'}],
                          'total_slots': 4, 'taken_slots': 4, 'accepting_new_enrollments': True,
                          'stop_accepting_new_enrollments_before': '2022-12-22T18:16:52.998305'},
             'user': {'name': 'Hector Guerrini', 'user_id': '9257', 'role': 'EXTERNAL'}, 'state': 'IN_QUEUE',
             'date_subscribed': '2022-12-20T19:16:52.998305', 'message': 'the enrollment was set in_queue'
        }

        assert dropActivityViewmodel == expected

    def test_drop_activity_viewmodel_dropped(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[8]

        dropActivityViewmodel = DropActivityViewmodel(enrollment).to_dict()

        expected = {'activity': {'code': 'COD1468', 'title': 'Atividade da COD 1468',
                          'description': 'Isso definitivamente é uma atividade',
                          'activity_type': 'HIGH_IMPACT_LECTURES', 'is_extensive': True, 'delivery_model': 'ONLINE',
                          'start_date': '2022-12-21T19:16:52.998305', 'duration': 60,
                          'responsible_professors': [{'name': 'Caio Toledo', 'user_id': 'd7f1', 'role': 'PROFESSOR'},
                                                     {'name': 'Patricia Santos', 'user_id': 'c695',
                                                      'role': 'PROFESSOR'}], 'speakers': [
                    {'name': 'Daniel Romanato', 'bio': 'Buscando descobrir o mundo', 'company': 'Samsung'}],
                          'total_slots': 50, 'taken_slots': 1, 'accepting_new_enrollments': True,
                          'stop_accepting_new_enrollments_before': None},
             'user': {'name': 'Pedro Marcelino', 'user_id': '80fb', 'role': 'INTERNATIONAL_STUDENT'},
             'state': 'DROPPED', 'date_subscribed': '2022-12-19T19:16:51.998305',
             'message': 'the enrollment was dropped'
        }

        assert dropActivityViewmodel == expected
