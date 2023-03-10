from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.infra.dto.enrollment_dynamo_dto import EnrollmentDynamoDTO


class Test_EnrollmentDynamoDTO:
    def test_from_entity(self):

        enrollment = Enrollment(
            activity_code="activity_code",
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=1671229013000
        )

        enrollemnt_dto = EnrollmentDynamoDTO.from_entity(enrollment)

        expected = EnrollmentDynamoDTO(
            activity_code="activity_code",
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=1671229013000
        )

        assert enrollemnt_dto == expected

    def test_to_dynamo(self):
        enrollemnt_dto = EnrollmentDynamoDTO(
            activity_code="activity_code",
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=1671229013000
        ).to_dynamo()


        expected = {
            "activity_code": "activity_code",
            "user_id": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
            "state": "ENROLLED",
            "date_subscribed": 1671229013000,
            "entity": "enrollment",
        }

        assert enrollemnt_dto == expected

    def test_from_entity_to_dynamo(self):
        enrollment = Enrollment(
            activity_code="activity_code",
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=1671229013000
        )

        enrollemnt_dto = EnrollmentDynamoDTO.from_entity(enrollment).to_dynamo()

        expected = {
            "activity_code": "activity_code",
            "user_id": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
            "state": "ENROLLED",
            "date_subscribed": 1671229013000,
            "entity": "enrollment",
        }

        assert enrollemnt_dto == expected


    def test_from_dynamo(self):
        dynamo_data = {
            "activity_code": "activity_code",
            "user_id": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
            "state": "ENROLLED",
            "date_subscribed": 1671229013000,
            "entity": "enrollment",
        }

        enrollment_dto = EnrollmentDynamoDTO.from_dynamo(dynamo_data)

        expected = EnrollmentDynamoDTO(
            activity_code="activity_code",
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=1671229013000
        )

        assert enrollment_dto == expected

    def test_to_entity(self):
        enrollment_dto = EnrollmentDynamoDTO(
            activity_code="activity_code",
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=1671229013000
        )

        enrollment = enrollment_dto.to_entity()

        expected = Enrollment(
            activity_code="activity_code",
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=1671229013000
        )

        assert enrollment == expected

    def test_from_dynamo_to_entity(self):
        dynamo_data = {
            "activity_code": "activity_code",
            "user_id": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
            "state": "ENROLLED",
            "date_subscribed": 1671229013000,
            "entity": "enrollment",
        }

        enrollment = EnrollmentDynamoDTO.from_dynamo(dynamo_data).to_entity()

        expected = Enrollment(
            activity_code="activity_code",
            user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002",
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=1671229013000
        )

        assert enrollment == expected
