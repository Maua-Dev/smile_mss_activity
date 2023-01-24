from src.modules.enroll_activity.app.enroll_activity_viewmodel import EnrollActivityViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_EnrollActivityViewmodel:

    def test_enroll_activity_viewmodel(self):
        repo = ActivityRepositoryMock()

        enrollment = repo.enrollments[1]

        enroll_activity_viewmodel = EnrollActivityViewmodel(enrollment).to_dict()

        expected = {
            'activity': {'code': 'ECM2345', 'title': 'Atividade da ECM 2345', 'description': 'Isso é uma atividade',
                         'activity_type': 'COURSE', 'is_extensive': False, 'delivery_model': 'IN_PERSON',
                         'start_date': 1671747413000000, 'duration': 120, 'link': None, 'place': 'H332',
                         'responsible_professors': [{'name': 'Caio Toledo', 'user_id': 'd7f1', 'role': 'PROFESSOR'}],
                         'speakers': [{'name': 'Vitor Briquez', 'bio': 'Incrível', 'company': 'Apple'}],
                         'total_slots': 4, 'taken_slots': 4, 'accepting_new_enrollments': True,
                         'stop_accepting_new_enrollments_before': 1671743812000000},
            'user': {'name': 'Bruno Soller', 'user_id': 'b16f', 'role': 'STUDENT'}, 'state': 'ENROLLED',
            'date_subscribed': '2022-12-17T19:16:52.998305', 'message': 'the enrollment was enrolled'}

        assert enroll_activity_viewmodel == expected
