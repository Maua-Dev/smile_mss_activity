from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE


class ActivityDynamoDTO:
    code: str
    title: str
    description: str
    activity_type: ACTIVITY_TYPE
    is_extensive: bool
    delivery_model: DELIVERY_MODEL
    start_date: int  # milliseconds
    duration: int  # minutes
    link: str
    place: str
    responsible_professors: List[User]
    speakers: List[Speaker]
    total_slots: int
    taken_slots: int
    accepting_new_enrollments: bool
    stop_accepting_new_enrollments_before: int  # milliseconds
    confirmation_code: str

    def __init__(self, code: str, title: str, description: str, activity_type: ACTIVITY_TYPE, is_extensive: bool,
                 delivery_model: DELIVERY_MODEL, start_date: int, duration: int, link: str, place: str,
                 responsible_professors: List[User], speakers: List[Speaker], total_slots: int,
                 accepting_new_enrollments: bool, stop_accepting_new_enrollments_before: int, taken_slots: int = None, confirmation_code: str = None):
        self.code = code
        self.title = title
        self.description = description
        self.activity_type = activity_type
        self.is_extensive = is_extensive
        self.delivery_model = delivery_model
        self.start_date = start_date
        self.duration = duration
        self.link = link
        self.place = place
        self.responsible_professors = responsible_professors
        self.speakers = speakers
        self.total_slots = total_slots
        self.accepting_new_enrollments = accepting_new_enrollments
        self.stop_accepting_new_enrollments_before = stop_accepting_new_enrollments_before
        self.taken_slots = taken_slots
        self.confirmation_code = confirmation_code

    @staticmethod
    def from_entity(activity: Activity) -> "ActivityDynamoDTO":
        """
        Parse data from Activity entity to ActivityDynamoDTO
        """
        return ActivityDynamoDTO(
            code=activity.code,
            title=activity.title,
            description=activity.description,
            activity_type=activity.activity_type,
            is_extensive=activity.is_extensive,
            delivery_model=activity.delivery_model,
            start_date=activity.start_date,
            duration=activity.duration,
            link=activity.link,
            place=activity.place,
            responsible_professors=activity.responsible_professors,
            speakers=activity.speakers,
            total_slots=activity.total_slots,
            accepting_new_enrollments=activity.accepting_new_enrollments,
            stop_accepting_new_enrollments_before=activity.stop_accepting_new_enrollments_before,
            confirmation_code=activity.confirmation_code,
        )

    def to_dynamo(self):
        """
        Parse data from ActivityDynamoDTO to DynamoDB format
        """
        data = {
            "activity_code": self.code,
            "title": self.title,
            "description": self.description,
            "activity_type": self.activity_type.value,
            "is_extensive": self.is_extensive,
            "delivery_model": self.delivery_model.value,
            "start_date": self.start_date,
            "duration": self.duration,
            "link": self.link,
            "place": self.place,
            "responsible_professors": [{
                "name": professor.name,
                "user_id": professor.user_id,
                "role": professor.role.value,
            } for professor in self.responsible_professors],
            "speakers": [{
                "name": speaker.name,
                "bio": speaker.bio,
                "company": speaker.company,
            } for speaker in self.speakers],
            "total_slots": self.total_slots,
            "accepting_new_enrollments": self.accepting_new_enrollments,
            "stop_accepting_new_enrollments_before": self.stop_accepting_new_enrollments_before,
            "confirmation_code": self.confirmation_code,
            "entity": "activity",
        }

        data_without_none_values = {k: v for k, v in data.items() if v is not None}

        return data_without_none_values

    @staticmethod
    def from_dynamo(activity_data: dict):
        """
        Parse data from DynamoDB format to ActivityDynamoDTO
        """
        return ActivityDynamoDTO(
            code=activity_data.get("activity_code"),
            title=activity_data.get("title"),
            description=activity_data.get("description"),
            activity_type=ACTIVITY_TYPE(activity_data.get("activity_type")),
            is_extensive=bool(activity_data.get("is_extensive")),
            delivery_model=DELIVERY_MODEL(activity_data.get("delivery_model")),
            start_date=int(activity_data.get("start_date")),
            duration=int(activity_data.get("duration")),
            link=activity_data.get("link"),
            place=activity_data.get("place"),
            responsible_professors=[User(
                name=professor["name"],
                user_id=professor["user_id"],
                role=ROLE(professor["role"]),
            ) for professor in activity_data["responsible_professors"]],
            speakers=[Speaker(
                speaker["name"],
                speaker["bio"],
                speaker["company"],
            ) for speaker in activity_data["speakers"]],
            total_slots=int(activity_data.get("total_slots")),
            accepting_new_enrollments=bool(activity_data.get("accepting_new_enrollments")),
            stop_accepting_new_enrollments_before=int(activity_data.get("stop_accepting_new_enrollments_before")) if activity_data.get("stop_accepting_new_enrollments_before") is not None else None,
            taken_slots=int(activity_data.get("taken_slots")),
            confirmation_code=activity_data.get("confirmation_code") if activity_data.get("confirmation_code") is not None else None,
        )

    def to_entity(self) -> Activity:
        """
        Parse data from ActivityDynamoDTO to Activity entity
        """
        return Activity(
            code=self.code,
            title=self.title,
            description=self.description,
            activity_type=self.activity_type,
            is_extensive=self.is_extensive,
            delivery_model=self.delivery_model,
            start_date=self.start_date,
            duration=self.duration,
            link=self.link,
            place=self.place,
            responsible_professors=self.responsible_professors,
            speakers=self.speakers,
            total_slots=self.total_slots,
            accepting_new_enrollments=self.accepting_new_enrollments,
            stop_accepting_new_enrollments_before=self.stop_accepting_new_enrollments_before,
            taken_slots=self.taken_slots,
            confirmation_code=self.confirmation_code,
        )

    def __eq__(self, other):
        return self.code == other.code and self.title == other.title and self.description == other.description and self.activity_type == other.activity_type and self.is_extensive == other.is_extensive and self.delivery_model == other.delivery_model and self.start_date == other.start_date and self.duration == other.duration and self.link == other.link and self.place == other.place and self.responsible_professors == other.responsible_professors and self.speakers == other.speakers and self.total_slots == other.total_slots and self.accepting_new_enrollments == other.accepting_new_enrollments and self.stop_accepting_new_enrollments_before == other.stop_accepting_new_enrollments_before and self.taken_slots == other.taken_slots and self.confirmation_code == other.confirmation_code
