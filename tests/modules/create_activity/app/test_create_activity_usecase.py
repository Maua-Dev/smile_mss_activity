import pytest
from src.modules.create_activity.app.create_activity_usecase import CreateActivityUsecase
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound, ForbiddenAction
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.external.observability.observability_mock import ObservabilityMock
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock

observability = ObservabilityMock(module_name="delete_activity")

class Test_CreateActivityUsecase:

    def test_create_activity_usecase(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)
        activitiesLenBefore = len(repo_activity.activities)

        activity = usecase(code="CodigoNovo", title="Atividade da ECM 2345", description="Isso é uma atividade",
                           duration=120, link="www.zoom.br/123", place="H332", total_slots=4, is_extensive=True,
                           accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                           delivery_model=DELIVERY_MODEL.HYBRID,
                           start_date=1671747413000,
                           stop_accepting_new_enrollments_before=1671743813000,
                           speakers=[Speaker(
                               name="Robert Cecil Martin",
                               bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                               company="Clean Architecture Company",
                           )], responsible_professors_user_id=[repo_user.users[2].user_id], user=repo_user.users[0])

        activitiesLenAfter = activitiesLenBefore + 1

        assert len(repo_activity.activities) == activitiesLenAfter
        assert repo_activity.activities[activitiesLenBefore].code == "CodigoNovo"
        assert repo_activity.activities[activitiesLenBefore].title == "Atividade da ECM 2345"
        assert repo_activity.activities[activitiesLenBefore].description == "Isso é uma atividade"
        assert repo_activity.activities[activitiesLenBefore].activity_type == ACTIVITY_TYPE.LECTURES
        assert repo_activity.activities[activitiesLenBefore].delivery_model == DELIVERY_MODEL.HYBRID
        assert repo_activity.activities[activitiesLenBefore].duration == 120
        assert repo_activity.activities[activitiesLenBefore].link == "www.zoom.br/123"
        assert repo_activity.activities[activitiesLenBefore].place == "H332"
        assert repo_activity.activities[activitiesLenBefore].total_slots == 4
        assert repo_activity.activities[activitiesLenBefore].is_extensive == True
        assert repo_activity.activities[activitiesLenBefore].taken_slots == 0
        assert repo_activity.activities[activitiesLenBefore].accepting_new_enrollments == True
        assert repo_activity.activities[activitiesLenBefore].start_date == 1671747413000
        assert repo_activity.activities[activitiesLenBefore].stop_accepting_new_enrollments_before == 1671743813000
        assert repo_activity.activities[activitiesLenBefore].speakers[0].name == "Robert Cecil Martin"
        assert repo_activity.activities[activitiesLenBefore].speakers[
                   0].bio == "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design"
        assert repo_activity.activities[activitiesLenBefore].speakers[0].company == "Clean Architecture Company"
        assert repo_activity.activities[activitiesLenBefore].responsible_professors[0] == repo_user.users[2]

    def test_create_activity_usecase_two_speakers(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)
        activitiesLenBefore = len(repo_activity.activities)

        activity = usecase(code="CodigoNovo", title="Atividade da ECM 2345", description="Isso é uma atividade",
                           duration=120, link='www.zoom.br/123', place="H332", total_slots=4, is_extensive=True,
                           accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                           delivery_model=DELIVERY_MODEL.HYBRID,
                           start_date=1671747413000,
                           stop_accepting_new_enrollments_before=1671743813000,
                           speakers=[Speaker(
                               name="Robert Cecil Martin",
                               bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                               company="Clean Architecture Company",
                           ),
                               Speaker(
                                   name="Vitor Soller",
                                   bio="SOCORRRO ALGUEM ME AJUDA",
                                   company="Clean Architecture Company",
                               )
                           ], responsible_professors_user_id=[repo_user.users[2].user_id], user=repo_user.users[0])

        assert len(repo_activity.activities) == activitiesLenBefore + 1
        assert len(repo_activity.activities[activitiesLenBefore].speakers) == 2
        assert repo_activity.activities[activitiesLenBefore].speakers[0].name == "Robert Cecil Martin"
        assert repo_activity.activities[activitiesLenBefore].speakers[1].name == "Vitor Soller"

    def test_create_activity_usecase_with_two_professors(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)
        activitiesLenBefore = len(repo_activity.activities)

        activity = usecase(code="CodigoNovo", title="Atividade da ECM 2345", description="Isso é uma atividade",
                           duration=120, link='www.zoom.br/1234', place="H332", total_slots=4, is_extensive=True,
                           accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                           delivery_model=DELIVERY_MODEL.HYBRID,
                           start_date=1671747413000,
                           stop_accepting_new_enrollments_before=1671743813000,
                           speakers=[Speaker(
                               name="Robert Cecil Martin",
                               bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                               company="Clean Architecture Company",
                           )], responsible_professors_user_id=[repo_user.users[2].user_id, repo_user.users[11].user_id], user=repo_user.users[0])

        activitiesLenAfter = activitiesLenBefore + 1

        assert len(repo_activity.activities) == activitiesLenAfter
        assert len(repo_activity.activities[activitiesLenBefore].responsible_professors) == 2
        assert repo_activity.activities[activitiesLenBefore].responsible_professors[0] == repo_user.users[2]
        assert repo_activity.activities[activitiesLenBefore].responsible_professors[1] == repo_user.users[11]

    def test_create_activity_usecase_invalid_code_int(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)

        with pytest.raises(EntityError):
            usecase(code=00000, title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000,
                    stop_accepting_new_enrollments_before=1671743813000,
                    speakers=[
                        Speaker(
                            name="Robert Cecil Martin",
                            bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                            company="Clean Architecture Company",
                        )
                    ],
                    responsible_professors_user_id=[repo_user.users[2].user_id], user=repo_user.users[0])

    def test_create_activity_usecase_duplicated_item(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)

        with pytest.raises(DuplicatedItem):
            usecase(code="ECM2345", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000,
                    stop_accepting_new_enrollments_before=1671743813000,
                    speakers=[
                        Speaker(
                            name="Robert Cecil Martin",
                            bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                            company="Clean Architecture Company",
                        )
                    ],
                    responsible_professors_user_id=[repo_user.users[2].user_id], user=repo_user.users[0])

    def test_create_activity_usecase_invalid_speaker(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)

        with pytest.raises(EntityError):
            usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000,
                    stop_accepting_new_enrollments_before=1671743813000,
                    speakers=[
                        Speaker(
                            name=1,
                            bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                            company="Clean Architecture Company",
                        ),
                        Speaker(
                            name="Vitor Soller",
                            bio="SOCORRRO ALGUEM ME AJUDA",
                            company="Clean Architecture Company",
                        )
                    ],
                    responsible_professors_user_id=[repo_user.users[2].user_id], user=repo_user.users[0])

    def test_create_activity_usecase_invalid_speaker_not_speaker(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)

        with pytest.raises(EntityError):
            usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link='www.zoom.br/321', place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000,
                    stop_accepting_new_enrollments_before=1671743813000,
                    speakers=[
                        "Vitor Soller",
                    ],
                    responsible_professors_user_id=[repo_user.users[2].user_id], user=repo_user.users[0])

    def test_create_activity_usecase_missing_responsible_professor(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)

        with pytest.raises(NoItemsFound):
            usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000,
                    stop_accepting_new_enrollments_before=1671743813000,
                    speakers=[
                        Speaker(
                            name="Robert Cecil Martin",
                            bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                            company="Clean Architecture Company",
                        )
                    ],
                    responsible_professors_user_id=[repo_user.users[2].user_id, "0000-0000-00000-000000-0000000-00000"], user=repo_user.users[0])

    def test_create_activity_usecase_invalid_zero_responsible_professor(self):
            repo_activity = ActivityRepositoryMock()
            repo_user = UserRepositoryMock()
            usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)

            with pytest.raises(EntityError):
                usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                        duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                        accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                        delivery_model=DELIVERY_MODEL.HYBRID,
                        start_date=1671747413000,
                        stop_accepting_new_enrollments_before=1671743813000,
                        speakers=[
                            Speaker(
                                name="Robert Cecil Martin",
                                bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                company="Clean Architecture Company",
                            )
                        ],
                        responsible_professors_user_id=[], user=repo_user.users[0])

    def test_create_activity_usecase_invalid_responsible_professor_not_list(self):
            repo_activity = ActivityRepositoryMock()
            repo_user = UserRepositoryMock()
            usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)

            with pytest.raises(EntityError):
                usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                        duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                        accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                        delivery_model=DELIVERY_MODEL.HYBRID,
                        start_date=1671747413000,
                        stop_accepting_new_enrollments_before=1671743813000,
                        speakers=[
                            Speaker(
                                name="Robert Cecil Martin",
                                bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                                company="Clean Architecture Company",
                            )
                        ],
                        responsible_professors_user_id="0000-0000-00000-000000-0000000-00000", user=repo_user.users[0])

    def test_create_activity_usecase_forbidden_not_admin(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()
        usecase = CreateActivityUsecase(repo_activity, repo_user, observability=observability)

        with pytest.raises(ForbiddenAction):
            usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000,
                    stop_accepting_new_enrollments_before=1671743813000,
                    speakers=[
                        Speaker(
                            name="Robert Cecil Martin",
                            bio="Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                            company="Clean Architecture Company",
                        )
                    ],
                    responsible_professors_user_id=[repo_user.users[2].user_id], user=repo_user.users[1])
