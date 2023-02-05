import os
from datetime import datetime

import pytest

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.repositories.activity_repository_dynamo import ActivityRepositoryDynamo
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock
from src.shared.infra.repositories.user_repository_mock import UserRepositoryMock


class Test_ActivityRepositoryDynamo:

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_activity(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        new_activity = new_activity = Activity(
            code="EAD109",
            title="Curso de verão de cálculo 2",
            description="curso de verão",
            activity_type=ACTIVITY_TYPE.COURSES,
            is_extensive=False,
            delivery_model=DELIVERY_MODEL.ONLINE,
            start_date=1671747413000,
            duration=120,
            link=None,
            place="H332",
            responsible_professors=[
                User(name="Juliana Vetores", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="João Vitor Branco", bio="Incrível", company="IMT")],
            total_slots=4,
            taken_slots=4,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=1671743812000
        )

        activity_created = activity_repository_dynamo.create_activity(new_activity)

        assert activity_created == new_activity

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_activity(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        for activity in activity_repository_mock.activities:
            activity_gotten = activity_repository_dynamo.get_activity(activity.code)
            assert type(activity_gotten) == Activity
            assert activity_gotten.code == activity.code
            assert activity_gotten.title == activity.title
            assert activity_gotten.description == activity.description
            assert activity_gotten.delivery_model == activity.delivery_model
            assert activity_gotten.activity_type == activity.activity_type
            assert activity_gotten.start_date == activity.start_date
            assert activity_gotten.duration == activity.duration
            assert activity_gotten.link == activity.link
            assert activity_gotten.place == activity.place
            assert activity_gotten.responsible_professors == activity.responsible_professors
            assert activity_gotten.speakers == activity.speakers
            assert activity_gotten.total_slots == activity.total_slots
            assert activity_gotten.taken_slots == activity.taken_slots
            assert activity_gotten.accepting_new_enrollments == activity.accepting_new_enrollments
            assert activity_gotten.stop_accepting_new_enrollments_before == activity.stop_accepting_new_enrollments_before

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_enrollment(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        enrollment = activity_repository_mock.enrollments[0]

        new_enrollment = activity_repository_dynamo.create_enrollment(enrollment)

        assert enrollment == new_enrollment

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_enrollment(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        enrollment = activity_repository_mock.enrollments[0]

        enrollment_gotten = activity_repository_dynamo.get_enrollment(enrollment.user_id, enrollment.activity_code)

        assert enrollment_gotten == enrollment

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_get_enrollment_dropped(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        enrollment = activity_repository_mock.enrollments[8]

        enrollment_gotten = activity_repository_dynamo.get_enrollment(enrollment.user_id, enrollment.activity_code)

        assert enrollment_gotten is None

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_enrollment_drop(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()
        enrollment = repo_activity_dynamo.update_enrollment(user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002", code="ECM2345",
                                            new_state=ENROLLMENT_STATE.DROPPED)

        assert enrollment.user_id == "d61dbf66-a10f-11ed-a8fc-0242ac120002"
        assert enrollment.activity_code == "ECM2345"
        assert enrollment.state == ENROLLMENT_STATE.DROPPED

    # @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_enrollment_enroll(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        enrollment = repo_activity_dynamo.update_enrollment(user_id="03555872-a110-11ed-a8fc-0242ac120002", code="ECM2345",
                                            new_state=ENROLLMENT_STATE.ENROLLED)

        assert enrollment.user_id == "03555872-a110-11ed-a8fc-0242ac120002"
        assert enrollment.activity_code == "ECM2345"
        assert enrollment.state == ENROLLMENT_STATE.ENROLLED

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_enrollment_not_found(self):
        repo_activity_dynamo = ActivityRepositoryDynamo()

        enrollment = repo_activity_dynamo.update_enrollment(user_id="03555872-a110-11ed-a8fc-0242ac120002", code="NAO_EXISTE", new_state=ENROLLMENT_STATE.DROPPED)

        assert enrollment is None

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_update_activity(self):
        repo_activity = ActivityRepositoryMock()
        repo_user = UserRepositoryMock()

        repo_activity_dynamo = ActivityRepositoryDynamo()
        new_activity = repo_activity_dynamo.update_activity(code=repo_activity.activities[0].code,
                                                             new_title="NOVO TITULO",
                                                             new_description='nova descricao',
                                                             new_activity_type=ACTIVITY_TYPE.LECTURES,
                                                             new_is_extensive=True,
                                                             new_delivery_model=DELIVERY_MODEL.ONLINE,
                                                             new_start_date=1630465200000, new_duration=15,
                                                             new_link="www.google.com.br",
                                                             new_place="Sala 1",
                                                             new_responsible_professors=[
                                                                 repo_user.users[2],
                                                                 repo_user.users[11]],
                                                             new_speakers=[
                                                                 Speaker(
                                                                     name="Fulano de Tal",
                                                                     bio="Fulano de Tal é um professor de Engenharia de Software",
                                                                     company="Universidade Federal de Fulano de tal",
                                                                 )
                                                             ], new_total_slots=100,
                                                             new_accepting_new_enrollments=True,
                                                             new_stop_accepting_new_enrollments_before=None)

        assert new_activity.code == repo_activity.activities[0].code
        assert new_activity.title == "NOVO TITULO"
        assert new_activity.description == 'nova descricao'
        assert new_activity.activity_type == ACTIVITY_TYPE.LECTURES
        assert new_activity.is_extensive == True
        assert new_activity.delivery_model == DELIVERY_MODEL.ONLINE
        assert new_activity.start_date == 1630465200000
        assert new_activity.duration == 15
        assert new_activity.link == 'www.google.com.br'
        assert new_activity.place == "Sala 1"
        assert new_activity.responsible_professors == [
            repo_user.users[2],
            repo_user.users[11]]
        assert new_activity.speakers == [
            Speaker(
                name="Fulano de Tal",
                bio="Fulano de Tal é um professor de Engenharia de Software",
                company="Universidade Federal de Fulano de tal",
            )
        ]
        assert new_activity.total_slots == 100
        assert new_activity.accepting_new_enrollments == True
        assert new_activity.stop_accepting_new_enrollments_before is None
        assert new_activity.taken_slots == repo_activity.activities[0].taken_slots
