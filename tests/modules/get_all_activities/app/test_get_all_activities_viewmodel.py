from src.modules.get_all_activities.app.get_all_activities_usecase import GetAllActivitiesUsecase
from src.modules.get_all_activities.app.get_all_activities_viewmodel import GetAllActivitiesViewmodel
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock

observability = ObservabilityMock(module_name="get_all_activites")

class Test_GetAllActivitiesViewmodel:
    def test_get_all_activities_viewmodel(self):
        repo = ActivityRepositoryMock()
        usecase = GetAllActivitiesUsecase(repo, observability=observability)
        all_activities = usecase()
        viewmodel = GetAllActivitiesViewmodel(all_activities)

        expected = {
            'all_activities': [{'activity': {'accepting_new_enrollments': False,
                                              'activity_type': 'CULTURAL_ACTIVITY',
                                              'code': 'PINOQ1',
                                              'delivery_model': 'IN_PERSON',
                                              'description': 'Não era a última....',
                                              'start_date': 1670005013000,
                                              'end_date': 1670007713000,
                                              'is_extensive': False,
                                              'link': None,
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Caio '
                                                                                  'Toledo',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '03555624-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Buscando descobrir o '
                                                                   'mundo',
                                                            'company': 'Samsung',
                                                            'name': 'Daniel Romanato'},
                                                           {'bio': 'Daora',
                                                            'company': 'Microsoft',
                                                            'name': 'Lucas Soller'}],
                                              'stop_accepting_new_enrollments_before': 1669918612000,
                                              'taken_slots': 4,
                                              'title': 'Atividade da PINOQ1',
                                              'total_slots': 10}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'PROFESSORS_ACADEMY',
                                              'code': 'CODE',
                                              'delivery_model': 'HYBRID',
                                              'description': 'O mesmo speaker pela 50° vez',
                                              'start_date': 1671488213000,
                                              'end_date': 1671495413000,
                                              'is_extensive': True,
                                              'link': 'https://devmaua.com',
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Caio '
                                                                                  'Toledo',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '03555624-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Buscando descobrir o '
                                                                   'mundo',
                                                            'company': 'Samsung',
                                                            'name': 'Daniel Romanato'}],
                                              'stop_accepting_new_enrollments_before': None,
                                              'taken_slots': 0,
                                              'title': 'Atividade da CODE',
                                              'total_slots': 50}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'INTERNSHIP_FAIR',
                                              'code': 'SC456',
                                              'delivery_model': 'ONLINE',
                                              'description': 'Sem criatividade para '
                                                             'descrição',
                                              'start_date': 1671563813000,
                                              'end_date': 1671568613000,
                                              'is_extensive': False,
                                              'link': 'https://devmaua.com',
                                              'place': None,
                                              'responsible_professors': [{'name': 'Caio '
                                                                                  'Toledo',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '03555624-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Incrível',
                                                            'company': 'Apple',
                                                            'name': 'Vitor Briquez'}],
                                              'stop_accepting_new_enrollments_before': None,
                                              'taken_slots': 1,
                                              'title': 'Atividade da SC456',
                                              'total_slots': 10}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'LECTURES',
                                              'code': 'ELET355',
                                              'delivery_model': 'HYBRID',
                                              'description': 'Isso é uma atividade, sério.',
                                              'start_date': 1671661013000,
                                              'end_date': 1695661013000,
                                              'is_extensive': True,
                                              'link': 'https://devmaua.com',
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Patricia '
                                                                                  'Santos',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Daora',
                                                            'company': 'Microsoft',
                                                            'name': 'Lucas Soller'}],
                                              'stop_accepting_new_enrollments_before': None,
                                              'taken_slots': 1,
                                              'title': 'Atividade da ELET 355',
                                              'total_slots': 10}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'HIGH_IMPACT_LECTURES',
                                              'code': 'COD1468',
                                              'delivery_model': 'ONLINE',
                                              'description': 'Isso definitivamente é uma '
                                                             'atividade',
                                              'start_date': 1671661013000,
                                              'end_date': 1671664613000,
                                              'is_extensive': True,
                                              'link': 'https://devmaua.com',
                                              'place': None,
                                              'responsible_professors': [{'name': 'Caio '
                                                                                  'Toledo',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '03555624-a110-11ed-a8fc-0242ac120002'},
                                                                         {'name': 'Patricia '
                                                                                  'Santos',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Buscando descobrir o '
                                                                   'mundo',
                                                            'company': 'Samsung',
                                                            'name': 'Daniel Romanato'}],
                                              'stop_accepting_new_enrollments_before': None,
                                              'taken_slots': 1,
                                              'title': 'Atividade da COD 1468',
                                              'total_slots': 50}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'ACADEMIC_COMPETITIONS',
                                              'code': 'AC000',
                                              'delivery_model': 'IN_PERSON',
                                              'description': 'Isso é uma guerra',
                                              'start_date': 1671661013000,
                                              'end_date': 1671672413000,
                                              'is_extensive': True,
                                              'link': None,
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Patricia '
                                                                                  'Santos',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Daora',
                                                            'company': 'Microsoft',
                                                            'name': 'Lucas Soller'}],
                                              'stop_accepting_new_enrollments_before': 1671574613000,
                                              'taken_slots': 2,
                                              'title': 'Atividade de competição',
                                              'total_slots': 50}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'ALUMNI_CAFE',
                                              'code': 'CAFE',
                                              'delivery_model': 'IN_PERSON',
                                              'description': 'Atividade pra tomar café',
                                              'start_date': 1671661013000,
                                              'end_date': 1671662213000,
                                              'is_extensive': True,
                                              'link': None,
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Patricia '
                                                                                  'Santos',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Daora',
                                                            'company': 'Microsoft',
                                                            'name': 'Lucas Soller'}],
                                              'stop_accepting_new_enrollments_before': None,
                                              'taken_slots': 2,
                                              'title': 'Atividade da CAFE',
                                              'total_slots': 2}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'HACKATHON',
                                              'code': 'ECM251',
                                              'delivery_model': 'HYBRID',
                                              'description': 'Se o professor chegar vai '
                                                             'ter atividade...',
                                              'start_date': 1671733013000,
                                              'end_date': 1671735413000,
                                              'is_extensive': False,
                                              'link': 'https://devmaua.com',
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Patricia '
                                                                                  'Santos',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Buscando descobrir o '
                                                                   'mundo',
                                                            'company': 'Samsung',
                                                            'name': 'Daniel Romanato'}],
                                              'stop_accepting_new_enrollments_before': None,
                                              'taken_slots': 1,
                                              'title': 'Atividade da ECM251',
                                              'total_slots': 20}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'SPORTS_ACTIVITY',
                                              'code': 'ULTIMA',
                                              'delivery_model': 'IN_PERSON',
                                              'description': 'Atividade pra acabar',
                                              'start_date': 1671733013000,
                                              'end_date': 1671735713000,
                                              'is_extensive': False,
                                              'link': None,
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Caio '
                                                                                  'Toledo',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '03555624-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Buscando descobrir o '
                                                                   'mundo',
                                                            'company': 'Samsung',
                                                            'name': 'Daniel Romanato'}],
                                              'stop_accepting_new_enrollments_before': 1671733012000,
                                              'taken_slots': 3,
                                              'title': 'Última atividade',
                                              'total_slots': 3}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'COURSES',
                                              'code': 'ECM2345',
                                              'delivery_model': 'IN_PERSON',
                                              'description': 'Isso é uma atividade',
                                              'start_date': 1671747413000,
                                              'end_date': 1671754613000,
                                              'is_extensive': False,
                                              'link': None,
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Caio '
                                                                                  'Toledo',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '03555624-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Incrível',
                                                            'company': 'Apple',
                                                            'name': 'Vitor Briquez'}],
                                              'stop_accepting_new_enrollments_before': 1671743812000,
                                              'taken_slots': 4,
                                              'title': 'Atividade da ECM 2345',
                                              'total_slots': 4}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'TECHNICAL_VISITS',
                                              'code': 'CODIGO',
                                              'delivery_model': 'ONLINE',
                                              'description': 'Isso DEFINITIVAMENTE é uma '
                                                             'atividade!',
                                              'start_date': 1672006613000,
                                              'end_date': 1672010213000,
                                              'is_extensive': False,
                                              'link': 'https://devmaua.com',
                                              'place': None,
                                              'responsible_professors': [{'name': 'Caio '
                                                                                  'Toledo',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '03555624-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Incrível',
                                                            'company': 'Apple',
                                                            'name': 'Vitor Briquez'},
                                                           {'bio': 'Daora',
                                                            'company': 'Microsoft',
                                                            'name': 'Lucas Soller'},
                                                           {'bio': 'Buscando descobrir o '
                                                                   'mundo',
                                                            'company': 'Samsung',
                                                            'name': 'Daniel Romanato'}],
                                              'stop_accepting_new_enrollments_before': 1671747413000,
                                              'taken_slots': 2,
                                              'title': 'Atividade da CÓDIGO',
                                              'total_slots': 15}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'CULTURAL_ACTIVITY',
                                              'code': 'PRF246',
                                              'delivery_model': 'IN_PERSON',
                                              'description': 'Um único professor pra tudo',
                                              'start_date': 1672006613000,
                                              'end_date': 1672015013000,
                                              'is_extensive': True,
                                              'link': None,
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Caio '
                                                                                  'Toledo',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '03555624-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Incrível',
                                                            'company': 'Apple',
                                                            'name': 'Vitor Briquez'}],
                                              'stop_accepting_new_enrollments_before': None,
                                              'taken_slots': 0,
                                              'title': 'Atividade da PRF246',
                                              'total_slots': 50}},
                                {'activity': {'accepting_new_enrollments': True,
                                              'activity_type': 'GCSP',
                                              'code': '2468',
                                              'delivery_model': 'HYBRID',
                                              'description': 'Atividade com números pares',
                                              'start_date': 1672006613000,
                                              'end_date': 1672010213000,
                                              'is_extensive': False,
                                              'link': 'https://devmaua.com',
                                              'place': 'H332',
                                              'responsible_professors': [{'name': 'Caio '
                                                                                  'Toledo',
                                                                          'role': 'PROFESSOR',
                                                                          'user_id': '03555624-a110-11ed-a8fc-0242ac120002'}],
                                              'speakers': [{'bio': 'Daora',
                                                            'company': 'Microsoft',
                                                            'name': 'Lucas Soller'}],
                                              'stop_accepting_new_enrollments_before': None,
                                              'taken_slots': 0,
                                              'title': 'Atividade da 2468',
                                              'total_slots': 25}}],
             'message': 'the activities were retrieved'

        }
        assert viewmodel.to_dict() == expected
