from src.modules.get_activities_responsible_professor.app.get_activities_responsible_professor_usecase import \
    GetActivitiesResponsibleProfessorUsecase
from src.modules.get_activities_responsible_professor.app.get_activities_responsible_professor_viewmodel import \
    GetActivitiesResponsibleProfessorViewmodel
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_GetActivitiesResponsibleProfessorViewModel:
    def test_get_activities_responsible_professor_viewmodel(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)

        requester_user = repo_user.users[2]

        specific_professor_activities_with_enrollments_dict = usecase(requester_user)

        viewmodel = GetActivitiesResponsibleProfessorViewmodel(specific_professor_activities_with_enrollments_dict)

        expected = {
            'specific_professor_activities_with_enrollments': [
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'João Vilas',
                                'user_id': 'd61dbf66-a10f-11ed-a8fc-0242ac120002',
                                'role': 'ADMIN'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671229013000
                        },
                        {
                            'user': {
                                'name': 'Bruno Soller',
                                'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671315413000
                        },
                        {
                            'user': {
                                'name': 'Caio Toledo',
                                'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671401813000
                        },
                        {
                            'user': {
                                'name': 'Pedro Marcelino',
                                'user_id': '0355573c-a110-11ed-a8fc-0242ac120002',
                                'role': 'INTERNATIONAL_STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671488213000
                        },
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Hector Guerrini',
                                'user_id': '03555872-a110-11ed-a8fc-0242ac120002',
                                'role': 'EXTERNAL'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671488213000
                        }
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Ricardo Soller',
                                'user_id': '2f0df47e-a110-11ed-a8fc-0242ac120002',
                                'role': 'EMPLOYEE'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671574613000
                        },
                        {
                            'user': {
                                'name': 'Marcos Romanato',
                                'user_id': '38c3d7fe-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671661013000
                        }
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Marco Briquez',
                                'user_id': '452a5f9a-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671488213000
                        }
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [

                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [

                    ]
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
                        'confirmation_code': '555666'
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Bruno Soller',
                                'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1670710613000
                        },
                        {
                            'user': {
                                'name': 'Caio Toledo',
                                'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1670710614000
                        },
                        {
                            'user': {
                                'name': 'Ricardo Soller',
                                'user_id': '2f0df47e-a110-11ed-a8fc-0242ac120002',
                                'role': 'EMPLOYEE'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1670710616000
                        },
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Bruno Soller',
                                'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'COMPLETED',
                            'date_subscribed': 1668896213000
                        },
                        {
                            'user': {
                                'name': 'Caio Toledo',
                                'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            },
                            'state': 'COMPLETED',
                            'date_subscribed': 1668982612000
                        },
                        {
                            'user': {
                                'name': 'Pedro Marcelino',
                                'user_id': '0355573c-a110-11ed-a8fc-0242ac120002',
                                'role': 'INTERNATIONAL_STUDENT'
                            },
                            'state': 'COMPLETED',
                            'date_subscribed': 1669069013000
                        },
                        {
                            'user': {
                                'name': 'Hector Guerrini',
                                'user_id': '03555872-a110-11ed-a8fc-0242ac120002',
                                'role': 'EXTERNAL'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1669760213000
                        }
                    ]
                }
            ],
            'message': 'the activities were retrieved to responsible professor'
        }

        assert viewmodel.to_dict() == expected

    def test_get_activities_responsible_professor_viewmodel_no_items(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)

        requester_user = repo_user.users[12]

        specific_professor_activities_with_enrollments_dict = usecase(requester_user)

        viewmodel = GetActivitiesResponsibleProfessorViewmodel(specific_professor_activities_with_enrollments_dict)

        expected = {
            'specific_professor_activities_with_enrollments': [],
            'message': 'the activities were retrieved to responsible professor'
        }

        assert viewmodel.to_dict() == expected

    def test_get_activities_responsible_professor_viewmodel_no_user_found(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)

        fake_enrollment = Enrollment(
            user_id="invalid_user_id",
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed = 1675947866400,
            activity_code=repo_activity.activities[0].code
        )
        repo_activity.enrollments.append(fake_enrollment)
        requester_user = repo_user.users[2]

        specific_professor_activities_with_enrollments_dict = usecase(requester_user)

        viewmodel = GetActivitiesResponsibleProfessorViewmodel(specific_professor_activities_with_enrollments_dict)

        expected = {
            'specific_professor_activities_with_enrollments': [
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'João Vilas',
                                'user_id': 'd61dbf66-a10f-11ed-a8fc-0242ac120002',
                                'role': 'ADMIN'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671229013000
                        },
                        {
                            'user': {
                                'name': 'Bruno Soller',
                                'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671315413000
                        },
                        {
                            'user': {
                                'name': 'Caio Toledo',
                                'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671401813000
                        },
                        {
                            'user': {
                                'name': 'Pedro Marcelino',
                                'user_id': '0355573c-a110-11ed-a8fc-0242ac120002',
                                'role': 'INTERNATIONAL_STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671488213000
                        },
                        {
                            'user': {
                                'name': 'NOT_FOUND',
                                'user_id': 'NOT_FOUND',
                                'role': 'NOT_FOUND'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1675947866400
                        }
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Hector Guerrini',
                                'user_id': '03555872-a110-11ed-a8fc-0242ac120002',
                                'role': 'EXTERNAL'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671488213000
                        }
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Ricardo Soller',
                                'user_id': '2f0df47e-a110-11ed-a8fc-0242ac120002',
                                'role': 'EMPLOYEE'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671574613000
                        },
                        {
                            'user': {
                                'name': 'Marcos Romanato',
                                'user_id': '38c3d7fe-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671661013000
                        }
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Marco Briquez',
                                'user_id': '452a5f9a-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1671488213000
                        }
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [

                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [

                    ]
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
                        'confirmation_code': '555666'
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Bruno Soller',
                                'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1670710613000
                        },
                        {
                            'user': {
                                'name': 'Caio Toledo',
                                'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1670710614000
                        },
                        {
                            'user': {
                                'name': 'Ricardo Soller',
                                'user_id': '2f0df47e-a110-11ed-a8fc-0242ac120002',
                                'role': 'EMPLOYEE'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1670710616000
                        },
                    ]
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
                        'confirmation_code': None
                    },
                    'enrollments': [
                        {
                            'user': {
                                'name': 'Bruno Soller',
                                'user_id': '0355535e-a110-11ed-a8fc-0242ac120002',
                                'role': 'STUDENT'
                            },
                            'state': 'COMPLETED',
                            'date_subscribed': 1668896213000
                        },
                        {
                            'user': {
                                'name': 'Caio Toledo',
                                'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                                'role': 'PROFESSOR'
                            },
                            'state': 'COMPLETED',
                            'date_subscribed': 1668982612000
                        },
                        {
                            'user': {
                                'name': 'Pedro Marcelino',
                                'user_id': '0355573c-a110-11ed-a8fc-0242ac120002',
                                'role': 'INTERNATIONAL_STUDENT'
                            },
                            'state': 'COMPLETED',
                            'date_subscribed': 1669069013000
                        },
                        {
                            'user': {
                                'name': 'Hector Guerrini',
                                'user_id': '03555872-a110-11ed-a8fc-0242ac120002',
                                'role': 'EXTERNAL'
                            },
                            'state': 'ENROLLED',
                            'date_subscribed': 1669760213000
                        }
                    ]
                }
            ],
            'message': 'the activities were retrieved to responsible professor'
        }

        assert viewmodel.to_dict() == expected
