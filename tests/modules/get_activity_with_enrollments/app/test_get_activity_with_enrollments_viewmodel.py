from src.modules.get_activity_with_enrollments.app.get_activity_with_enrollments_usecase import \
    GetActivityWithEnrollmentsUsecase
from src.modules.get_activity_with_enrollments.app.get_activity_with_enrollments_viewmodel import \
    GetActivityWithEnrollmentsViewmodel
from src.shared.infra.repositories.activity_repository_mock \
    import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetActivityWithEnrollmentsViewmodel:

    def test_get_activity_with_enrollments_viewmodel(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        activity_with_enrollments = usecase(user=repo_user.users[2], code=repo_activity.activities[0].code)
        viewmodel = GetActivityWithEnrollmentsViewmodel(activity_with_enrollments)

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
                    'duration': 120,
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
                            'name': 'João Vilas',
                            'role': 'ADMIN',
                            'user_id': 'd61dbf66-a10f-11ed-a8fc-0242ac120002'
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1671229013000
                    },
                    {
                        'user': {
                            'name': 'Bruno Soller',
                            'role': 'STUDENT',
                            'user_id': '0355535e-a110-11ed-a8fc-0242ac120002'
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1671315413000
                    },
                    {
                        'user': {
                            'name': 'Caio Toledo',
                            'role': 'PROFESSOR',
                            'user_id': '03555624-a110-11ed-a8fc-0242ac120002'
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1671401813000
                    },
                    {
                        'user': {
                            'name': 'Pedro Marcelino',
                            'role': 'INTERNATIONAL_STUDENT',
                            'user_id': '0355573c-a110-11ed-a8fc-0242ac120002'
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1671488213000
                    },
                ]
            },
            'message': 'the activity was retrieved by the professor'
        }
        assert expected == viewmodel.to_dict()
    def test_get_activity_with_enrollments_viewmodel_no_slots_taken(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivityWithEnrollmentsUsecase(repo_activity=repo_activity, repo_user=repo_user)
        activity_with_enrollments = usecase(user=repo_user.users[2], code=repo_activity.activities[8].code)
        viewmodel = GetActivityWithEnrollmentsViewmodel(activity_with_enrollments)

        expected = {
            'activity_with_enrollments': {
                'activity': {
                    'code': 'CODE',
                    'title': 'Atividade da CODE',
                    'description': 'O mesmo speaker pela 50° vez',
                    'activity_type': 'PROFESSORS_ACADEMY',
                    'is_extensive': True,
                    'delivery_model': 'HYBRID',
                    'start_date': 1671488213000,
                    'duration': 120,
                    'link': 'https://devmaua.com',
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
                            'name': 'Daniel Romanato',
                            'bio': 'Buscando descobrir o mundo',
                            'company': 'Samsung'
                        }
                    ],
                    'total_slots': 50,
                    'taken_slots': 0,
                    'accepting_new_enrollments': True,
                    'stop_accepting_new_enrollments_before': None,
                    'confirmation_code': None
                },
                'enrollments': [

                ]
            },
            'message': 'the activity was retrieved by the professor'
        }
        assert expected == viewmodel.to_dict()