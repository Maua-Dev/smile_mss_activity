from src.modules.manual_drop_activity.app.manual_drop_activity_usecase import ManualDropActivityUsecase
from src.modules.manual_drop_activity.app.manual_drop_activity_viewmodel import ManualDropActivityViewmodel
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="manual_drop_activity")

class Test_ManualDropActivityViewmodel:
    def test_get_activity_with_enrollments_viewmodel_disconfirming(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        enrollment = repo_activity.enrollments[0]
        requester_user = repo_user.users[0]
        usecase = ManualDropActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        activity_dict_with_enrollments = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                                 user_id=enrollment.user_id)

        viewmodel = ManualDropActivityViewmodel(activity_dict_with_enrollments)

        expected = {
            'activity_with_enrollments': {
                'activity': {
                    'code': 'ECM2345',
                    'title': 'Atividade da ECM 2345',
                    'description': 'Isso é uma atividade',
                    'activity_type': 'COURSES',
                    'is_extensive': False,
                    'delivery_model': 'IN_PERSON',
                    'start_date': 1671747413000,
                    'end_date': 120*60*1000 + 1671747413000,
                    'link': None,
                    'place': 'H332',
                    'responsible_professors': [
                        {
                            'name': 'Caio Toledo',
                            'role': 'PROFESSOR',
                            'user_id': '03555624-a110-11ed-a8fc-0242ac120002'
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
                    'stop_accepting_new_enrollments_before': 1671743812000,
                    'confirmation_code': None
                },
                'enrollments': [
                    {
                        'user': {
                            'name': 'Bruno Soller',
                            'role': 'STUDENT',
                            'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                            'email': "teste@teste.com"
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1671315413000
                    },
                    {
                        'user': {
                            'name': 'Caio Toledo',
                            'role': 'PROFESSOR',
                            'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                            'email': "teste@teste.com"
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1671401813000
                    },
                    {
                        'user': {
                            'name': 'Pedro Marcelino',
                            'role': 'INTERNATIONAL_STUDENT',
                            'user_id': '0355573c-a110-11ed-a8fc-0242ac120002',
                            'email': "teste@teste.com"
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1671488213000
                    },
                    {
                        'user': {
                            'name': 'Hector Guerrini',
                            'role': 'EXTERNAL',
                            'user_id': '03555872-a110-11ed-a8fc-0242ac120002',
                            'email': "teste@teste.com"
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1671574613000
                    },
                    {
                        'user': {
                            'name': 'Ricardo Soller',
                            'role': 'EMPLOYEE',
                            'user_id': '2f0df47e-a110-11ed-a8fc-0242ac120002',
                            'email': "teste@teste.com"
                        },
                        'state': 'IN_QUEUE',
                        'date_subscribed': 1671574673000
                    },
                    {
                        'user': {
                            'name': 'Marcos Romanato',
                            'role': 'STUDENT',
                            'user_id': '38c3d7fe-a110-11ed-a8fc-0242ac120002',
                            'email': "teste@teste.com"
                        },
                        'state': 'IN_QUEUE',
                        'date_subscribed': 1671574733000
                    }
                ]
            },
            'message': 'the activity was retrieved by the professor'
        }
        assert expected == viewmodel.to_dict()
