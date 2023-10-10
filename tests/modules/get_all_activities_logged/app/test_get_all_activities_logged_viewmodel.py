from src.modules.get_all_activities_logged.app.get_all_activities_logged_usecase import GetAllActivitiesLoggedUsecase
from src.modules.get_all_activities_logged.app.get_all_activities_logged_viewmodel import GetAllActivitiesLoggedViewmodel
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="get_all_activities_logged")

class Test_GetAllActivitiesLoggedViewmodel:
    def test_get_all_activities_viewmodel(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        requester_user = repo_user.users[2]

        usecase = GetAllActivitiesLoggedUsecase(repo_activity, observability=observability)

        activities_logged = usecase(requester_user.user_id)

        viewmodel = GetAllActivitiesLoggedViewmodel(activities_logged=activities_logged)

        expected = {
            'all_activities_and_user_enrollments':[
                {
                    'activity':{
                        'accepting_new_enrollments':False,
                        'activity_type':'CULTURAL_ACTIVITY',
                        'code':'PINOQ1',
                        'delivery_model':'IN_PERSON',
                        'description':'Não era ''a ''última....',
                        'end_date':45*60*1000 + 1670005013000,
                        'is_extensive':False,
                        'link':None,
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Caio ''Toledo',
                            'role':'PROFESSOR',
                            'user_id':'03555624-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Buscando ''descobrir ''o ''mundo',
                            'company':'Samsung',
                            'name':'Daniel ''Romanato'
                        },
                        {
                            'bio':'Daora',
                            'company':'Microsoft',
                            'name':'Lucas ''Soller'
                        }
                        ],
                        'start_date':1670005013000,
                        'stop_accepting_new_enrollments_before':1669918612000,
                        'taken_slots':4,
                        'title':'Atividade da ''PINOQ1',
                        'total_slots':10
                    },
                    'enrollment':{
                        'date_subscribed':1668982612000,
                        'state':'COMPLETED'
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'PROFESSORS_ACADEMY',
                        'code':'CODE',
                        'delivery_model':'HYBRID',
                        'description':'O mesmo ''speaker ''pela ''50° vez',
                        'end_date':120*60*1000 + 1671488213000,
                        'is_extensive':True,
                        'link':'https://devmaua.com',
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Caio ''Toledo',
                            'role':'PROFESSOR',
                            'user_id':'03555624-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Buscando ''descobrir ''o ''mundo',
                            'company':'Samsung',
                            'name':'Daniel ''Romanato'
                        }
                        ],
                        'start_date':1671488213000,
                        'stop_accepting_new_enrollments_before':None,
                        'taken_slots':0,
                        'title':'Atividade da ''CODE',
                        'total_slots':50
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'INTERNSHIP_FAIR',
                        'code':'SC456',
                        'delivery_model':'ONLINE',
                        'description':'Sem ''criatividade ''para ''descrição',
                        'end_date':80*60*1000 + 1671563813000,
                        'is_extensive':False,
                        'link':'https://devmaua.com',
                        'place':None,
                        'responsible_professors':[
                        {
                            'name':'Caio ''Toledo',
                            'role':'PROFESSOR',
                            'user_id':'03555624-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Incrível',
                            'company':'Apple',
                            'name':'Vitor ''Briquez'
                        }
                        ],
                        'start_date':1671563813000,
                        'stop_accepting_new_enrollments_before':None,
                        'taken_slots':1,
                        'title':'Atividade da ''SC456',
                        'total_slots':10
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'LECTURES',
                        'code':'ELET355',
                        'delivery_model':'HYBRID',
                        'description':'Isso é ''uma ''atividade, ''sério.',
                        'end_date':400*60*1000 + 1671661013000,
                        'is_extensive':True,
                        'link':'https://devmaua.com',
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Patricia ''Santos',
                            'role':'PROFESSOR',
                            'user_id':'6bb122d4-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Daora',
                            'company':'Microsoft',
                            'name':'Lucas ''Soller'
                        }
                        ],
                        'start_date':1671661013000,
                        'stop_accepting_new_enrollments_before':None,
                        'taken_slots':1,
                        'title':'Atividade da ''ELET 355',
                        'total_slots':10
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'HIGH_IMPACT_LECTURES',
                        'code':'COD1468',
                        'delivery_model':'ONLINE',
                        'description':'Isso ''definitivamente ''é uma ''atividade',
                        'end_date':60*60*1000 + 1671661013000,
                        'is_extensive':True,
                        'link':'https://devmaua.com',
                        'place':None,
                        'responsible_professors':[
                        {
                            'name':'Caio ''Toledo',
                            'role':'PROFESSOR',
                            'user_id':'03555624-a110-11ed-a8fc-0242ac120002'
                        },
                        {
                            'name':'Patricia ''Santos',
                            'role':'PROFESSOR',
                            'user_id':'6bb122d4-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Buscando ''descobrir ''o ''mundo',
                            'company':'Samsung',
                            'name':'Daniel ''Romanato'
                        }
                        ],
                        'start_date':1671661013000,
                        'stop_accepting_new_enrollments_before':None,
                        'taken_slots':1,
                        'title':'Atividade da ''COD 1468',
                        'total_slots':50
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'ACADEMIC_COMPETITIONS',
                        'code':'AC000',
                        'delivery_model':'IN_PERSON',
                        'description':'Isso é ''uma ''guerra',
                        'end_date':190*60*1000 + 1671661013000,
                        'is_extensive':True,
                        'link':None,
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Patricia ''Santos',
                            'role':'PROFESSOR',
                            'user_id':'6bb122d4-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Daora',
                            'company':'Microsoft',
                            'name':'Lucas ''Soller'
                        }
                        ],
                        'start_date':1671661013000,
                        'stop_accepting_new_enrollments_before':1671574613000,
                        'taken_slots':2,
                        'title':'Atividade de ''competição',
                        'total_slots':50
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'ALUMNI_CAFE',
                        'code':'CAFE',
                        'delivery_model':'IN_PERSON',
                        'description':'Atividade ''pra ''tomar ''café',
                        'end_date':20*60*1000 + 1671661013000,
                        'is_extensive':True,
                        'link':None,
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Patricia ''Santos',
                            'role':'PROFESSOR',
                            'user_id':'6bb122d4-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Daora',
                            'company':'Microsoft',
                            'name':'Lucas ''Soller'
                        }
                        ],
                        'start_date':1671661013000,
                        'stop_accepting_new_enrollments_before':None,
                        'taken_slots':2,
                        'title':'Atividade da ''CAFE',
                        'total_slots':2
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'HACKATHON',
                        'code':'ECM251',
                        'delivery_model':'HYBRID',
                        'description':'Se o ''professor ''chegar ''vai ter ''atividade...',
                        'end_date':40*60*1000 + 1671733013000,
                        'is_extensive':False,
                        'link':'https://devmaua.com',
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Patricia ''Santos',
                            'role':'PROFESSOR',
                            'user_id':'6bb122d4-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Buscando ''descobrir ''o ''mundo',
                            'company':'Samsung',
                            'name':'Daniel ''Romanato'
                        }
                        ],
                        'start_date':1671733013000,
                        'stop_accepting_new_enrollments_before':None,
                        'taken_slots':1,
                        'title':'Atividade da ''ECM251',
                        'total_slots':20
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'SPORTS_ACTIVITY',
                        'code':'ULTIMA',
                        'delivery_model':'IN_PERSON',
                        'description':'Atividade ''pra ''acabar',
                        'end_date':45*60*1000 + 1671733013000,
                        'is_extensive':False,
                        'link':None,
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Caio ''Toledo',
                            'role':'PROFESSOR',
                            'user_id':'03555624-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Buscando ''descobrir ''o ''mundo',
                            'company':'Samsung',
                            'name':'Daniel ''Romanato'
                        }
                        ],
                        'start_date':1671733013000,
                        'stop_accepting_new_enrollments_before':1671733012000,
                        'taken_slots':3,
                        'title':'Última ''atividade',
                        'total_slots':3
                    },
                    'enrollment':{
                        'date_subscribed':1670710614000,
                        'state':'ENROLLED'
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'COURSES',
                        'code':'ECM2345',
                        'delivery_model':'IN_PERSON',
                        'description':'Isso é ''uma ''atividade',
                        'end_date':120*60*1000 + 1671747413000,
                        'is_extensive':False,
                        'link':None,
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Caio ''Toledo',
                            'role':'PROFESSOR',
                            'user_id':'03555624-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Incrível',
                            'company':'Apple',
                            'name':'Vitor ''Briquez'
                        }
                        ],
                        'start_date':1671747413000,
                        'stop_accepting_new_enrollments_before':1671743812000,
                        'taken_slots':4,
                        'title':'Atividade da ''ECM 2345',
                        'total_slots':4
                    },
                    'enrollment':{
                        'date_subscribed':1671401813000,
                        'state':'ENROLLED'
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'TECHNICAL_VISITS',
                        'code':'CODIGO',
                        'delivery_model':'ONLINE',
                        'description':'Isso ''DEFINITIVAMENTE ''é uma ''atividade!',
                        'end_date':60*60*1000 + 1672006613000,
                        'is_extensive':False,
                        'link':'https://devmaua.com',
                        'place':None,
                        'responsible_professors':[
                        {
                            'name':'Caio ''Toledo',
                            'role':'PROFESSOR',
                            'user_id':'03555624-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Incrível',
                            'company':'Apple',
                            'name':'Vitor ''Briquez'
                        },
                        {
                            'bio':'Daora',
                            'company':'Microsoft',
                            'name':'Lucas ''Soller'
                        },
                        {
                            'bio':'Buscando ''descobrir ''o ''mundo',
                            'company':'Samsung',
                            'name':'Daniel ''Romanato'
                        }
                        ],
                        'start_date':1672006613000,
                        'stop_accepting_new_enrollments_before':1671747413000,
                        'taken_slots':2,
                        'title':'Atividade da ''CÓDIGO',
                        'total_slots':15
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'CULTURAL_ACTIVITY',
                        'code':'PRF246',
                        'delivery_model':'IN_PERSON',
                        'description':'Um ''único ''professor ''pra ''tudo',
                        'end_date':140*60*1000 + 1672006613000,
                        'is_extensive':True,
                        'link':None,
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Caio ''Toledo',
                            'role':'PROFESSOR',
                            'user_id':'03555624-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Incrível',
                            'company':'Apple',
                            'name':'Vitor ''Briquez'
                        }
                        ],
                        'start_date':1672006613000,
                        'stop_accepting_new_enrollments_before':None,
                        'taken_slots':0,
                        'title':'Atividade da ''PRF246',
                        'total_slots':50
                    }
                },
                {
                    'activity':{
                        'accepting_new_enrollments':True,
                        'activity_type':'GCSP',
                        'code':'2468',
                        'delivery_model':'HYBRID',
                        'description':'Atividade ''com ''números ''pares',
                        'end_date':60*60*1000 + 1672006613000,
                        'is_extensive':False,
                        'link':'https://devmaua.com',
                        'place':'H332',
                        'responsible_professors':[
                        {
                            'name':'Caio ''Toledo',
                            'role':'PROFESSOR',
                            'user_id':'03555624-a110-11ed-a8fc-0242ac120002'
                        }
                        ],
                        'speakers':[
                        {
                            'bio':'Daora',
                            'company':'Microsoft',
                            'name':'Lucas ''Soller'
                        }
                        ],
                        'start_date':1672006613000,
                        'stop_accepting_new_enrollments_before':None,
                        'taken_slots':0,
                        'title':'Atividade da ''2468',
                        'total_slots':25
                    }
                }
            ],
            'message':'the activities were retrieved to the user'
        }

        assert viewmodel.to_dict() == expected
