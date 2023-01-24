import abc
import datetime

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError


class Enrollment(abc.ABC):
    activity: Activity
    user: User
    state: ENROLLMENT_STATE
    date_subscribed: int

    def __init__(self, activity: Activity, user: User, state: ENROLLMENT_STATE, date_subscribed: int):

        if type(activity) != Activity:
            raise EntityError("activity")
        self.activity = activity

        if type(user) != User:
            raise EntityError("user")
        self.user = user

        if type(state) != ENROLLMENT_STATE:
            raise EntityError("state")
        self.state = state

        if type(date_subscribed) != int:
            raise EntityError("date_subscribed")
        self.date_subscribed = date_subscribed

    def __repr__(self):
        return f"Enrollment(activity={self.activity}, user={self.user}, state={self.state.value}, date_subscribed={self.date_subscribed})"

    def __eq__(self, other):
        return self.activity == other.activity and self.user == other.user and self.state == other.state and self.date_subscribed == other.date_subscribed

