import datetime
from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL


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
    duration: int  # minutes
    link: str
    place: str
    speakers: List[SpeakerViewmodel]
    total_slots: int
    taken_slots: int
    accepting_new_enrollments: bool
    stop_accepting_new_enrollments_before: int
    confirmation_code: str

    def __init__(self, activity: Activity):
        self.code = activity.code
        self.title = activity.title
        self.description = activity.description
        self.activity_type = activity.activity_type
        self.is_extensive = activity.is_extensive
        self.delivery_model = activity.delivery_model
        self.start_date = activity.start_date
        self.duration = activity.duration
        self.link = activity.link
        self.place = activity.place
        self.speakers = [SpeakerViewmodel(speaker)
                         for speaker in activity.speakers]
        self.total_slots = activity.total_slots
        self.taken_slots = activity.taken_slots
        self.accepting_new_enrollments = activity.accepting_new_enrollments
        self.stop_accepting_new_enrollments_before = activity.stop_accepting_new_enrollments_before
        self.confirmation_code = activity.confirmation_code

    def to_dict(self):
        return {
            "code": self.code,
            "title": self.title,
            "description": self.description,
            "activity_type": self.activity_type.value,
            "is_extensive": self.is_extensive,
            "delivery_model": self.delivery_model.value,
            "start_date": self.start_date,
            "duration": self.duration,
            "link": self.link,
            "place": self.place,
            "speakers": [speaker.to_dict() for speaker in self.speakers],
            "total_slots": self.total_slots,
            "taken_slots": self.taken_slots,
            "accepting_new_enrollments": self.accepting_new_enrollments,
            "stop_accepting_new_enrollments_before": self.stop_accepting_new_enrollments_before if self.stop_accepting_new_enrollments_before is not None else None,
            "confirmation_code": self.confirmation_code
        }


class GetAllActivitiesViewmodel:
    all_activities: List[Activity]

    def __init__(self, all_activities: List[Activity]):
        self.all_activities = all_activities

    def to_dict(self):
        return {
            "all_activities": [ActivityViewmodel(activity).to_dict() for activity in
                               self.all_activities],
            "message": "the activities were retrieved"
        }
