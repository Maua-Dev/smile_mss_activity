import os
from datetime import datetime

import pytest

from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.infra.repositories.activity_repository_dynamo import ActivityRepositoryDynamo
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


class Test_ActivityRepositoryDynamo:

    @pytest.mark.skip("Can't test dynamo in Github")
    def test_create_activity(self):
        os.environ["STAGE"] = "TEST"
        activity_repository_dynamo = ActivityRepositoryDynamo()
        activity_repository_mock = ActivityRepositoryMock()

        new_activity = activity_repository_mock.activities[0]

        new_activity.code = "TEST_CODE"

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
