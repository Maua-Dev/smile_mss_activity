from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL


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


class ActivityViewmodel:
    code: str
    title: str
    description: str
    activity_type: ACTIVITY_TYPE
    is_extensive: bool
    delivery_model: DELIVERY_MODEL
    start_date: int
    end_date: int
    link: str
    place: str
    responsible_professors: List[UserViewmodel]
    speakers: List[SpeakerViewmodel]
    total_slots: int
    taken_slots: int
    accepting_new_enrollments: bool
    stop_accepting_new_enrollments_before: int

    def __init__(self, activity: Activity):
        self.code = activity.code
        self.title = activity.title
        self.description = activity.description
        self.activity_type = activity.activity_type.value
        self.is_extensive = activity.is_extensive
        self.delivery_model = activity.delivery_model.value
        self.start_date = activity.start_date
        self.end_date = activity.end_date
        self.link = activity.link
        self.place = activity.place
        self.responsible_professors = [UserViewmodel(professor) for professor in activity.responsible_professors]
        self.speakers = [SpeakerViewmodel(speaker) for speaker in activity.speakers]
        self.total_slots = activity.total_slots
        self.taken_slots = activity.taken_slots
        self.accepting_new_enrollments = activity.accepting_new_enrollments
        self.stop_accepting_new_enrollments_before = activity.stop_accepting_new_enrollments_before

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "activity_type": self.activity_type,
            "is_extensive": self.is_extensive,
            "delivery_model": self.delivery_model,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "link": self.link,
            "place": self.place,
            "responsible_professors": [(professor.to_dict()) for professor in self.responsible_professors],
            "speakers": [(speaker.to_dict()) for speaker in self.speakers],
            "total_slots": self.total_slots,
            "taken_slots": self.taken_slots,
            "accepting_new_enrollments": self.accepting_new_enrollments,
            "stop_accepting_new_enrollments_before": self.stop_accepting_new_enrollments_before,
        }


class DeleteActivityViewmodel:
    activity: ActivityViewmodel

    def __init__(self, activity: Activity):
        self.activity = ActivityViewmodel(activity)

    def to_dict(self):
        return {
            "activity": self.activity.to_dict(),
            "message": "the activity was deleted"}
