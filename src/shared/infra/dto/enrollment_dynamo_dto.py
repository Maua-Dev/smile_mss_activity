from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE


class EnrollmentDynamoDTO:
    activity_code: str
    user_id: str
    state: ENROLLMENT_STATE
    date_subscribed: int  # milliseconds

    def __init__(self, activity_code: str, user_id: str, state: ENROLLMENT_STATE, date_subscribed: int):
        self.activity_code = activity_code
        self.user_id = user_id
        self.state = state
        self.date_subscribed = date_subscribed

    @staticmethod
    def from_entity(self):
        """
        Parse a Enrollment entity to a EnrollmentDynamoDTO
        """
        return EnrollmentDynamoDTO(
            activity_code=self.activity_code,
            user_id=self.user_id,
            state=self.state,
            date_subscribed=self.date_subscribed
        )

    def to_dynamo(self):
        """
        Parse a EnrollmentDynamoDTO to a DynamoDB item
        """
        return {
            "activity_code": self.activity_code,
            "user_id": self.user_id,
            "state": self.state.value,
            "date_subscribed": self.date_subscribed,
            "entity": "enrollment",
        }

    @staticmethod
    def from_dynamo(dynamo_data: dict):
        """
        Parse a DynamoDB item to a EnrollmentDynamoDTO
        """
        return EnrollmentDynamoDTO(
            activity_code=dynamo_data.get("activity_code"),
            user_id=dynamo_data.get("user_id"),
            state=ENROLLMENT_STATE(dynamo_data.get("state")),
            date_subscribed=int(dynamo_data.get("date_subscribed"))
        )

    def to_entity(self):
        """
        Parse a EnrollmentDynamoDTO to a Enrollment entity
        """
        return Enrollment(
            activity_code=self.activity_code,
            user_id=self.user_id,
            state=self.state,
            date_subscribed=self.date_subscribed
        )

    def __eq__(self, other):
        return self.activity_code == other.activity_code and self.user_id == other.user_id and self.state == other.state and self.date_subscribed == other.date_subscribed
