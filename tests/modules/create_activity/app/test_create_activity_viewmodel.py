import datetime
from src.modules.create_activity.app.create_activity_viewmodel import CreateActivityViewmodel
from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE


class Test_CreateActivityViewmodel:

    def test_create_acitivity_viewmodel(self):

        user = User(
            name = "Dummy Name",
            role = ROLE.PROFESSOR,
            user_id = "71f06f24-a110-11ed-a8fc-0242ac120002"
        )

        speaker = Speaker(
            name="Robert Cecil Martin",
            bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
            company="Clean Architecture Company"
        )

        activity = Activity(
            code="ZYX321",
            title="Clean Architecture code review!",
            description="Reviewing IMT student's codes",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=False,
            delivery_model=DELIVERY_MODEL.IN_PERSON,
            start_date=1669141013000,
            end_date=1684151213000,
            link=None,
            place="H331",
            responsible_professors=[user],
            speakers=[speaker],
            total_slots=100,
            taken_slots=97,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=1666451812000,
            confirmation_code="123456"
        )

        activity_viewmodel = CreateActivityViewmodel(activity=activity).to_dict()

        expected = {
            "activity": {
            "code": "ZYX321",
            "title": "Clean Architecture code review!",
            "description": "Reviewing IMT student's codes",
            "activity_type": "LECTURES",
            "is_extensive": False,
            "delivery_model": "IN_PERSON",
            "start_date": 1669141013000,
            "end_date": 1684151213000,
            "link": None,
            "place": "H331",
            "responsible_professors": [{
                "name": "Dummy Name",
                "role": "PROFESSOR",
                "user_id": "71f06f24-a110-11ed-a8fc-0242ac120002"
            }],
            "speakers": [{
                "name": "Robert Cecil Martin",
                "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                "company": "Clean Architecture Company"
            }],
            "total_slots": 100,
            "taken_slots": 97,
            "accepting_new_enrollments": True,
            "stop_accepting_new_enrollments_before": 1666451812000,
            },
            "message":"the activity was created",
            }

        assert expected == activity_viewmodel

    def test_create_acitivity_viewmodel_link_is_not_none(self):

            user = User(
                name = "Dummy Name",
                role = ROLE.PROFESSOR,
                user_id = "71f06f24-a110-11ed-a8fc-0242ac120002"
            )


            speaker = Speaker(
                name = "Robert Cecil Martin",
                bio = "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                company = "Clean Architecture Company"
            )

            activity = Activity(
                code="ZYX321",
                title="Clean Architecture code review!",
                description="Reviewing IMT student's codes",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1669141013000,
                end_date=1684151213000,
                link="www.google.com",
                place="H331",
                responsible_professors=[user],
                speakers=[speaker],
                total_slots=100,
                taken_slots=97,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1666451812000,
                confirmation_code=None
            )
            activity_viewmodel = CreateActivityViewmodel(activity=activity).to_dict()

            expected = {"activity":
                {"code": "ZYX321",
                 "title": "Clean Architecture code review!",
                 "description": "Reviewing IMT student's codes",
                 "activity_type": "LECTURES",
                 "is_extensive": False,
                 "delivery_model": "IN_PERSON",
                 "start_date": 1669141013000,
                 "end_date": 1684151213000,
                 "link": "www.google.com",
                 "place": "H331",
                 "responsible_professors": [{
                     "name": "Dummy Name",
                     "role": "PROFESSOR",
                     "user_id": "71f06f24-a110-11ed-a8fc-0242ac120002"
                 }],
                 "speakers": [{
                     "name": "Robert Cecil Martin",
                     "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                     "company": "Clean Architecture Company"
                 }],
                 "total_slots": 100,
                 "taken_slots": 97,
                 "accepting_new_enrollments": True,
                 "stop_accepting_new_enrollments_before": 1666451812000,
                 },
                "message":"the activity was created"
                }

            assert expected == activity_viewmodel

    def test_create_activity_viewmodel_description_is_none(self):
         
            user = User(
                name = "Dummy Name",
                role = ROLE.PROFESSOR,
                user_id = "71f06f24-a110-11ed-a8fc-0242ac120002"
            )


            speaker = Speaker(
                name = "Robert Cecil Martin",
                bio = "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                company = "Clean Architecture Company"
            )

            activity = Activity(
                code="ZYX321",
                title="Clean Architecture code review!",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1669141013000,
                end_date=1684151213000,
                link="www.google.com",
                place="H331",
                responsible_professors=[user],
                speakers=[speaker],
                total_slots=100,
                taken_slots=97,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1666451812000,
                confirmation_code=None
            )
            activity_viewmodel = CreateActivityViewmodel(activity=activity).to_dict()

            expected = {"activity":
                {"code": "ZYX321",
                 "title": "Clean Architecture code review!",
                 "description": None,
                 "activity_type": "LECTURES",
                 "is_extensive": False,
                 "delivery_model": "IN_PERSON",
                 "start_date": 1669141013000,
                 "end_date": 1684151213000,
                 "link": "www.google.com",
                 "place": "H331",
                 "responsible_professors": [{
                     "name": "Dummy Name",
                     "role": "PROFESSOR",
                     "user_id": "71f06f24-a110-11ed-a8fc-0242ac120002"
                 }],
                 "speakers": [{
                     "name": "Robert Cecil Martin",
                     "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                     "company": "Clean Architecture Company"
                 }],
                 "total_slots": 100,
                 "taken_slots": 97,
                 "accepting_new_enrollments": True,
                 "stop_accepting_new_enrollments_before": 1666451812000,
                 },
                "message":"the activity was created"
                }

            assert expected == activity_viewmodel
    
    def test_create_activity_viewmodel_professors_is_none(self):
            
            speaker = Speaker(
                name = "Robert Cecil Martin",
                bio = "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                company = "Clean Architecture Company"
            )

            activity = Activity(
                code="ZYX321",
                title="Clean Architecture code review!",
                description="Reviewing IMT student's codes",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1669141013000,
                end_date=1684151213000,
                link="www.google.com",
                place="H331",
                speakers=[speaker],
                total_slots=100,
                taken_slots=97,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1666451812000,
                confirmation_code=None
            )
            activity_viewmodel = CreateActivityViewmodel(activity=activity).to_dict()

            expected = {"activity":
                {"code": "ZYX321",
                 "title": "Clean Architecture code review!",
                 "description": "Reviewing IMT student's codes",
                 "activity_type": "LECTURES",
                 "is_extensive": False,
                 "delivery_model": "IN_PERSON",
                 "start_date": 1669141013000,
                 "end_date": 1684151213000,
                 "link": "www.google.com",
                 "place": "H331",
                 "responsible_professors": None,
                 "speakers": [{
                     "name": "Robert Cecil Martin",
                     "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                     "company": "Clean Architecture Company"
                 }],
                 "total_slots": 100,
                 "taken_slots": 97,
                 "accepting_new_enrollments": True,
                 "stop_accepting_new_enrollments_before": 1666451812000,
                 },
                "message":"the activity was created"
                }

            assert expected == activity_viewmodel
    
    def test_create_activity_viewmodel_speakers_is_none(self):  
          
            user = User(
                name = "Dummy Name",
                role = ROLE.PROFESSOR,
                user_id = "71f06f24-a110-11ed-a8fc-0242ac120002"
            )

            activity = Activity(
                code="ZYX321",
                title="Clean Architecture code review!",
                description="Reviewing IMT student's codes",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=False,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1669141013000,
                end_date=1684151213000,
                link="www.google.com",
                place="H331",
                responsible_professors=[user],
                total_slots=100,
                taken_slots=97,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1666451812000,
                confirmation_code=None
            )
            activity_viewmodel = CreateActivityViewmodel(activity=activity).to_dict()

            expected = {"activity":
                {"code": "ZYX321",
                 "title": "Clean Architecture code review!",
                 "description": "Reviewing IMT student's codes",
                 "activity_type": "LECTURES",
                 "is_extensive": False,
                 "delivery_model": "IN_PERSON",
                 "start_date": 1669141013000,
                 "end_date": 1684151213000,
                 "link": "www.google.com",
                 "place": "H331",
                 "responsible_professors": [{
                     "name": "Dummy Name",
                     "role": "PROFESSOR",
                     "user_id": "71f06f24-a110-11ed-a8fc-0242ac120002"
                 }],
                 "speakers": None,
                 "total_slots": 100,
                 "taken_slots": 97,
                 "accepting_new_enrollments": True,
                 "stop_accepting_new_enrollments_before": 1666451812000,
                 },
                "message":"the activity was created"
                }

            assert expected == activity_viewmodel
