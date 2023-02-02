from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL


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
    # taken_slots: int
    accepting_new_enrollments: bool
    stop_accepting_new_enrollments_before: int  # milliseconds

    def __init__(self, code: str, title: str, description: str, activity_type: ACTIVITY_TYPE, is_extensive: bool,
                 delivery_model: DELIVERY_MODEL, start_date: int, duration: int, link: str, place: str,
                 responsible_professors: List[User], speakers: List[Speaker], total_slots: int,
                 accepting_new_enrollments: bool, stop_accepting_new_enrollments_before: int):
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
        )

    def to_dynamo(self):
        """
        Parse data from ActivityDynamoDTO to DynamoDB format
        """
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
        }

    def __eq__(self, other):
        return self.code == other.code and self.title == other.title and self.description == other.description and self.activity_type == other.activity_type and self.is_extensive == other.is_extensive and self.delivery_model == other.delivery_model and self.start_date == other.start_date and self.duration == other.duration and self.link == other.link and self.place == other.place and self.responsible_professors == other.responsible_professors and self.speakers == other.speakers and self.total_slots == other.total_slots and self.accepting_new_enrollments == other.accepting_new_enrollments and self.stop_accepting_new_enrollments_before == other.stop_accepting_new_enrollments_before
