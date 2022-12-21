import abc
import datetime
from typing import List

from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class Activity(abc.ABC):
    code: str
    title: str
    description: str
    activity_type: ACTIVITY_TYPE
    is_extensive: bool
    delivery_model: DELIVERY_MODEL
    start_date: datetime.datetime
    duration: int #minutes
    encharged_professors: List[User]
    speakers: List[Speaker]
    enrollments: List[Enrollment]
    total_slots: int
    taken_slots: int
    accepting_new_subscriptions: bool
    stop_accepting_new_subscriptions_before: datetime.datetime

    def __init__(self, code: str, title: str, description: str, activity_type: ACTIVITY_TYPE, is_extensive: bool, delivery_model: DELIVERY_MODEL, start_date: datetime.datetime, duration: int, encharged_professors: List[User], speakers: List[Speaker], enrollments: List[Enrollment], total_slots: int, taken_slots: int, accepting_new_subscriptions: bool, stop_accepting_new_subscriptions_before: datetime.datetime):
        if type(code) != str:
            raise EntityError("code")
        self.code = code

        if type(title) != str:
            raise EntityError("title")
        self.title = title

        if type(description) != str:
            raise EntityError("description")
        self.description = description

        if type(activity_type) != ACTIVITY_TYPE:
            raise EntityError("activity_type")
        self.type = activity_type

        if type(is_extensive) != bool:
            raise EntityError("is_extensive")
        self.is_extensive = is_extensive

        if type(delivery_model) != DELIVERY_MODEL:
            raise EntityError("delivery_model")
        self.delivery_model = delivery_model

        if type(start_date) != datetime.datetime:
            raise EntityError("start_date")
        self.start_date = start_date

        if type(duration) != int:
            raise EntityError("duration")
        self.duration = duration

        if type(encharged_professors) != list:
            raise EntityError("encharged_professors")

        if not all([type(encharged_professor) == User for encharged_professor in encharged_professors]): # check if all elements are User
            raise EntityError("encharged_professors")

        if not all([encharged_professor.role == ROLE.PROFESSOR for encharged_professor in encharged_professors]):  # check if all elements are professors
            raise EntityError("encharged_professors")

        self.encharged_professors = encharged_professors

        if type(speakers) != list:
            raise EntityError("speakers")

        if not all([type(speaker) == Speaker for speaker in speakers]): # check if all elements are Speaker
            raise EntityError("speakers")
        self.speakers = speakers

        if type(enrollments) != list:
            raise EntityError("enrollments")

        if not all([type(enrollment) == Enrollment for enrollment in enrollments]): # check if all elements are Enrollment
            raise EntityError("enrollments")
        self.enrollments = enrollments

        if type(total_slots) != int:
            raise EntityError("total_slots")
        self.total_slots = total_slots

        if type(taken_slots) != int:
            raise EntityError("taken_slots")
        self.taken_slots = taken_slots

        if type(accepting_new_subscriptions) != bool:
            raise EntityError("accepting_new_subscriptions")
        self.accepting_new_subscriptions = accepting_new_subscriptions

        if type(stop_accepting_new_subscriptions_before) != datetime.datetime:
            raise EntityError("stop_accepting_new_subscriptions_before")
        self.stop_accepting_new_subscriptions_before = stop_accepting_new_subscriptions_before

    def __repr__(self):
        return f"Activity(code={self.code}, title={self.title}, description={self.description}, activity_type={self.activity_type.value}, is_extensive={self.is_extensive}, delivery_model={self.delivery_model.value}, start_date={self.start_date.isoformat()}, duration={self.duration}, encharged_professors={self.encharged_professors}, speakers={self.speakers}, enrollments={self.enrollments}, total_slots={self.total_slots}, taken_slots={self.taken_slots}, accepting_new_subscriptions={self.accepting_new_subscriptions}, stop_accepting_new_subscriptions_before={self.stop_accepting_new_subscriptions_before.isoformat()})"

    def __eq__(self, other):
        return self.code == other.code and self.title == other.title and self.description == other.description and self.activity_type == other.activity_type and self.is_extensive == other.is_extensive and self.delivery_model == other.delivery_model and self.start_date == other.start_date and self.duration == other.duration and self.encharged_professors == other.encharged_professors and self.speakers == other.speakers and self.enrollments == other.enrollments and self.total_slots == other.total_slots and self.taken_slots == other.taken_slots and self.accepting_new_subscriptions == other.accepting_new_subscriptions and self.stop_accepting_new_subscriptions_before == other.stop_accepting_new_subscriptions_before