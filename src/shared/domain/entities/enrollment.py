import abc
from typing import Optional

from src.shared.domain.entities.activity import Activity
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError


class Enrollment(abc.ABC):
    activity_code: str
    user_id: str
    state: ENROLLMENT_STATE
    date_subscribed: int # milliseconds
    position: int

    def __init__(self, activity_code: str, user_id: str, state: ENROLLMENT_STATE, date_subscribed: int, position: Optional[int]):

        if not Activity.validate_activity_code(activity_code):
            raise EntityError("activity_code")
        self.activity_code = activity_code

        if type(user_id) != str:
            raise EntityError("user_id")
        self.user_id = user_id

        if type(state) != ENROLLMENT_STATE:
            raise EntityError("state")
        self.state = state

        if type(date_subscribed) != int:
            raise EntityError("date_subscribed")
        self.date_subscribed = date_subscribed

        self.position = position

    def __repr__(self):
        return f"Enrollment(activity_code={self.activity_code}, user_id={self.user_id}, state={self.state.value}, date_subscribed={self.date_subscribed})"

    def __eq__(self, other):
        return self.activity_code == other.activity_code and self.user_id == other.user_id and self.state == other.state and self.date_subscribed == other.date_subscribed

