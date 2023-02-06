from typing import List, Tuple

from boto3.dynamodb.conditions import Key

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.environments import Environments
from src.shared.infra.dto.activity_dynamo_dto import ActivityDynamoDTO
from src.shared.infra.dto.enrollment_dynamo_dto import EnrollmentDynamoDTO
from src.shared.infra.external.dynamo.datasources.dynamo_datasource import DynamoDatasource


class ActivityRepositoryDynamo(IActivityRepository):
    dynamo: DynamoDatasource

    @staticmethod
    def activity_partition_key_format(activity_code: str) -> str:
        return f"{activity_code}"

    @staticmethod
    def activity_sort_key_format(activity_code: str) -> str:
        return f"activity#{activity_code}"

    @staticmethod
    def enrollment_partition_key_format(activity_code: str) -> str:
        return f"{activity_code}"

    @staticmethod
    def enrollment_sort_key_format(user_id: str) -> str:
        return f"enrollment#{user_id}"

    @staticmethod
    def enrollment_gsi_partition_key_format(user_id: str) -> str:
        return f"{user_id}"

    @staticmethod
    def enrollment_gsi_sort_key_format(activity_code: str) -> str:
        return f"enrollment#{activity_code}"

    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)

    def get_enrollment(self, user_id: str, code: str) -> Enrollment:

        enrollment_data = self.dynamo.get_item(
            partition_key=self.enrollment_partition_key_format(code),
            sort_key=self.enrollment_sort_key_format(user_id)
        )

        if "Item" not in enrollment_data:
            return None

        enrollment = EnrollmentDynamoDTO.from_dynamo(enrollment_data.get("Item")).to_entity()

        if enrollment.state != ENROLLMENT_STATE.DROPPED:
            return enrollment

        return None

    def get_activity(self, code: str) -> Activity:

        query_string = Key(self.dynamo.partition_key).eq(self.activity_partition_key_format(code))

        response = self.dynamo.query(
            key_condition_expression=query_string,
            Select="ALL_ATTRIBUTES"
        )

        if len(response.get("Items")) == 0:
            return None
        elif response.get("Items")[0]["entity"] == "enrollment":
            return None

        activity_data = response.get("Items")[0]

        activity_data["taken_slots"] = 0

        for enrollment in response.get("Items")[1:]:
            if enrollment["state"] == ENROLLMENT_STATE.ENROLLED.value or enrollment["state"] == ENROLLMENT_STATE.COMPLETED.value:
                activity_data["taken_slots"] += 1

        activity = ActivityDynamoDTO.from_dynamo(activity_data).to_entity()

        return activity

    def update_enrollment(self, user_id: str, code: str, new_state: ENROLLMENT_STATE) -> Enrollment:

        response = self.dynamo.update_item(
            partition_key=self.enrollment_partition_key_format(code),
            sort_key=self.enrollment_sort_key_format(user_id),
            update_dict={"state": new_state.value})

        if "Attributes" not in response:
            return None

        return EnrollmentDynamoDTO.from_dynamo(response["Attributes"]).to_entity()

    def get_activity_with_enrollments(self, code: str) -> Tuple[Activity, List[Enrollment]]:

        query_string = Key(self.dynamo.partition_key).eq(self.activity_partition_key_format(code))

        response = self.dynamo.query(
            key_condition_expression=query_string,
            Select="ALL_ATTRIBUTES"
        )

        if len(response.get("Items")) == 0:
            return None, None

        activity_data = response.get("Items")[0]

        activity_data["taken_slots"] = 0
        enrollments = list()

        for enrollment in response.get("Items")[1:]:
            enrollments.append(EnrollmentDynamoDTO.from_dynamo(enrollment).to_entity())
            if enrollment["state"] == ENROLLMENT_STATE.ENROLLED.value or enrollment[
                "state"] == ENROLLMENT_STATE.COMPLETED.value:
                activity_data["taken_slots"] += 1

        activity = ActivityDynamoDTO.from_dynamo(activity_data).to_entity()

        return activity, enrollments

    def create_enrollment(self, enrollment: Enrollment) -> Enrollment:
        item = EnrollmentDynamoDTO.from_entity(enrollment).to_dynamo()
        item["GSI1-PK"] = self.enrollment_gsi_partition_key_format(enrollment.user_id)
        item["GSI1-SK"] = self.enrollment_gsi_sort_key_format(enrollment.activity_code)
        response = self.dynamo.put_item(
            item=item,
            partition_key=self.enrollment_partition_key_format(enrollment.activity_code),
            sort_key=self.enrollment_sort_key_format(enrollment.user_id),
            is_decimal=True
        )

        return enrollment

    def update_activity(self, code: str, new_title: str = None, new_description: str = None,
                        new_activity_type: ACTIVITY_TYPE = None, new_is_extensive: bool = None,
                        new_delivery_model: DELIVERY_MODEL = None, new_start_date: int = None, new_duration: int = None,
                        new_link: str = None, new_place: str = None, new_responsible_professors: List[User] = None,
                        new_speakers: List[Speaker] = None, new_total_slots: int = None, new_taken_slots: int = None,
                        new_accepting_new_enrollments: bool = None,
                        new_stop_accepting_new_enrollments_before: int = None) -> Activity:

        new_activity = Activity(
            code=code,
            title=new_title,
            description=new_description,
            activity_type=new_activity_type,
            is_extensive=new_is_extensive,
            delivery_model=new_delivery_model,
            start_date=new_start_date,
            duration=new_duration,
            link=new_link,
            place=new_place,
            responsible_professors=new_responsible_professors,
            speakers=new_speakers,
            total_slots=new_total_slots,
            taken_slots=new_taken_slots,
            accepting_new_enrollments=new_accepting_new_enrollments,
            stop_accepting_new_enrollments_before=new_stop_accepting_new_enrollments_before
        )

        new_activity_dto = ActivityDynamoDTO.from_entity(new_activity)

        new_activity_dto = new_activity_dto.to_dynamo()

        response = self.dynamo.hard_update_item(
            partition_key=self.activity_partition_key_format(code),
            sort_key=self.activity_sort_key_format(code),
            item=new_activity_dto,
        )

        return new_activity

    def delete_activity(self, code: str) -> Activity:

        taken_slots = self.get_activity(code).taken_slots

        response = self.dynamo.delete_item(
            partition_key=self.activity_partition_key_format(code),
            sort_key=self.activity_sort_key_format(code))

        response["Attributes"]["taken_slots"] = taken_slots

        return ActivityDynamoDTO.from_dynamo(response["Attributes"]).to_entity()

    def batch_update_enrollment(self, enrollments: List[Enrollment], state: ENROLLMENT_STATE) -> List[Enrollment]:
        to_update_list = list()

        enrollments_dtos = [EnrollmentDynamoDTO.from_entity(enrollment).to_dynamo() for enrollment in enrollments]

        for enrollment in enrollments_dtos:
            enrollment["state"] = state.value
            data = {
                "PK": self.enrollment_partition_key_format(enrollment['activity_code']),
                "SK": self.enrollment_sort_key_format(enrollment['user_id']),
                "GSI1-PK": self.enrollment_gsi_partition_key_format(enrollment['user_id']),
                "GSI1-SK": self.enrollment_gsi_sort_key_format(enrollment['activity_code'])
            }
            data.update(enrollment)

            to_update_list.append(data)

        response = self.dynamo.batch_write_items(to_update_list)

        new_enrollments = list()

        for enrollment in enrollments:
            enrollment.state = state
            new_enrollments.append(enrollment)

        return new_enrollments

    def get_all_activities_admin(self) -> List[Tuple[Activity, List[Enrollment]]]:
        response = self.dynamo.get_all_items()

        activities_dict = list()
        enrollments = dict()
        for item in response["Items"]:
            if item["entity"] == "activity":
                activities_dict.append(item)

            elif item["entity"] == "enrollment":
                enrollments[item["activity_code"]] = enrollments.get(item["activity_code"], list())
                enrollments[item["activity_code"]].append(EnrollmentDynamoDTO.from_dynamo(item).to_entity())

        activities_with_enrollments = list()
        for activity in activities_dict:
            activity_to_add = activity
            activity_to_add["taken_slots"] = len(
                [enrollment for enrollment in enrollments.get(activity["activity_code"], list()) if
                 enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.COMPLETED])
            activities_with_enrollments.append((ActivityDynamoDTO.from_dynamo(activity_to_add).to_entity(), enrollments.get(activity["activity_code"], list())))

        return activities_with_enrollments

    def get_all_activities(self) -> List[Activity]:
        response = self.dynamo.get_all_items()

        activities_dict = list()
        enrollments = dict()
        for item in response["Items"]:
            if item["entity"] == "activity":
                activities_dict.append(item)

            elif item["entity"] == "enrollment":
                enrollments[item["activity_code"]] = enrollments.get(item["activity_code"], list())
                enrollments[item["activity_code"]].append(EnrollmentDynamoDTO.from_dynamo(item).to_entity())

        activities = list()
        for activity in activities_dict:
            activity_to_add = activity
            activity_to_add["taken_slots"] = len([enrollment for enrollment in enrollments.get(activity["activity_code"], list()) if enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.COMPLETED])
            activities.append(ActivityDynamoDTO.from_dynamo(activity_to_add).to_entity())

        return activities

    def create_activity(self, activity: Activity) -> Activity:
        activity_dto = ActivityDynamoDTO.from_entity(activity)
        item = activity_dto.to_dynamo()

        resp = self.dynamo.put_item(partition_key=self.activity_partition_key_format(activity.code),
                                    sort_key=self.activity_sort_key_format(activity.code), item=item,
                                    is_decimal=True)

        return activity

    def get_enrollments_by_user_id(self, user_id: str) -> List[Enrollment]:
        query_string = Key("GSI1-PK").eq(user_id) & Key("GSI1-SK").begins_with("enrollment#")

        response = self.dynamo.query(
            key_condition_expression=query_string,
            IndexName="GSI1"
        )

        enrollments = list()
        for item in response["Items"]:
            if item["state"] == ENROLLMENT_STATE.ENROLLED.value:
                enrollments.append(EnrollmentDynamoDTO.from_dynamo(item).to_entity())

        return enrollments
