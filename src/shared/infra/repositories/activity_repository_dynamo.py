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


    def __init__(self):
        self.dynamo = DynamoDatasource(endpoint_url=Environments.get_envs().endpoint_url,
                                       dynamo_table_name=Environments.get_envs().dynamo_table_name,
                                       region=Environments.get_envs().region,
                                       partition_key=Environments.get_envs().dynamo_partition_key,
                                       sort_key=Environments.get_envs().dynamo_sort_key)

    def get_enrollment(self, user_id: str, code: str) -> Enrollment:
        pass

    def get_activity(self, code: str) -> Activity:

        query_string = Key(self.dynamo.partition_key).eq(self.activity_partition_key_format(code))

        response = self.dynamo.query(
            key_condition_expression=query_string,
            Select="ALL_ATTRIBUTES"
        )

        if response.get("Items") is None:
            return None

        activity_data = response.get("Items")[0]

        activity_data["taken_slots"] = len(response.get("Items")) - 1

        activity = ActivityDynamoDTO.from_dynamo(activity_data).to_entity()

        return activity

    def update_enrollment(self, user_id: str, code: str, new_state: ENROLLMENT_STATE) -> Enrollment:
        pass

    def get_activity_with_enrollments(self, code: str) -> Tuple[Activity, List[Enrollment]]:
        pass

    def create_enrollment(self, enrollment: Enrollment) -> Enrollment:
        item = EnrollmentDynamoDTO.from_entity(enrollment).to_dynamo()

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
        pass

    def delete_activity(self, code: str) -> Activity:
        pass

    def batch_update_enrollment(self, enrollments: List[Enrollment], state: ENROLLMENT_STATE) -> List[Enrollment]:
        pass

    def get_all_activities_admin(self) -> List[Tuple[Activity, List[Enrollment]]]:
        pass

    def get_all_activities(self) -> List[Activity]:
        pass

    def create_activity(self, activity: Activity) -> Activity:
        activity_dto = ActivityDynamoDTO.from_entity(activity)
        item = activity_dto.to_dynamo()

        resp = self.dynamo.put_item(partition_key=self.activity_partition_key_format(activity.code),
                                    sort_key=self.activity_sort_key_format(activity.code), item=item,
                                    is_decimal=True)

        return activity

    def get_enrollments_by_user_id(self, user_id: str) -> List[Enrollment]:
        pass
