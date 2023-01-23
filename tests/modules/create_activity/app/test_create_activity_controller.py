
from src.modules.create_activity.app.create_activity_controller import CreateActivityController
from src.modules.create_activity.app.create_activity_usecase import CreateActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_CreateActivityController:
    def test_create_activity_controller(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(body={"code":"ZYX321",
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
            })
        response = controller(request=request)

        assert response.body['code']== 'ZYX321'
        assert response.body['title'] == "Reviewing IMT student's codes"
        assert response.body['ACTIVITY_TYPE'] == 'LECTURES'
        assert response.body['is_extensive'] == False
        assert response.body['DELIVERY_MODEL'] == 'IN_PERSON'
        assert response.body['start_date'] == '2022-11-22T15:16:52.998305'
        assert response.body['place'] == 'H331'
        assert response.body['duration'] == 90
        assert response.body['responsible_professors']['user_id'] == 'a1z2'
        assert response.body['speakers']['name'] == 'Dummy Name'
        assert response.body['total_slots'] == 100
        assert response.body['taken_slots'] == 97
        assert response.body['accepting_new_enrollments'] == True
        assert response.body['stop_accepting_new_enrollments_before'] == '2022-12-22T12:16:51.998305'
        assert response.status_code == 201

    def test_create_activity_controller_missing_code(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(body={})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field code is missing"
"""
    def test_create_activity_bad_request_int(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)
        controller = CreateActivityController(usecase=usecase)

        request = HttpRequest(body={'code':12345})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Field code is not valid"
"""