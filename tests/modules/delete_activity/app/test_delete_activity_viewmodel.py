import datetime

from src.modules.delete_activity.app.delete_activity_viewmodel import DeleteActivityViewmodel
from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_DeleteActivityViewmodel:

    def test_delete_activity_viewmodel(self):
        repo = ActivityRepositoryMock()
        viewmodel = DeleteActivityViewmodel(
            repo.activities[0]
        )

        expected = {
            'activity': {'code': 'ECM2345', 'title': 'Atividade da ECM 2345', 'description': 'Isso é uma atividade',
                         'activity_type': 'COURSES', 'is_extensive': False, 'delivery_model': 'IN_PERSON',
                         'start_date': 1671747413000, 'duration': 120, 'link': None, 'place': 'H332',
                         'responsible_professors': [{'name': 'Caio Toledo', 'user_id': '03555624-a110-11ed-a8fc-0242ac120002', 'role': 'PROFESSOR'}],
                         'speakers': [{'name': 'Vitor Briquez', 'bio': 'Incrível', 'company': 'Apple'}],
                         'total_slots': 4, 'taken_slots': 4, 'accepting_new_enrollments': True,
                         'stop_accepting_new_enrollments_before': 1671743812000,
                         'confirmation_code': None},
            'message': 'the activity was deleted'}

        assert viewmodel.to_dict() == expected
