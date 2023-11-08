from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE


class UserViewmodel:
    name: str
    role: ROLE
    user_id: str

    def __init__(self, user: User):
        self.name = user.name
        self.role = user.role
        self.user_id = user.user_id

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "role": self.role.value,
            "user_id": self.user_id
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


class DownloadActivityViewmodel:
    code: str
    title: str
    description: str
    activity_type: ACTIVITY_TYPE
    is_extensive: bool
    delivery_model: DELIVERY_MODEL
    start_date: int # milliseconds
    end_date: int  # milliseconds
    link: str
    place: str
    speakers: List[SpeakerViewmodel]
    total_slots: int
    taken_slots: int
    accepting_new_enrollments: bool
    stop_accepting_new_enrollments_before: int
    

    def __init__(self, activity: Activity, requester_user: User):
        self.code = activity.code
        self.title = activity.title
        self.description = activity.description
        self.activity_type = activity.activity_type
        self.is_extensive = activity.is_extensive
        self.delivery_model = activity.delivery_model
        self.start_date = activity.start_date
        self.end_date = activity.end_date
        self.link = activity.link
        self.place = activity.place
        self.speakers = [SpeakerViewmodel(speaker)
                         for speaker in activity.speakers]
        self.total_slots = activity.total_slots
        self.taken_slots = activity.taken_slots
        self.accepting_new_enrollments = activity.accepting_new_enrollments
        self.stop_accepting_new_enrollments_before = activity.stop_accepting_new_enrollments_before
        self.responsible_professors = [UserViewmodel(
            professor) for professor in activity.responsible_professors]
        self.requester_user = UserViewmodel(requester_user)

    def to_dict(self):
        return {
            "activity": {
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "activity_type": self.activity_type.value,
            "is_extensive": self.is_extensive,
            "delivery_model": self.delivery_model.value,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "link": self.link,
            "place": self.place,
            "responsible_professors": [professor.to_dict() for professor in self.responsible_professors],
            "speakers": [speaker.to_dict() for speaker in self.speakers],
            "total_slots": self.total_slots,
            "taken_slots": self.taken_slots,
            "accepting_new_enrollments": self.accepting_new_enrollments,
            "stop_accepting_new_enrollments_before": self.stop_accepting_new_enrollments_before if self.stop_accepting_new_enrollments_before is not None else None,
        }}
    
