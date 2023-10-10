from typing import List

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


class EnrollmentViewmodel:
    user: UserViewmodel
    state: ENROLLMENT_STATE
    date_subscribed: int

    def __init__(self, enrollment: Enrollment):
        self.state = enrollment.state
        self.date_subscribed = enrollment.date_subscribed

    def to_dict(self):
        return {
            "state": self.state.value,
            "date_subscribed": self.date_subscribed,
        }


class ActivityViewmodel:
    code: str
    title: str
    description: str
    activity_type: ACTIVITY_TYPE
    is_extensive: bool
    delivery_model: DELIVERY_MODEL
    start_date: int
    end_date: int  # minutes
    link: str
    place: str
    responsible_professors: List[UserViewmodel]
    speakers: List[SpeakerViewmodel]
    total_slots: int
    taken_slots: int
    accepting_new_enrollments: bool
    stop_accepting_new_enrollments_before: int
    enrollment: EnrollmentViewmodel

    def __init__(self, activity_and_state: dict):
        self.code = activity_and_state['activity'].code
        self.title = activity_and_state['activity'].title
        self.description = activity_and_state['activity'].description
        self.activity_type = activity_and_state['activity'].activity_type
        self.is_extensive = activity_and_state['activity'].is_extensive
        self.delivery_model = activity_and_state['activity'].delivery_model
        self.start_date = activity_and_state['activity'].start_date
        self.end_date = activity_and_state['activity'].end_date
        self.link = activity_and_state['activity'].link
        self.place = activity_and_state['activity'].place
        self.responsible_professors = [UserViewmodel(professor) for professor in
                                       activity_and_state['activity'].responsible_professors]
        self.speakers = [SpeakerViewmodel(speaker) for speaker in activity_and_state['activity'].speakers]
        self.total_slots = activity_and_state['activity'].total_slots
        self.taken_slots = activity_and_state['activity'].taken_slots
        self.accepting_new_enrollments = activity_and_state['activity'].accepting_new_enrollments
        self.stop_accepting_new_enrollments_before = activity_and_state[
            'activity'].stop_accepting_new_enrollments_before
        self.enrollment = EnrollmentViewmodel(
            activity_and_state['enrollment']) if "enrollment" in activity_and_state else None

    def to_dict(self):
        to_return = {
            "activity": {"code": self.code,
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
                         },
            "enrollment": self.enrollment.to_dict() if self.enrollment is not None else None,
        }

        return {k: v for k, v in to_return.items() if v is not None}


class GetAllActivitiesLoggedViewmodel:
    activities_logged: dict

    def __init__(self, activities_logged: dict):
        self.activities_logged = activities_logged

    def to_dict(self):
        return {
            "all_activities_and_user_enrollments": [ActivityViewmodel(activity_and_state).to_dict() for activity_code, activity_and_state in self.activities_logged.items()],
            "message": "the activities were retrieved to the user"
        }
