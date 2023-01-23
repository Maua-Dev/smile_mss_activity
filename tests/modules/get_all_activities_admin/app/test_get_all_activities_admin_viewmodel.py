from src.modules.get_all_activities_admin.app.get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from src.modules.get_all_activities_admin.app.get_all_activities_admin_viewmodel import GetAllActivitiesAdminViewmodel
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_GetAllActivitiesAdminViewmodel:
    def test_get_all_activities_admin_viewmodel(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesAdminUsecase(repo)
        all_activities_with_enrollments = usecase()
        viewmodel = GetAllActivitiesAdminViewmodel(all_activities_with_enrollments)

        expected = {
                   "all_activities_with_enrollments": [
                      {
                         "code": "ECM2345",
                         "title": "Atividade da ECM 2345",
                         "description": "Isso é uma atividade",
                         "activity_type": "COURSE",
                         "is_extensive": False,
                         "delivery_model": "IN_PERSON",
                         "start_date": "2022-12-22T19:16:52.998305",
                         "duration": 120,
                         "link": None,
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Caio Toledo",
                               "user_id": "d7f1",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Vitor Briquez",
                               "bio": "Incrível",
                               "company": "Apple"
                            }
                         ],
                         "total_slots": 4,
                         "taken_slots": 4,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": "2022-12-22T18:16:52.998305",
                         "enrollments": [
                            {
                               "user": {
                                  "name": "João Vilas",
                                  "user_id": "db43",
                                  "role": "ADMIN"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-16T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Bruno Soller",
                                  "user_id": "b16f",
                                  "role": "STUDENT"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-17T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Caio Toledo",
                                  "user_id": "d7f1",
                                  "role": "PROFESSOR"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-18T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Pedro Marcelino",
                                  "user_id": "80fb",
                                  "role": "INTERNATIONAL_STUDENT"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Hector Guerrini",
                                  "user_id": "9257",
                                  "role": "EXTERNAL"
                               },
                               "state": "IN_QUEUE",
                               "date_subscribed": "2022-12-20T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Ricardo Soller",
                                  "user_id": "f664",
                                  "role": "EMPLOYEE"
                               },
                               "state": "IN_QUEUE",
                               "date_subscribed": "2022-12-20T19:17:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Marcos Romanato",
                                  "user_id": "bea2",
                                  "role": "STUDENT"
                               },
                               "state": "IN_QUEUE",
                               "date_subscribed": "2022-12-20T19:18:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "ELET355",
                         "title": "Atividade da ELET 355",
                         "description": "Isso é uma atividade, sério.",
                         "activity_type": "LECTURES",
                         "is_extensive": True,
                         "delivery_model": "HYBRID",
                         "start_date": "2022-12-21T19:16:52.998305",
                         "duration": 400,
                         "link": "https://devmaua.com",
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Patricia Santos",
                               "user_id": "c695",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Lucas Soller",
                               "bio": "Daora",
                               "company": "Microsoft"
                            }
                         ],
                         "total_slots": 10,
                         "taken_slots": 1,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": None,
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Bruno Soller",
                                  "user_id": "b16f",
                                  "role": "STUDENT"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "COD1468",
                         "title": "Atividade da COD 1468",
                         "description": "Isso definitivamente é uma atividade",
                         "activity_type": "HIGH_IMPACT_LECTURES",
                         "is_extensive": True,
                         "delivery_model": "ONLINE",
                         "start_date": "2022-12-21T19:16:52.998305",
                         "duration": 60,
                         "link": "https://devmaua.com",
                         "place": None,
                         "responsible_professors": [
                            {
                               "name": "Caio Toledo",
                               "user_id": "d7f1",
                               "role": "PROFESSOR"
                            },
                            {
                               "name": "Patricia Santos",
                               "user_id": "c695",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Daniel Romanato",
                               "bio": "Buscando descobrir o mundo",
                               "company": "Samsung"
                            }
                         ],
                         "total_slots": 50,
                         "taken_slots": 1,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": None,
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Pedro Marcelino",
                                  "user_id": "80fb",
                                  "role": "INTERNATIONAL_STUDENT"
                               },
                               "state": "DROPPED",
                               "date_subscribed": "2022-12-19T19:16:51.998305"
                            },
                            {
                               "user": {
                                  "name": "Hector Guerrini",
                                  "user_id": "9257",
                                  "role": "EXTERNAL"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "CODIGO",
                         "title": "Atividade da CÓDIGO",
                         "description": "Isso DEFINITIVAMENTE é uma atividade!",
                         "activity_type": "TECHNICAL_VISITS",
                         "is_extensive": False,
                         "delivery_model": "ONLINE",
                         "start_date": "2022-12-25T19:16:52.998305",
                         "duration": 60,
                         "link": "https://devmaua.com",
                         "place": None,
                         "responsible_professors": [
                            {
                               "name": "Caio Toledo",
                               "user_id": "d7f1",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Vitor Briquez",
                               "bio": "Incrível",
                               "company": "Apple"
                            },
                            {
                               "name": "Lucas Soller",
                               "bio": "Daora",
                               "company": "Microsoft"
                            },
                            {
                               "name": "Daniel Romanato",
                               "bio": "Buscando descobrir o mundo",
                               "company": "Samsung"
                            }
                         ],
                         "total_slots": 15,
                         "taken_slots": 2,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": "2022-12-22T19:16:52.998305",
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Hector Guerrini",
                                  "user_id": "9257",
                                  "role": "EXTERNAL"
                               },
                               "state": "REJECTED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Ricardo Soller",
                                  "user_id": "f664",
                                  "role": "EMPLOYEE"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-20T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Marcos Romanato",
                                  "user_id": "bea2",
                                  "role": "STUDENT"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-21T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "AC000",
                         "title": "Atividade de competição",
                         "description": "Isso é uma guerra",
                         "activity_type": "ACADEMIC_COMPETITIONS",
                         "is_extensive": True,
                         "delivery_model": "IN_PERSON",
                         "start_date": "2022-12-21T19:16:52.998305",
                         "duration": 190,
                         "link": None,
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Patricia Santos",
                               "user_id": "c695",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Lucas Soller",
                               "bio": "Daora",
                               "company": "Microsoft"
                            }
                         ],
                         "total_slots": 50,
                         "taken_slots": 2,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": "2022-12-20T19:16:52.998305",
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Ricardo Soller",
                                  "user_id": "f664",
                                  "role": "EMPLOYEE"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-19T17:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Marcos Romanato",
                                  "user_id": "bea2",
                                  "role": "STUDENT"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "ECM251",
                         "title": "Atividade da ECM251",
                         "description": "Se o professor chegar vai ter atividade...",
                         "activity_type": "HACKATHON",
                         "is_extensive": False,
                         "delivery_model": "HYBRID",
                         "start_date": "2022-12-22T15:16:52.998305",
                         "duration": 40,
                         "link": "https://devmaua.com",
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Patricia Santos",
                               "user_id": "c695",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Daniel Romanato",
                               "bio": "Buscando descobrir o mundo",
                               "company": "Samsung"
                            }
                         ],
                         "total_slots": 20,
                         "taken_slots": 1,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": None,
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Marcos Romanato",
                                  "user_id": "bea2",
                                  "role": "STUDENT"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "SC456",
                         "title": "Atividade da SC456",
                         "description": "Sem criatividade para descrição",
                         "activity_type": "INTERNSHIP_FAIR",
                         "is_extensive": False,
                         "delivery_model": "ONLINE",
                         "start_date": "2022-12-20T16:16:52.998305",
                         "duration": 80,
                         "link": "https://devmaua.com",
                         "place": None,
                         "responsible_professors": [
                            {
                               "name": "Caio Toledo",
                               "user_id": "d7f1",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Vitor Briquez",
                               "bio": "Incrível",
                               "company": "Apple"
                            }
                         ],
                         "total_slots": 10,
                         "taken_slots": 1,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": None,
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Marco Briquez",
                                  "user_id": "f26f",
                                  "role": "STUDENT"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "CAFE",
                         "title": "Atividade da CAFE",
                         "description": "Atividade pra tomar café",
                         "activity_type": "ALUMNI_CAFE",
                         "is_extensive": True,
                         "delivery_model": "IN_PERSON",
                         "start_date": "2022-12-21T19:16:52.998305",
                         "duration": 20,
                         "link": None,
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Patricia Santos",
                               "user_id": "c695",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Lucas Soller",
                               "bio": "Daora",
                               "company": "Microsoft"
                            }
                         ],
                         "total_slots": 2,
                         "taken_slots": 2,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": None,
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Simone Romanato",
                                  "user_id": "d23a",
                                  "role": "EXTERNAL"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-18T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Bruno Soller",
                                  "user_id": "b16f",
                                  "role": "STUDENT"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Caio Toledo",
                                  "user_id": "d7f1",
                                  "role": "PROFESSOR"
                               },
                               "state": "DROPPED",
                               "date_subscribed": "2022-12-20T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "CODE",
                         "title": "Atividade da CODE",
                         "description": "O mesmo speaker pela 50° vez",
                         "activity_type": "PROFESSORS_ACADEMY",
                         "is_extensive": True,
                         "delivery_model": "HYBRID",
                         "start_date": "2022-12-19T19:16:52.998305",
                         "duration": 120,
                         "link": "https://devmaua.com",
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Caio Toledo",
                               "user_id": "d7f1",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Daniel Romanato",
                               "bio": "Buscando descobrir o mundo",
                               "company": "Samsung"
                            }
                         ],
                         "total_slots": 50,
                         "taken_slots": 0,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": None,
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Viviani Soller",
                                  "user_id": "d673",
                                  "role": "EXTERNAL"
                               },
                               "state": "DROPPED",
                               "date_subscribed": "2022-12-17T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "PRF246",
                         "title": "Atividade da PRF246",
                         "description": "Um único professor pra tudo",
                         "activity_type": "CULTURAL_ACTIVITY",
                         "is_extensive": True,
                         "delivery_model": "IN_PERSON",
                         "start_date": "2022-12-25T19:16:52.998305",
                         "duration": 140,
                         "link": None,
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Caio Toledo",
                               "user_id": "d7f1",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Vitor Briquez",
                               "bio": "Incrível",
                               "company": "Apple"
                            }
                         ],
                         "total_slots": 50,
                         "taken_slots": 0,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": None,
                         "enrollments": [
                            {
                               "user": {
                                  "name": "João Vilas",
                                  "user_id": "db43",
                                  "role": "ADMIN"
                               },
                               "state": "DROPPED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "2468",
                         "title": "Atividade da 2468",
                         "description": "Atividade com números pares",
                         "activity_type": "GCSP",
                         "is_extensive": False,
                         "delivery_model": "HYBRID",
                         "start_date": "2022-12-25T19:16:52.998305",
                         "duration": 60,
                         "link": "https://devmaua.com",
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Caio Toledo",
                               "user_id": "d7f1",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Lucas Soller",
                               "bio": "Daora",
                               "company": "Microsoft"
                            }
                         ],
                         "total_slots": 25,
                         "taken_slots": 0,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": None,
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Bruno Soller",
                                  "user_id": "b16f",
                                  "role": "STUDENT"
                               },
                               "state": "DROPPED",
                               "date_subscribed": "2022-12-19T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "ULTIMA",
                         "title": "Última atividade",
                         "description": "Atividade pra acabar",
                         "activity_type": "SPORTS_ACTIVITY",
                         "is_extensive": False,
                         "delivery_model": "IN_PERSON",
                         "start_date": "2022-12-22T15:16:52.998305",
                         "duration": 45,
                         "link": None,
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Caio Toledo",
                               "user_id": "d7f1",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Daniel Romanato",
                               "bio": "Buscando descobrir o mundo",
                               "company": "Samsung"
                            }
                         ],
                         "total_slots": 3,
                         "taken_slots": 3,
                         "accepting_new_enrollments": True,
                         "stop_accepting_new_enrollments_before": "2022-12-22T15:16:51.998305",
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Bruno Soller",
                                  "user_id": "b16f",
                                  "role": "STUDENT"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-10T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Caio Toledo",
                                  "user_id": "d7f1",
                                  "role": "PROFESSOR"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-11T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Pedro Marcelino",
                                  "user_id": "80fb",
                                  "role": "INTERNATIONAL_STUDENT"
                               },
                               "state": "DROPPED",
                               "date_subscribed": "2022-12-12T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Ricardo Soller",
                                  "user_id": "f664",
                                  "role": "EMPLOYEE"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-12-13T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Hector Guerrini",
                                  "user_id": "9257",
                                  "role": "EXTERNAL"
                               },
                               "state": "IN_QUEUE",
                               "date_subscribed": "2022-12-21T19:16:52.998305"
                            }
                         ]
                      },
                      {
                         "code": "PINOQ1",
                         "title": "Atividade da PINOQ1",
                         "description": "Não era a última....",
                         "activity_type": "CULTURAL_ACTIVITY",
                         "is_extensive": False,
                         "delivery_model": "IN_PERSON",
                         "start_date": "2022-12-02T15:16:52.998305",
                         "duration": 45,
                         "link": None,
                         "place": "H332",
                         "responsible_professors": [
                            {
                               "name": "Caio Toledo",
                               "user_id": "d7f1",
                               "role": "PROFESSOR"
                            }
                         ],
                         "speakers": [
                            {
                               "name": "Daniel Romanato",
                               "bio": "Buscando descobrir o mundo",
                               "company": "Samsung"
                            },
                            {
                               "name": "Lucas Soller",
                               "bio": "Daora",
                               "company": "Microsoft"
                            }
                         ],
                         "total_slots": 10,
                         "taken_slots": 4,
                         "accepting_new_enrollments": False,
                         "stop_accepting_new_enrollments_before": "2022-12-01T15:16:51.998305",
                         "enrollments": [
                            {
                               "user": {
                                  "name": "Bruno Soller",
                                  "user_id": "b16f",
                                  "role": "STUDENT"
                               },
                               "state": "COMPLETED",
                               "date_subscribed": "2022-11-19T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Caio Toledo",
                                  "user_id": "d7f1",
                                  "role": "PROFESSOR"
                               },
                               "state": "COMPLETED",
                               "date_subscribed": "2022-11-20T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Pedro Marcelino",
                                  "user_id": "80fb",
                                  "role": "INTERNATIONAL_STUDENT"
                               },
                               "state": "COMPLETED",
                               "date_subscribed": "2022-11-21T19:16:52.998305"
                            },
                            {
                               "user": {
                                  "name": "Hector Guerrini",
                                  "user_id": "9257",
                                  "role": "EXTERNAL"
                               },
                               "state": "ENROLLED",
                               "date_subscribed": "2022-11-29T19:16:52.998305"
                            }
                         ]
                      }
                   ],
                   "message": "the activities were retrieved by admin"
                }

        assert viewmodel.to_dict() == expected
