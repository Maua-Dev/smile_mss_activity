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
