import abc
import datetime
from typing import List

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
    duration: int  # minutes
    link: str
    place: str
    responsible_professors: List[User]
    speakers: List[Speaker]
    total_slots: int
    taken_slots: int
    accepting_new_enrollments: bool
    stop_accepting_new_enrollments_before: datetime.datetime

    def __init__(self, code: str, title: str, description: str, activity_type: ACTIVITY_TYPE, is_extensive: bool,
                 delivery_model: DELIVERY_MODEL, start_date: datetime.datetime, duration: int, link: str, place: str,
                 responsible_professors: List[User], speakers: List[Speaker], total_slots: int, taken_slots: int,
                 accepting_new_enrollments: bool, stop_accepting_new_enrollments_before: datetime.datetime):
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
        self.activity_type = activity_type

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

        if link is None and place is None:
            raise EntityError("link or place")

        if type(link) != str and link is not None:
            raise EntityError("link")

        if type(place) != str and place is not None:
            raise EntityError("place")

        self.link = link
        self.place = place

        if type(responsible_professors) != list:
            raise EntityError("responsible_professors")

        elif not all([type(encharged_professor) == User for encharged_professor in
                      responsible_professors]):  # check if all elements are User
            raise EntityError("responsible_professors")

        elif not all([encharged_professor.role == ROLE.PROFESSOR for encharged_professor in
                      responsible_professors]):  # check if all elements are professors
            raise EntityError("responsible_professors")

        self.responsible_professors = responsible_professors

        if type(speakers) != list:
            raise EntityError("speakers")

        if not all([type(speaker) == Speaker for speaker in speakers]):  # check if all elements are Speaker
            raise EntityError("speakers")
        self.speakers = speakers

        if type(total_slots) != int:
            raise EntityError("total_slots")
        self.total_slots = total_slots

        if type(taken_slots) != int:
            raise EntityError("taken_slots")
        self.taken_slots = taken_slots

        if type(accepting_new_enrollments) != bool:
            raise EntityError("accepting_new_enrollments")
        self.accepting_new_enrollments = accepting_new_enrollments

        if type(stop_accepting_new_enrollments_before) == datetime.datetime:
            if stop_accepting_new_enrollments_before > start_date:
                raise EntityError("stop_accepting_new_enrollments_before")

        elif stop_accepting_new_enrollments_before is None:
            self.stop_accepting_new_enrollments_before = stop_accepting_new_enrollments_before

        else:
            raise EntityError("stop_accepting_new_enrollments_before")

        self.stop_accepting_new_enrollments_before = stop_accepting_new_enrollments_before

    def __repr__(self):
        return f"Activity(code={self.code}, title={self.title}, description={self.description}, activity_type={self.activity_type.value}, is_extensive={self.is_extensive}, delivery_model={self.delivery_model.value}, start_date={self.start_date.isoformat()}, duration={self.duration}, link={self.link}, place={self.place} responsible_professors={self.responsible_professors}, speakers={self.speakers}, total_slots={self.total_slots}, taken_slots={self.taken_slots}, accepting_new_enrollments={self.accepting_new_enrollments}, stop_accepting_new_enrollments_before={self.stop_accepting_new_enrollments_before.isoformat() if self.stop_accepting_new_enrollments_before is not None else None})"

    def __eq__(self, other):
        return self.code == other.code and self.title == other.title and self.description == other.description and self.activity_type == other.activity_type and self.is_extensive == other.is_extensive and self.delivery_model == other.delivery_model and self.start_date == other.start_date and self.duration == other.duration and self.link == other.link and self.place == other.place and self.responsible_professors == other.responsible_professors and self.speakers == other.speakers and self.total_slots == other.total_slots and self.taken_slots == other.taken_slots and self.accepting_new_enrollments == other.accepting_new_enrollments and self.stop_accepting_new_enrollments_before == other.stop_accepting_new_enrollments_before
