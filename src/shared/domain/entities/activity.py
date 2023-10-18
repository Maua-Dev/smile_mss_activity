import abc
from typing import List, Optional

from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class Activity(abc.ABC):
    code: str
    title: str
    description: Optional[str]
    activity_type: ACTIVITY_TYPE
    is_extensive: bool
    delivery_model: DELIVERY_MODEL
    start_date: int  # milliseconds
    end_date: int  # milliseconds
    link: Optional[str]
    place: Optional[str]
    responsible_professors: Optional[List[User]]
    speakers: Optional[List[Speaker]]
    total_slots: int
    taken_slots: int
    accepting_new_enrollments: bool
    stop_accepting_new_enrollments_before: int  # milliseconds
    confirmation_code: str

    def __init__(self, code: str, title: str, activity_type: ACTIVITY_TYPE, is_extensive: bool,
                 delivery_model: DELIVERY_MODEL, start_date: int, end_date: int, 
                total_slots: int, taken_slots: int,
                 accepting_new_enrollments: bool, stop_accepting_new_enrollments_before: int, confirmation_code: str,link: Optional[str] = None,
                 place: Optional[str]=None,description: Optional[str]=None,responsible_professors: Optional[List[User]]=None,speakers: Optional[List[Speaker]]=None):

        if not self.validate_activity_code(code):
            raise EntityError("code")
        self.code = code

        if type(title) != str:
            raise EntityError("title")
        self.title = title

        if type(description) != str and description is not None:
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

        if type(start_date) != int:
            raise EntityError("start_date")
        if not 1000000000000 < start_date < 10000000000000:
            raise EntityError("start_date")
        self.start_date = start_date

        if type(end_date) != int:
            raise EntityError("end_date")
        self.end_date = end_date

        if link is None and place is None:
            raise EntityError("link or place")

        if type(link) != str and link is not None:
            raise EntityError("link")

        if type(place) != str and place is not None:
            raise EntityError("place")

        self.link = link
        self.place = place

        if type(responsible_professors) != list and responsible_professors is not None: 
            raise EntityError("responsible_professors")

        elif responsible_professors is not None and not all([type(encharged_professor) == User for encharged_professor in
                      responsible_professors if encharged_professor]):  # check if all elements are User
            raise EntityError("responsible_professors")

        elif responsible_professors is not None and not all([encharged_professor.role == ROLE.PROFESSOR for encharged_professor in
                      responsible_professors]):  # check if all elements are professors
            raise EntityError("responsible_professors")

        self.responsible_professors = responsible_professors

        if type(speakers) != list and speakers is not None:
            raise EntityError("speakers")

        if speakers is not None and not all([type(speaker) == Speaker for speaker in speakers if speaker is not None]):  # check if all elements are Speaker
            raise EntityError("speakers")
        self.speakers = speakers

        if type(total_slots) != int:
            raise EntityError("total_slots")
        if total_slots < 0:
            raise EntityError("total_slots")
        self.total_slots = total_slots

        if type(taken_slots) != int:
            raise EntityError("taken_slots")
        if taken_slots < 0:
            raise EntityError("taken_slots")
        self.taken_slots = taken_slots

        if type(accepting_new_enrollments) != bool:
            raise EntityError("accepting_new_enrollments")
        self.accepting_new_enrollments = accepting_new_enrollments

        if stop_accepting_new_enrollments_before is None:
            self.stop_accepting_new_enrollments_before = stop_accepting_new_enrollments_before
            
        if stop_accepting_new_enrollments_before is not None:
            
            if type(stop_accepting_new_enrollments_before) != int:
                raise EntityError("stop_accepting_new_enrollments_before")
            
            if not 1000000000000 < stop_accepting_new_enrollments_before < 10000000000000:
                raise EntityError("stop_accepting_new_enrollments_before")

        self.stop_accepting_new_enrollments_before = stop_accepting_new_enrollments_before

        if confirmation_code is not None:
            if not self.validate_confirmation_code(confirmation_code):
                raise EntityError("confirmation_code")
        self.confirmation_code = confirmation_code

    @staticmethod
    def validate_confirmation_code(confirmation_code: str) -> bool:
        if type(confirmation_code) != str:
            return False
        if len(confirmation_code) != 6:
            return False
        if not confirmation_code.isnumeric():
            return False
        return True

    @staticmethod
    def validate_activity_code(code: str) -> bool:
        if type(code) != str:
            return False
        if len(code) <= 0:
            return False
        return True

    def __repr__(self):
        return f"Activity({self.code}, {self.title}, {self.description}, {self.activity_type}, {self.is_extensive}, {self.delivery_model}, {self.start_date}, {self.end_date}, {self.link}, {self.place}, {self.responsible_professors}, {self.speakers}, {self.total_slots}, {self.taken_slots}, {self.accepting_new_enrollments}, {self.stop_accepting_new_enrollments_before}, {self.confirmation_code})"

    def __eq__(self, other):
        return self.code == other.code and self.title == other.title and self.description == other.description and self.activity_type == other.activity_type and self.is_extensive == other.is_extensive and self.delivery_model == other.delivery_model and self.start_date == other.start_date and self.end_date == other.end_date and self.link == other.link and self.place == other.place and self.responsible_professors == other.responsible_professors and self.speakers == other.speakers and self.total_slots == other.total_slots and self.taken_slots == other.taken_slots and self.accepting_new_enrollments == other.accepting_new_enrollments and self.stop_accepting_new_enrollments_before == other.stop_accepting_new_enrollments_before and self.confirmation_code == other.confirmation_code
