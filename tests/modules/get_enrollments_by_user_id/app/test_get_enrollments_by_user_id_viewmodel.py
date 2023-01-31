from src.modules.get_enrollments_by_user_id.app.get_enrollments_by_user_id_usecase import GetEnrollmentsByUserIdUsecase
from src.modules.get_enrollments_by_user_id.app.get_enrollments_by_user_id_viewmodel import \
    GetEnrollmentsByUserIdViewModel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetEnrollmentsByUserId:

    def test_get_enrollments_by_user_id_viewmodel(self):
        repo = ActivityRepositoryMock()
        usecase = GetEnrollmentsByUserIdUsecase(repo)

        list_enrollments = usecase(user_id=repo.users[1].user_id)

        viewmodel = GetEnrollmentsByUserIdViewModel(list_enrollments)

        expected = {
            'enrollments': [
                {
                    'activity': {
                        'code': 'ECM2345',
                        'title': 'Atividade da ECM 2345',
                        'description': 'Isso é uma atividade',
                        'activity_type': 'COURSE',
                        'is_extensive': False,
                        'delivery_model': 'IN_PERSON',
                        'start_date': 1671747413000,
                        'duration': 120,
                        'link': None,
                        'place': 'H332',
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
                        'stop_accepting_new_enrollments_before': 1671743812000
                    },
                    'user': {
                        'name': 'Bruno Soller',
                        'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                        'role': 'STUDENT'
                    },
                    'state': 'ENROLLED',
                    'date_subscribed': 1671315413000
                },
                {
                    'activity': {
                        'code': 'ELET355',
                        'title': 'Atividade da ELET 355',
                        'description': 'Isso é uma atividade, sério.',
                        'activity_type': 'LECTURES',
                        'is_extensive': True,
                        'delivery_model': 'HYBRID',
                        'start_date': 1671661013000,
                        'duration': 400,
                        'link': 'https://devmaua.com',
                        'place': 'H332',
                        'responsible_professors': [
                            {
                                'name': 'Patricia Santos',
                                'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            }
                        ],
                        'speakers': [
                            {
                                'name': 'Lucas Soller',
                                'bio': 'Daora',
                                'company': 'Microsoft'
                            }
                        ],
                        'total_slots': 10,
                        'taken_slots': 1,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': None
                    },
                    'user': {
                        'name': 'Bruno Soller',
                        'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                        'role': 'STUDENT'
                    },
                    'state': 'ENROLLED',
                    'date_subscribed': 1671488213000
                },
                {
                    'activity': {
                        'code': 'CAFE',
                        'title': 'Atividade da CAFE',
                        'description': 'Atividade pra tomar café',
                        'activity_type': 'ALUMNI_CAFE',
                        'is_extensive': True,
                        'delivery_model': 'IN_PERSON',
                        'start_date': 1671661013000,
                        'duration': 20,
                        'link': None,
                        'place': 'H332',
                        'responsible_professors': [
                            {
                                'name': 'Patricia Santos',
                                'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            }
                        ],
                        'speakers': [
                            {
                                'name': 'Lucas Soller',
                                'bio': 'Daora',
                                'company': 'Microsoft'
                            }
                        ],
                        'total_slots': 2,
                        'taken_slots': 2,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': None
                    },
                    'user': {
                        'name': 'Bruno Soller',
                        'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                        'role': 'STUDENT'
                    },
                    'state': 'ENROLLED',
                    'date_subscribed': 1671488213000
                },
                {
                    'activity': {
                        'code': 'ULTIMA',
                        'title': 'Última atividade',
                        'description': 'Atividade pra acabar',
                        'activity_type': 'SPORTS_ACTIVITY',
                        'is_extensive': False,
                        'delivery_model': 'IN_PERSON',
                        'start_date': 1671733013000,
                        'duration': 45,
                        'link': None,
                        'place': 'H332',
                        'responsible_professors': [
                            {
                                'name': 'Caio Toledo',
                                'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            }
                        ],
                        'speakers': [
                            {
                                'name': 'Daniel Romanato',
                                'bio': 'Buscando descobrir o mundo',
                                'company': 'Samsung'
                            }
                        ],
                        'total_slots': 3,
                        'taken_slots': 3,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': 1671733012000
                    },
                    'user': {
                        'name': 'Bruno Soller',
                        'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                        'role': 'STUDENT'
                    },
                    'state': 'ENROLLED',
                    'date_subscribed': 1670710613000
                }
            ],
            'message': "the emrollments were retrieved"
        }

        assert viewmodel.to_dict() == expected
