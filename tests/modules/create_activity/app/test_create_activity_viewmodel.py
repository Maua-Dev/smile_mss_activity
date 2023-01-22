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
            user_id = "a1z2"
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
            start_date=datetime.datetime(2022, 11, 22, 15, 16, 52, 998305),
            duration=90,
            link=None,
            place="H331",
            responsible_professors=[user],
            speakers=[speaker],
            total_slots=100,
            taken_slots=97,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=datetime.datetime(2022, 10, 22, 12, 16, 51, 998305)
        )
        activity_viewmodel = CreateActivityViewmodel(activity=activity).to_dict()
        
        expected = {
            "code":"ZYX321",
            "title":"Clean Architecture code review!",
            "description":"Reviewing IMT student's codes",
            "activity_type":"LECTURES",
            "is_extensive":False,
            "delivery_model":"IN_PERSON",
            "start_date":"2022-11-22T15:16:52.998305",
            "duration":90,
            "link":None,
            "place":"H331",
            "responsible_professors":[{ 
                "name":"Dummy Name",
                "role":"PROFESSOR",
                "user_id":"a1z2"
            }],
            "speakers":[{
                "name":"Robert Cecil Martin",
                "bio":"Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                "company":"Clean Architecture Company"
            }],
            "total_slots":100,
            "taken_slots":97,
            "accepting_new_enrollments":True,
            "stop_accepting_new_enrollments_before":"2022-10-22T12:16:51.998305",
            "message":"the activity was created"
            }

        assert expected == activity_viewmodel
