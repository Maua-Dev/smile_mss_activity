from src.modules.download_activity.app.download_activity_viewmodel import DownloadActivityViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

class TestDownloadActivityViewmodel:
    def test_download_activity_viewmodel(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        activity = repo_activity.activities[0]
        user = repo_user.users[0]

        download_activity_viewmodel = DownloadActivityViewmodel(activity, user).to_dict()

        expected = {
            'activity': {
                'code': 'ECM2345',
                'name': "Atividade da ECM 2345",
                'description': "Isso é uma atividade",
                'activity_type': 'COURSES',
                'is_extensive': False,
                'delivery_model': 'IN_PERSON',
                'start_date': 1671747413000,
                'end_date': 1671754613000,
                'place': "H332",
                'responsible_professors': [
                    {
                        'name': 'Caio Toledo',
                        'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                        'role': 'PROFESSOR'
                    }
                ],
                'speakers': [
                    {
                        'name': 'Vitor Briquez',
                        'bio': 'Incrível',
                        'company': 'Apple'
                    }
                ],
                'total_slots': 4,
                'taken_slots': 4,
                'accepting_new_enrollments': True,
                'stop_accepting_new_enrollments_before': 1671747413000
            },
            'requester_user':{
                'name': 'João Vilas',
                'role': 'ADMIN',
                'user_id': 'd61dbf66-a10f-11ed-a8fc-0242ac120002'
            }

        }
