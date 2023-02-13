from src.modules.get_all_activities_logged.app.get_all_activities_logged_usecase import GetAllActivitiesLoggedUsecase
from src.modules.get_all_activities_logged.app.get_all_activities_logged_viewmodel import GetAllActivitiesLoggedViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetAllActivitiesLoggedViewmodel:
    def test_get_all_activities_viewmodel(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        requester_user = repo_user.users[2]

        usecase = GetAllActivitiesLoggedUsecase(repo_activity)

        activities_logged = usecase(requester_user.user_id)

        viewmodel = GetAllActivitiesLoggedViewmodel(activities_logged=activities_logged)

        expected = {
            'all_activities_and_user_enrollments': [
                {
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
                        'stop_accepting_new_enrollments_before': 1671743812000,

                    },
                    'enrollment': {
                        'state': 'ENROLLED',
                        'date_subscribed': 1671401813000
                    }
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
                        'stop_accepting_new_enrollments_before': None,

                    }
                },
                {
                    'activity': {
                        'code': 'COD1468',
                        'title': 'Atividade da COD 1468',
                        'description': 'Isso definitivamente é uma atividade',
                        'activity_type': 'HIGH_IMPACT_LECTURES',
                        'is_extensive': True,
                        'delivery_model': 'ONLINE',
                        'start_date': 1671661013000,
                        'duration': 60,
                        'link': 'https://devmaua.com',
                        'place': None,
                        'responsible_professors': [
                            {
                                'name': 'Caio Toledo',
                                'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            },
                            {
                                'name': 'Patricia Santos',
                                'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002',
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
                        'total_slots': 50,
                        'taken_slots': 1,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': None,

                    }
                },
                {
                    'activity': {
                        'code': 'CODIGO',
                        'title': 'Atividade da CÓDIGO',
                        'description': 'Isso DEFINITIVAMENTE é uma atividade!',
                        'activity_type': 'TECHNICAL_VISITS',
                        'is_extensive': False,
                        'delivery_model': 'ONLINE',
                        'start_date': 1672006613000,
                        'duration': 60,
                        'link': 'https://devmaua.com',
                        'place': None,
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
                            },
                            {
                                'name': 'Lucas Soller',
                                'bio': 'Daora',
                                'company': 'Microsoft'
                            },
                            {
                                'name': 'Daniel Romanato',
                                'bio': 'Buscando descobrir o mundo',
                                'company': 'Samsung'
                            }
                        ],
                        'total_slots': 15,
                        'taken_slots': 2,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': 1671747413000,

                    }
                },
                {
                    'activity': {
                        'code': 'AC000',
                        'title': 'Atividade de competição',
                        'description': 'Isso é uma guerra',
                        'activity_type': 'ACADEMIC_COMPETITIONS',
                        'is_extensive': True,
                        'delivery_model': 'IN_PERSON',
                        'start_date': 1671661013000,
                        'duration': 190,
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
                        'total_slots': 50,
                        'taken_slots': 2,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': 1671574613000,

                    }
                },
                {
                    'activity': {
                        'code': 'ECM251',
                        'title': 'Atividade da ECM251',
                        'description': 'Se o professor chegar vai ter atividade...',
                        'activity_type': 'HACKATHON',
                        'is_extensive': False,
                        'delivery_model': 'HYBRID',
                        'start_date': 1671733013000,
                        'duration': 40,
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
                                'name': 'Daniel Romanato',
                                'bio': 'Buscando descobrir o mundo',
                                'company': 'Samsung'
                            }
                        ],
                        'total_slots': 20,
                        'taken_slots': 1,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': None,

                    }
                },
                {
                    'activity': {
                        'code': 'SC456',
                        'title': 'Atividade da SC456',
                        'description': 'Sem criatividade para descrição',
                        'activity_type': 'INTERNSHIP_FAIR',
                        'is_extensive': False,
                        'delivery_model': 'ONLINE',
                        'start_date': 1671563813000,
                        'duration': 80,
                        'link': 'https://devmaua.com',
                        'place': None,
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
                        'total_slots': 10,
                        'taken_slots': 1,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': None,

                    }
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
                        'stop_accepting_new_enrollments_before': None,

                    }
                },
                {
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
                        'total_slots': 50,
                        'taken_slots': 0,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': None,

                    }
                },
                {
                    'activity': {
                        'code': 'PRF246',
                        'title': 'Atividade da PRF246',
                        'description': 'Um único professor pra tudo',
                        'activity_type': 'CULTURAL_ACTIVITY',
                        'is_extensive': True,
                        'delivery_model': 'IN_PERSON',
                        'start_date': 1672006613000,
                        'duration': 140,
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
                        'total_slots': 50,
                        'taken_slots': 0,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': None,

                    }
                },
                {
                    'activity': {
                        'code': '2468',
                        'title': 'Atividade da 2468',
                        'description': 'Atividade com números pares',
                        'activity_type': 'GCSP',
                        'is_extensive': False,
                        'delivery_model': 'HYBRID',
                        'start_date': 1672006613000,
                        'duration': 60,
                        'link': 'https://devmaua.com',
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
                                'name': 'Lucas Soller',
                                'bio': 'Daora',
                                'company': 'Microsoft'
                            }
                        ],
                        'total_slots': 25,
                        'taken_slots': 0,
                        'accepting_new_enrollments': True,
                        'stop_accepting_new_enrollments_before': None,

                    }
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
                        'stop_accepting_new_enrollments_before': 1671733012000,
                    },
                    'enrollment': {
                        'state': 'ENROLLED',
                        'date_subscribed': 1670710614000
                    }
                },
                {
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
                                'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
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
                    },
                    'enrollment': {
                        'state': 'COMPLETED',
                        'date_subscribed': 1668982612000
                    }
                }
            ],
            'message': 'the activities were retrieved to the user'
        }

        assert viewmodel.to_dict() == expected
