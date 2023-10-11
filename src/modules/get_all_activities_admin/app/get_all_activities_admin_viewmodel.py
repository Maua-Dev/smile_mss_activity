from typing import List, Tuple

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
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


class UserInfoViewmodel:
    name: str
    user_id: str
    role: str
    email: str

    def __init__(self, user: UserInfo):
        self.name = user.name
        self.user_id = user.user_id
        self.role = user.role.value
        self.email = user.email

    def to_dict(self):
        return {
            "name": self.name,
            "user_id": self.user_id,
            "role": self.role,
            "email": self.email
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
    user: UserInfoViewmodel
    state: ENROLLMENT_STATE
    date_subscribed: int

    def __init__(self, enrollment: Enrollment, user: UserInfo):
        self.user = UserInfoViewmodel(user) if type(user) == UserInfo else "NOT_FOUND"
        self.state = enrollment.state
        self.date_subscribed = enrollment.date_subscribed

    def to_dict(self):
        return {
            "user": self.user.to_dict() if type(self.user) == UserInfoViewmodel else {
                'name': "NOT_FOUND",
                'user_id': "NOT_FOUND",
                'role': "NOT_FOUND",
                'email': "NOT_FOUND"
            },
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
    start_date: int # milliseconds
    end_date: int  # milliseconds
    link: str
    place: str
    responsible_professors: List[UserViewmodel]
    speakers: List[SpeakerViewmodel]
    total_slots: int
    taken_slots: int
    accepting_new_enrollments: bool
    stop_accepting_new_enrollments_before: int
    enrollments: List[EnrollmentViewmodel]
    confirmation_code: str

    def __init__(self, activity: Activity, enrollments: List[Tuple[Enrollment, User]]):
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
        self.responsible_professors = [UserViewmodel(professor) for professor in activity.responsible_professors]
        self.speakers = [SpeakerViewmodel(speaker) for speaker in activity.speakers]
        self.total_slots = activity.total_slots
        self.taken_slots = activity.taken_slots
        self.accepting_new_enrollments = activity.accepting_new_enrollments
        self.stop_accepting_new_enrollments_before = activity.stop_accepting_new_enrollments_before
        self.enrollments = [EnrollmentViewmodel(*enrollment) for enrollment in enrollments]
        self.confirmation_code = activity.confirmation_code

    def to_dict(self):
        return {
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
                         "confirmation_code": self.confirmation_code},
            "enrollments": [enrollment.to_dict() for enrollment in self.enrollments],
        }


class GetAllActivitiesAdminViewmodel:
    all_activities_dict: dict

    def __init__(self, all_activities_dict: dict):
        self.all_activities_dict = all_activities_dict

    def to_dict(self):
        return {
            "all_activities_with_enrollments": [ActivityViewmodel(self.all_activities_dict[activity_code]['activity'],
                                                                  self.all_activities_dict[activity_code][
                                                                      'enrollments']).to_dict() for activity_code in
                                                self.all_activities_dict],
            "message": "the activities were retrieved by admin"
        }
