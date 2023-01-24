import datetime

import pytest
from src.modules.create_activity.app.create_activity_usecase import CreateActivityUsecase
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, NoItemsFound
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.helpers.errors.domain_errors import EntityError


class Test_CreateActivityUsecase:

    def test_create_activity_usecase(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        activitiesLenBefore = len(repo.activities)

        activity = usecase(code="CodigoNovo", title="Atividade da ECM 2345", description="Isso é uma atividade",
                           duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                           accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                           delivery_model=DELIVERY_MODEL.HYBRID,
                           start_date=1671747413000000,
                           stop_accepting_new_enrollments_before=1671743813000000,
                           speakers=[{
                               "name": "Robert Cecil Martin",
                               "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                               "company": "Clean Architecture Company"
                           }], responsible_professors_user_id=[repo.users[2].user_id])

        activitiesLenAfter = activitiesLenBefore + 1

        assert len(repo.activities) == activitiesLenAfter
        assert repo.activities[activitiesLenBefore].code == "CodigoNovo"
        assert repo.activities[activitiesLenBefore].title == "Atividade da ECM 2345"
        assert repo.activities[activitiesLenBefore].description == "Isso é uma atividade"
        assert repo.activities[activitiesLenBefore].activity_type == ACTIVITY_TYPE.LECTURES
        assert repo.activities[activitiesLenBefore].delivery_model == DELIVERY_MODEL.HYBRID
        assert repo.activities[activitiesLenBefore].duration == 120
        assert repo.activities[activitiesLenBefore].link == None
        assert repo.activities[activitiesLenBefore].place == "H332"
        assert repo.activities[activitiesLenBefore].total_slots == 4
        assert repo.activities[activitiesLenBefore].is_extensive == True
        assert repo.activities[activitiesLenBefore].taken_slots == 0
        assert repo.activities[activitiesLenBefore].accepting_new_enrollments == True
        assert repo.activities[activitiesLenBefore].start_date == 1671747413000000
        assert repo.activities[activitiesLenBefore].stop_accepting_new_enrollments_before == 1671743813000000
        assert repo.activities[activitiesLenBefore].speakers[0].name == "Robert Cecil Martin"
        assert repo.activities[activitiesLenBefore].speakers[
                   0].bio == "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design"
        assert repo.activities[activitiesLenBefore].speakers[0].company == "Clean Architecture Company"
        assert repo.activities[activitiesLenBefore].responsible_professors[0] == repo.users[2]

    def test_create_activity_usecase_two_speakers(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        activitiesLenBefore = len(repo.activities)

        activity = usecase(code="CodigoNovo", title="Atividade da ECM 2345", description="Isso é uma atividade",
                           duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                           accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                           delivery_model=DELIVERY_MODEL.HYBRID,
                           start_date=1671747413000000,
                           stop_accepting_new_enrollments_before=1671743813000000,
                           speakers=[{
                               "name": "Robert Cecil Martin",
                               "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                               "company": "Clean Architecture Company"
                           },
                               {
                                   "name": "Vitor Soller",
                                   "bio": "SOCORRRO ALGUEM ME AJUDA",
                                   "company": "Clean Architecture Company"
                               }
                           ], responsible_professors_user_id=[repo.users[2].user_id])

        assert len(repo.activities) == activitiesLenBefore + 1
        assert len(repo.activities[activitiesLenBefore].speakers) == 2
        assert repo.activities[activitiesLenBefore].speakers[0].name == "Robert Cecil Martin"
        assert repo.activities[activitiesLenBefore].speakers[1].name == "Vitor Soller"

    def test_create_activity_usecase_with_two_professors(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo)
        activitiesLenBefore = len(repo.activities)

        activity = usecase(code="CodigoNovo", title="Atividade da ECM 2345", description="Isso é uma atividade",
                           duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                           accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                           delivery_model=DELIVERY_MODEL.HYBRID,
                           start_date=1671747413000000,
                           stop_accepting_new_enrollments_before=1671743813000000,
                           speakers=[{
                               "name": "Robert Cecil Martin",
                               "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                               "company": "Clean Architecture Company"
                           }], responsible_professors_user_id=[repo.users[2].user_id, repo.users[11].user_id])

        activitiesLenAfter = activitiesLenBefore + 1

        assert len(repo.activities) == activitiesLenAfter
        assert len(repo.activities[activitiesLenBefore].responsible_professors) == 2
        assert repo.activities[activitiesLenBefore].responsible_professors[0] == repo.users[2]
        assert repo.activities[activitiesLenBefore].responsible_professors[1] == repo.users[11]

    def test_create_activity_usecase_invalid_code_int(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(code=00000, title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000000,
                    stop_accepting_new_enrollments_before=1671743813000000,
                    speakers=[
                        {
                            "name": "Robert Cecil Martin",
                            "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                            "company": "Clean Architecture Company"
                        }
                    ],
                    responsible_professors_user_id=[repo.users[2].user_id])

    def test_create_activity_usecase_duplicated_item(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)

        with pytest.raises(DuplicatedItem):
            usecase(code="ECM2345", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000000,
                    stop_accepting_new_enrollments_before=1671743813000000,
                    speakers=[
                        {
                            "name": "Robert Cecil Martin",
                            "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                            "company": "Clean Architecture Company"
                        }
                    ],
                    responsible_professors_user_id=[repo.users[2].user_id])

    def test_create_activity_usecase_invalid_speaker_missing_parameter(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000000,
                    stop_accepting_new_enrollments_before=1671743813000000,
                    speakers=[
                        {
                            "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                            "company": "Clean Architecture Company"
                        },
                        {
                            "name": "Vitor Soller",
                            "bio": "SOCORRRO ALGUEM ME AJUDA",
                            "company": "Clean Architecture Company"
                        }
                    ],
                    responsible_professors_user_id=[repo.users[2].user_id])

    def test_create_activity_usecase_invalid_speaker_invalid_parameter(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000000,
                    stop_accepting_new_enrollments_before=1671743813000000,
                    speakers=[
                        {
                            "name":1,
                            "bio": "Author of Clean Architecture: A Craftsman's Guide to Software Structure and Design",
                            "company": "Clean Architecture Company"
                        },
                        {
                            "name": "Vitor Soller",
                            "bio": "SOCORRRO ALGUEM ME AJUDA",
                            "company": "Clean Architecture Company"
                        }
                    ],
                    responsible_professors_user_id=[repo.users[2].user_id])


    def test_create_activity_usecase_invalid_speaker(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)

        with pytest.raises(EntityError):
            usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000000,
                    stop_accepting_new_enrollments_before=1671743813000000,
                    speakers=[
                        "Vitor Soller",
                    ],
                    responsible_professors_user_id=[repo.users[2].user_id])

    def test_create_activity_usecase_missing_responsible_professor(self):
        repo = ActivityRepositoryMock()
        usecase = CreateActivityUsecase(repo=repo)

        with pytest.raises(NoItemsFound):
            usecase(code="CODIGONOVO", title="Atividade da ECM 2345", description="Isso é uma atividade",
                    duration=120, link=None, place="H332", total_slots=4, is_extensive=True,
                    accepting_new_enrollments=True, activity_type=ACTIVITY_TYPE.LECTURES,
                    delivery_model=DELIVERY_MODEL.HYBRID,
                    start_date=1671747413000000,
                    stop_accepting_new_enrollments_before=1671743813000000,
                    speakers=[
                        {
                            "name": "Vitor Soller",
                            "bio": "SOCORRRO ALGUEM ME AJUDA",
                            "company": "Clean Architecture Company"
                        }
                    ],
                    responsible_professors_user_id=[repo.users[2].user_id, "0000"])


