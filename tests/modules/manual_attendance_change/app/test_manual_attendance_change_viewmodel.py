from src.modules.manual_attendance_change.app.manual_attendance_change_usecase import ManualAttendanceChangeUsecase
from src.modules.manual_attendance_change.app.manual_attendance_change_viewmodel import ManualAttendanceChangeViewmodel
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetActivityWithEnrollmentsViewmodel:

    def test_get_activity_with_enrollments_viewmodel(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        enrollment = repo_activity.enrollments[0]
        requester_user = repo_user.users[2]
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        activity_dict_with_enrollments = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                                 user_id=enrollment.user_id,
                                                 new_state=ENROLLMENT_STATE.COMPLETED)
        viewmodel = ManualAttendanceChangeViewmodel(activity_dict_with_enrollments)

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
                        'state': 'COMPLETED',
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
                    }
                ]
            },
            'message': 'the activity was retrieved by the professor'
        }
        assert expected == viewmodel.to_dict()

    def test_get_activity_with_enrollments_viewmodel_disconfirming(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        enrollment = repo_activity.enrollments[29]
        requester_user = repo_user.users[2]
        usecase = ManualAttendanceChangeUsecase(repo_activity=repo_activity, repo_user=repo_user)

        activity_dict_with_enrollments = usecase(code=enrollment.activity_code, requester_user=requester_user,
                                                 user_id=enrollment.user_id,
                                                 new_state=ENROLLMENT_STATE.ENROLLED)
        viewmodel = ManualAttendanceChangeViewmodel(activity_dict_with_enrollments)

        expected = {
            'activity_with_enrollments': {
                'activity': {
                    'code': 'PINOQ1',
                    'title': 'Atividade da PINOQ1',
                    'description': 'Não era a última....',
                    'activity_type': 'CULTURAL_ACTIVITY',
                    'is_extensive': False,
                    'delivery_model': 'IN_PERSON',
                    'start_date': 1670005013000,
                    'duration': 45,
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
                            'name': 'Daniel Romanato',
                            'bio': 'Buscando descobrir o mundo',
                            'company': 'Samsung'
                        },
                        {
                            'name': 'Lucas Soller',
                            'bio': 'Daora',
                            'company': 'Microsoft'
                        }
                    ],
                    'total_slots': 10,
                    'taken_slots': 4,
                    'accepting_new_enrollments': False,
                    'stop_accepting_new_enrollments_before': 1669918612000,
                    'confirmation_code': None
                },
                'enrollments': [
                    {
                        'user': {
                            'name': 'Bruno Soller',
                            'role': 'STUDENT',
                            'user_id': '0355535e-a110-11ed-a8fc-0242ac120002'
                        },
                        'state': 'COMPLETED',
                        'date_subscribed': 1668896213000
                    },
                    {
                        'user': {
                            'name': 'Caio Toledo',
                            'role': 'PROFESSOR',
                            'user_id': '03555624-a110-11ed-a8fc-0242ac120002'
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1668982612000
                    },
                    {
                        'user': {
                            'name': 'Pedro Marcelino',
                            'role': 'INTERNATIONAL_STUDENT',
                            'user_id': '0355573c-a110-11ed-a8fc-0242ac120002'
                        },
                        'state': 'COMPLETED',
                        'date_subscribed': 1669069013000
                    },
                    {
                        'user': {
                            'name': 'Hector Guerrini',
                            'role': 'EXTERNAL',
                            'user_id': '03555872-a110-11ed-a8fc-0242ac120002'
                        },
                        'state': 'ENROLLED',
                        'date_subscribed': 1669760213000
                    }
                ]
            },
            'message': 'the activity was retrieved by the professor'
        }
        assert expected == viewmodel.to_dict()
