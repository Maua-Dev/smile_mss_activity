import pytest

from src.modules.create_activity.app.create_activity_controller import CreateActivityController
from src.modules.create_activity.app.create_activity_usecase import CreateActivityUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="create_activity")


class Test_CreateActivityController:
    def test_create_activity_controller(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "IN_PERSON",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000, 'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 201
        assert response.body['activity']['code'] == 'ZYX321'
        assert response.body['activity']['title'] == 'Clean Architecture code review!'
        assert response.body['activity']['description'] == "Reviewing IMT student's codes"
        assert response.body['activity']['activity_type'] == 'LECTURES'
        assert response.body['activity']['is_extensive'] == False
        assert response.body['activity']['delivery_model'] == 'IN_PERSON'
        assert response.body['activity']['start_date'] == 1669141012000
        assert response.body['activity']['place'] == 'H331'
        assert response.body['activity']['end_date'] == 90
        assert response.body['activity']['responsible_professors'][1]['user_id'] == '62cafdd4-a110-11ed-a8fc-0242ac120002'
        assert response.body['activity']['speakers'][0]['name'] == "Robert Cecil Martin"
        assert response.body['activity']['total_slots'] == 100
        assert response.body['activity']['taken_slots'] == 0
        assert response.body['activity']['accepting_new_enrollments'] == True
        assert response.body['activity']['stop_accepting_new_enrollments_before'] == 1666451811000

    def test_create_activity_controller_missing_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: code"

    def test_create_activity_controller_wrong_code(self):
            repo_activity = ActivityRepositoryMock()
            repo_user = UserRepositoryMock()
            usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
            controller = CreateActivityController(usecase=usecase, observability=observability)

            request = HttpRequest(
                body={
                    "code" : 123,
                    "title": "Clean Architecture code review!",
                    "description": "Reviewing IMT student's codes",
                    "activity_type": "LECTURES",
                    "is_extensive": False,
                    "delivery_model": "IN_PERSON",
                    "start_date": 1669141012000,
                    "end_date": 90,
                    "link": None,
                    "place": "H331",
                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                    "speakers": [{
                        "name": "Robert Cecil Martin",
                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                        "company": "Clean Architecture Company"
                    }],
                    "total_slots": 100,
                    "accepting_new_enrollments": True,
                    "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

            response = controller(request=request)

            assert response.status_code == 400
            assert response.body == "Parâmetro inválido: code"

    def test_create_activity_controller_duplicated_code(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ECM2345",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == 'Já existe uma atividade com esse código'

    def test_create_activity_controller_missing_title(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: title"

    def test_create_activity_controller_missing_description(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: description"

    def test_create_activity_controller_missing_activity_type(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: activity_type"

    def test_create_activity_controller_invalid_activity_type(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "INVALID_TYPE",
                                    "is_extensive": False,
                                    "delivery_model": "IN_PERSON",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000, 'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro inválido: activity_type"

    def test_create_activity_controller_missing_is_extensive(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: is_extensive"

    def test_create_activity_controller_missing_delivery_model(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: delivery_model"

    def test_create_activity_controller_invalid_delivery_model(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "INVALID_TYPE",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000, 'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro inválido: delivery_model"

    def test_create_activity_controller_invalid_start_date(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: start_date"

    def test_create_activity_controller_missing_end_date(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: end_date"

    def test_create_activity_controller_missing_responsible_professors(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: responsible_professors"

    def test_create_activity_invalid_responsible_professors(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": 123,
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro inválido: responsible_professors"

    def test_create_activity_invalid_responsible_professors_id_invalid(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ['123'],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 404
        assert response.body == "Professores responsáveis não encontrados"

    def test_create_activity_controller_missing_speakers(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: speakers"

    def test_create_actvivity_invalid_speaker_type(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": "123",
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro inválido: speakers"

    def test_create_activity_invalid_speaker_parameter(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company",
                    "invalid": "invalid"
                }],
                "total_slots": 100,
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro inválido: speakers"

    def test_create_activity_controller_missing_total_slots(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "accepting_new_enrollments": True,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: total_slots"

    def test_create_activity_controller_missing_accepting_new_enrollments(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(
            body={
                "code": "ZYX321",
                "title": "Clean Architecture code review!",
                "description": "Reviewing IMT student's codes",
                "activity_type": "LECTURES",
                "is_extensive": False,
                "delivery_model": "IN_PERSON",
                "start_date": 1669141012000,
                "end_date": 90,
                "link": None,
                "place": "H331",
                "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                "speakers": [{
                    "name": "Robert Cecil Martin",
                    "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                    "company": "Clean Architecture Company"
                }],
                "total_slots": 100,
                "stop_accepting_new_enrollments_before": 1666451811000,'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}})

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: accepting_new_enrollments"

    def test_create_activity_controller_missing_request_user(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "IN_PERSON",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002",
                                                               "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000,
                                    }
                              )

        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro ausente: requester_user"


    def test_create_activity_controller_forbidden_not_admin(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "IN_PERSON",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002",
                                                               "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000,
                                    'requester_user': {"sub": repo_user.users[1].user_id,
                                                       "name": repo_user.users[1].name,
                                                       "custom:role": repo_user.users[1].role.value}}
                              )

        response = controller(request=request)

        assert response.status_code == 403
        assert response.body == "Apenas administradores podem criar atividades"
    def test_create_activity_controller_in_person_no_place_established(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "IN_PERSON",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": None,
                                    "place": None,
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000, 'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro inválido: link or place"

    def test_create_activity_controller_online_no_link_established(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "ONLINE",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": None,
                                    "place": None,
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002",
                                                               "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000,
                                    'requester_user': {"sub": repo_user.users[0].user_id,
                                                       "name": repo_user.users[0].name,
                                                       "custom:role": repo_user.users[0].role.value}}
                              )
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro inválido: link or place"

    def test_create_activity_controller_hybrid_no_link_established(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "ONLINE",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": None,
                                    "place": "H331",
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002",
                                                               "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000,
                                    'requester_user': {"sub": repo_user.users[0].user_id,
                                                       "name": repo_user.users[0].name,
                                                       "custom:role": repo_user.users[0].role.value}}
                              )
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro a mais está gerando um conflito: local"

    def test_create_activity_controller_in_person_conflicting_link_information(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "IN_PERSON",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": 'www.maua.br',
                                    "place": 'H123',
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000, 'requester_user': {"sub": repo_user.users[0].user_id, "name": repo_user.users[0].name, "custom:role": repo_user.users[0].role.value}}
        )
        response = controller(request=request)


        assert response.status_code == 400
        assert response.body == "Parâmetro a mais está gerando um conflito: link"

    def test_create_activity_controller_online_conflicting_place_information(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity=repo_activity, repo_user=repo_user, observability=observability)
        controller = CreateActivityController(usecase=usecase, observability=observability)

        request = HttpRequest(body={"code": "ZYX321",
                                    "title": "Clean Architecture code review!",
                                    "description": "Reviewing IMT student's codes",
                                    "activity_type": "LECTURES",
                                    "is_extensive": False,
                                    "delivery_model": "ONLINE",
                                    "start_date": 1669141012000,
                                    "end_date": 90,
                                    "link": 'www.google.com',
                                    "place": 'H321',
                                    "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002",
                                                               "03555624-a110-11ed-a8fc-0242ac120002"],
                                    "speakers": [{
                                        "name": "Robert Cecil Martin",
                                        "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                        "company": "Clean Architecture Company"
                                    }],
                                    "total_slots": 100,
                                    "accepting_new_enrollments": True,
                                    "stop_accepting_new_enrollments_before": 1666451811000,
                                    'requester_user': {"sub": repo_user.users[0].user_id,
                                                       "name": repo_user.users[0].name,
                                                       "custom:role": repo_user.users[0].role.value}}
                              )
        response = controller(request=request)

        assert response.status_code == 400
        assert response.body == "Parâmetro a mais está gerando um conflito: local"

