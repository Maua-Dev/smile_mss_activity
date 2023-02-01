import datetime
from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE


class UserViewmodel:
    name: str
    user_id: str
    role: str

    def __init__(self, user: User):
        self.name = user.name
        self.user_id = user.user_id
        self.role = user.role.value

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
            "role": self.role
        }


class SpeakerViewmodel:
    name: str
    bio: str
    company: str

    def __init__(self, speaker: Speaker):
        self.name = speaker.name
        self.bio = speaker.bio
        self.company = speaker.company

    def to_dict(self):
        return {
            "name": self.name,
            "bio": self.bio,
            "company": self.company
        }

class DropActivityViewmodel:
    activity_code: str
    user: UserViewmodel
    state: ENROLLMENT_STATE
    date_subscribed: datetime.datetime
    user: User

    def __init__(self, enrollment: Enrollment, user: User):
        self.activity_code = enrollment.activity_code
        self.user = UserViewmodel(user)
        self.state = enrollment.state
        self.date_subscribed = enrollment.date_subscribed

    def to_dict(self):
        return {
            "activity_code": self.activity_code,
            "user": self.user.to_dict(),
            "state": self.state.value,
            "date_subscribed": self.date_subscribed,
            "message": "the enrollment was dropped"
        }
