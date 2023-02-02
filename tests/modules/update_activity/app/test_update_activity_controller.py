import datetime

import pytest

from src.modules.update_activity.app.update_activity_controller import UpdateActivityController
from src.modules.update_activity.app.update_activity_usecase import UpdateActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_UpdateActivityController:

    def test_update_activity_controller(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012000,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811000, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 200
        assert response.body['activity']['code'] == 'ECM2345'
        assert response.body['activity']['title'] == 'Clean Architecture code review!'
        assert response.body['activity']['description'] == "Reviewing IMT student's codes"
        assert response.body['activity']['activity_type'] == 'LECTURES'
        assert response.body['activity']['is_extensive'] == False
        assert response.body['activity']['delivery_model'] == 'IN_PERSON'
        assert response.body['activity']['start_date'] == 1669141012000
        assert response.body['activity']['duration'] == 90
        assert response.body['activity']['link'] == None
        assert response.body['activity']['place'] == 'H331'
        assert response.body['activity']['responsible_professors'][1]['user_id'] == '62cafdd4-a110-11ed-a8fc-0242ac120002'
        assert response.body['activity']['responsible_professors'][0]['user_id'] == '03555624-a110-11ed-a8fc-0242ac120002'
        assert response.body['activity']['speakers'][0]['name'] == 'Robert Cecil Martin'
        assert response.body['activity']['speakers'][0][
                   'bio'] == 'Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design'
        assert response.body['activity']['speakers'][0]['company'] == 'Clean Architecture Company'
        assert response.body['activity']['total_slots'] == 100
        assert response.body['activity']['accepting_new_enrollments'] == True
        assert response.body['activity']['stop_accepting_new_enrollments_before'] == 1666451811000
        assert response.body['message'] == "the activity was updated"

    def test_update_activity_missing_code(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(body={
            "new_title": "Clean Architecture code review!",
            "new_description": "Reviewing IMT student's codes",
            "new_activity_type": "LECTURES",
            "new_is_extensive": False,
            "new_delivery_model": "IN_PERSON",
            "new_start_date": 1669141012,
            "new_duration": 90,
            "new_link": None,
            "new_place": "H331",
            "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
            "new_speakers": [{
                "name": "Robert Cecil Martin",
                "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                "company": "Clean Architecture Company"
            }],
            "new_total_slots": 100,
            "new_accepting_new_enrollments": True,
            "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value} })

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is missing'

    def test_update_activity_controller_activity_not_found(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM23451",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 404
        assert response.body == 'No items found for Activity'

    def test_update_activity_controller_invalid_code(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": 2345,
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811,'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value} }
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == 'Field code is not valid'

    def test_update_activity_missing_new_title(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_title is missing"

    def test_update_activity_missing_new_description(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_description is missing"

    def test_update_activity_missing_new_activity_type(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_activity_type is missing"

    def test_update_activity_invalid_new_activity_type(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "INVALID",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_activity_type is not valid"

    def test_update_activity_missing_new_is_extensive(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_is_extensive is missing"

    def test_update_activity_missing_new_delivery_model(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_delivery_model is missing"

    def test_update_activity_invalid_new_delivery_model(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "INVALID",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_delivery_model is not valid"

    def test_update_activity_missing_new_start_date(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_start_date is missing"

    def test_update_activity_missing_new_duration(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_duration is missing"

    def test_update_activity_missing_new_responsible_professors(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_responsible_professors is missing"

    def test_update_activity_missing_new_speakers(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_speakers is missing"

    def test_update_activity_controller_professor_not_found(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002", "not_found"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 404
        assert response.body == "No items found for responsible_professors"

    def test_update_activity_controller_invalid_responsible_professors_int(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": 1,
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field responsible_professors is not valid"

    def test_update_activity_invalid_new_speakers(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": ["Pedro", "Juan"],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_speakers is not valid"

    def test_update_activity_invalid_entity_new_speakers(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company",
                      "invalid_field": "invalid"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_speakers is not valid"

    def test_update_activity_new_speakers_not_dict(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": 1,
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_speakers is not valid"


    def test_update_activity_missing_new_total_slots(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_total_slots is missing"

    def test_update_activity_missing_new_accepting_new_enrollments(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_stop_accepting_new_enrollments_before": 1666451811, 'requester_user': {"sub": repo.users[0].user_id, "cognito:username": repo.users[0].name, "custom:role": repo.users[0].role.value}}
        )

        response = controller(request)

        assert response.status_code == 400
        assert response.body == "Field new_accepting_new_enrollments is missing"

    @pytest.mark.skip("Still no ForbiddenAction exception")
    def test_update_activity_controller_forbidden_user_not_admin(self):
        repo = ActivityRepositoryMock()
        usecase = UpdateActivityUsecase(repo)
        controller = UpdateActivityController(usecase)

        request = HttpRequest(
            body={"code": "ECM2345",
                  "new_title": "Clean Architecture code review!",
                  "new_description": "Reviewing IMT student's codes",
                  "new_activity_type": "LECTURES",
                  "new_is_extensive": False,
                  "new_delivery_model": "IN_PERSON",
                  "new_start_date": 1669141012000,
                  "new_duration": 90,
                  "new_link": None,
                  "new_place": "H331",
                  "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                  "new_speakers": [{
                      "name": "Robert Cecil Martin",
                      "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                      "company": "Clean Architecture Company"
                  }],
                  "new_total_slots": 100,
                  "new_accepting_new_enrollments": True,
                  "new_stop_accepting_new_enrollments_before": 1666451811000, 'requester_user': {"sub": repo.users[1].user_id, "cognito:username": repo.users[1].name, "custom:role": repo.users[1].role.value}}
        )

        response = controller(request)

        assert response.status_code == 403
        assert response.body == "That action is forbidden for this update_activity, only admins can update activities"
