import datetime
from src.modules.update_activity.app.update_activity_usecase import UpdateActivityUsecase
from src.modules.update_activity.app.update_activity_viewmodel import UpdateActivityViewmodel
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_UpdateActivityViewmodel:

    def teste_update_activity_viewmodel(self):
        repo = ActivityRepositoryMock()
        viewmodel = UpdateActivityViewmodel(repo.activities[0])

        expected = {
            'message': 'the activity_code was updated',
            'activity_code': {
                'accepting_new_enrollments': True,
                'activity_type': 'COURSE',
                'code': 'ECM2345',
                'delivery_model': 'IN_PERSON',
                'description': 'Isso é uma atividade',
                'duration': 120,
                'link': None,
                'place': 'H332',
                'is_extensive': False,
                'responsible_professors': [
                    {
                        'name': 'Caio Toledo',
                        'role': 'PROFESSOR',
                        'user_id': '03555624-a110-11ed-a8fc-0242ac120002'}],
                'speakers': [{'bio': 'Incrível',
                              'company': 'Apple',
                              'name': 'Vitor Briquez'}],
                'start_date': 1671747413000,
                'stop_accepting_new_enrollments_before': 1671743812000,
                'taken_slots': 4,
                'title': 'Atividade da ECM 2345',
                'total_slots': 4
            }
        }

        assert viewmodel.to_dict() == expected
