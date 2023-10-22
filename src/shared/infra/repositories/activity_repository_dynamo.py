from decimal import Decimal
import hashlib
import os
from typing import List, Tuple

import boto3
from boto3.dynamodb.conditions import Key

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.environments import Environments
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.utils.compose_deleted_user_email import compose_deleted_user_email
from src.shared.helpers.utils.compose_enrolled_email import compose_enrolled_email
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
                                       sort_key=Environments.get_envs().dynamo_sort_key,
                                       gsi_partition_key=Environments.get_envs().dynamo_gsi_partition_key,
                                       gsi_sort_key=Environments.get_envs().dynamo_gsi_sort_key)

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

        if activity_data['entity'] == "enrollment":
            return None, None

        activity_data["taken_slots"] = 0
        enrollments = list()

        for enrollment in response.get("Items")[1:]:
            enrollments.append(EnrollmentDynamoDTO.from_dynamo(enrollment).to_entity())
            if enrollment["state"] == ENROLLMENT_STATE.ENROLLED.value or enrollment[
                "state"] == ENROLLMENT_STATE.COMPLETED.value:
                activity_data["taken_slots"] += 1

        enrollments.sort(key=lambda x: (x.state != ENROLLMENT_STATE.COMPLETED, x.date_subscribed))

        activity = ActivityDynamoDTO.from_dynamo(activity_data).to_entity()

        return activity, enrollments

    def create_enrollment(self, enrollment: Enrollment) -> Enrollment:
        item = EnrollmentDynamoDTO.from_entity(enrollment).to_dynamo()
        item[self.dynamo.gsi_partition_key] = self.enrollment_gsi_partition_key_format(enrollment.user_id)
        item[self.dynamo.gsi_sort_key] = self.enrollment_gsi_sort_key_format(enrollment.activity_code)
        response = self.dynamo.put_item(
            item=item,
            partition_key=self.enrollment_partition_key_format(enrollment.activity_code),
            sort_key=self.enrollment_sort_key_format(enrollment.user_id),
            is_decimal=True
        )

        return enrollment

    def update_activity(self, code: str, new_title: str = None, new_description: str = None,
                        new_activity_type: ACTIVITY_TYPE = None, new_is_extensive: bool = None,
                        new_delivery_model: DELIVERY_MODEL = None, new_start_date: int = None, new_end_date: int = None,
                        new_link: str = None, new_place: str = None, new_responsible_professors: List[User] = None,
                        new_speakers: List[Speaker] = None, new_total_slots: int = None, new_taken_slots: int = None,
                        new_accepting_new_enrollments: bool = None,
                        new_stop_accepting_new_enrollments_before: int = None, new_confirmation_code:str = None) -> Activity:
        
        activity_to_update = self.get_activity(code)

        if activity_to_update is None:
            return None
        

        update_dict = {
            "code": code,
            "title": new_title,
            "description": new_description,
            "activity_type": new_activity_type.value if new_activity_type is not None else None,
            "is_extensive": new_is_extensive,
            "delivery_model": new_delivery_model.value if new_delivery_model is not None else None,
            "start_date": Decimal(str(new_start_date)) if new_start_date is not None else None,
            "end_date": new_end_date,
            "link": new_link,
            "place": new_place,
            "responsible_professors": [{"name": professor.name, "user_id": professor.user_id, "role": professor.role.value} for professor in new_responsible_professors] if new_responsible_professors is not None else [],
            "speakers": [{"name": speaker.name, "bio": speaker.bio, "company": speaker.company} for speaker in new_speakers] if new_speakers is not None else [],
            "total_slots": new_total_slots,
            "taken_slots": new_taken_slots if new_taken_slots is not None else None,
            "accepting_new_enrollments": new_accepting_new_enrollments,
            "stop_accepting_new_enrollments_before": Decimal(str(new_stop_accepting_new_enrollments_before)) if new_stop_accepting_new_enrollments_before is not None else None,
            "confirmation_code": new_confirmation_code if new_confirmation_code is not None else None
        }

        update_dict_without_none_values = {
            k: v for k, v in update_dict.items() if v is not None}

        response = self.dynamo.update_item(
            partition_key=self.activity_partition_key_format(code),
            sort_key=self.activity_sort_key_format(code),
            update_dict=update_dict_without_none_values,
        )

        if "Attributes" not in response:
            return None
        
        return ActivityDynamoDTO.from_dynamo(response["Attributes"]).to_entity()

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
                self.dynamo.partition_key: self.enrollment_partition_key_format(enrollment['activity_code']),
                self.dynamo.sort_key: self.enrollment_sort_key_format(enrollment['user_id']),
                self.dynamo.gsi_partition_key: self.enrollment_gsi_partition_key_format(enrollment['user_id']),
                self.dynamo.gsi_sort_key: self.enrollment_gsi_sort_key_format(enrollment['activity_code'])
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
        query_string = Key(self.dynamo.gsi_partition_key).eq(user_id) & Key(self.dynamo.gsi_sort_key).begins_with("enrollment#")

        response = self.dynamo.query(
            key_condition_expression=query_string,
            IndexName="GSI1"
        )

        enrollments = list()
        for item in response["Items"]:
            if item["state"] == ENROLLMENT_STATE.ENROLLED.value or item["state"] == ENROLLMENT_STATE.IN_QUEUE.value:
                enrollments.append(EnrollmentDynamoDTO.from_dynamo(item).to_entity())

        return enrollments

    def get_enrollments_by_user_id_with_dropped(self, user_id: str) -> List[Enrollment]:
        query_string = Key(self.dynamo.gsi_partition_key).eq(user_id) & Key(self.dynamo.gsi_sort_key).begins_with("enrollment#")

        response = self.dynamo.query(
            key_condition_expression=query_string,
            IndexName="GSI1"
        )

        enrollments = list()
        for item in response["Items"]:
            enrollments.append(EnrollmentDynamoDTO.from_dynamo(item).to_entity())

        return enrollments

    def get_all_activities_logged(self, user_id: str) -> Tuple[List[Activity], List[Enrollment]]:
        response = self.dynamo.get_all_items()

        activities_dict = list()
        enrollments = dict()
        for item in response["Items"]:
            if item["entity"] == "activity":
                activities_dict.append(item)

            elif item["entity"] == "enrollment":
                enrollments[item["activity_code"]] = enrollments.get(item["activity_code"], list())
                enrollments[item["activity_code"]].append(EnrollmentDynamoDTO.from_dynamo(item).to_entity())

        user_enrollments = list()
        activities = list()
        for activity in activities_dict:
            activity_to_add = activity
            taken_slots = 0

            for enrollment in enrollments.get(activity["activity_code"], list()):
                if enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.COMPLETED:
                    taken_slots += 1
                if enrollment.user_id == user_id and (enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.IN_QUEUE or enrollment.state == ENROLLMENT_STATE.COMPLETED):
                    user_enrollments.append(enrollment)

            activity_to_add["taken_slots"] = taken_slots

            activities.append(ActivityDynamoDTO.from_dynamo(activity_to_add).to_entity())

        return activities, user_enrollments



    def batch_update_activities(self, to_update_activities: List[Activity]) -> List[Activity]:
        to_update_list = list()

        activities_dtos = [ActivityDynamoDTO.from_entity(activity).to_dynamo() for activity in to_update_activities]

        for activity in activities_dtos:
            data = {
                self.dynamo.partition_key: self.activity_partition_key_format(activity['activity_code']),
                self.dynamo.sort_key: self.activity_sort_key_format(activity['activity_code']),
            }
            data.update(activity)

            to_update_list.append(data)

        response = self.dynamo.batch_write_items(to_update_list)

        return to_update_activities

    def send_enrolled_email(self, user: UserInfo, activity: Activity):

        if not user.accepted_notifications_email:
            print("User has not accepted notifications email")
            return True

        try:
            client_ses = boto3.client('ses', region_name=os.environ.get('SES_REGION'))

            composed_html = compose_enrolled_email(activity, user)
            response = client_ses.send_email(
                Destination={
                    'ToAddresses': [
                        user.email,
                    ],
                    'BccAddresses':
                        [
                            os.environ.get("HIDDEN_COPY")
                        ]
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': "UTF-8",
                            'Data': composed_html,
                        },
                    },
                    'Subject': {
                        'Charset': "UTF-8",
                        'Data': "SMILE 2023 - Abriu uma vaga!",
                    },
                },
                ReplyToAddresses=[
                    os.environ.get("REPLY_TO_EMAIL"),
                ],
                Source=os.environ.get("FROM_EMAIL"),
            )

            return True
        except Exception as err:
            print(err)
            return False

    def send_deleted_user_email(self, user: UserInfo) -> bool:
        try:
            client_ses = boto3.client('ses', region_name=os.environ.get('SES_REGION'))

            delete_email_composed_html = compose_deleted_user_email(user)

            response = client_ses.send_email(
                Destination={
                    'ToAddresses': [
                        user.email,
                    ],
                    'BccAddresses':
                        [
                            os.environ.get("HIDDEN_COPY")
                        ]
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': "UTF-8",
                            'Data': delete_email_composed_html,
                        },
                    },
                    'Subject': {
                        'Charset': "UTF-8",
                        'Data': "SMILE 2023 - Exclusão de conta",
                    },
                },
                ReplyToAddresses=[
                    os.environ.get("REPLY_TO_EMAIL"),
                ],
                Source=os.environ.get("FROM_EMAIL"),
            )

            return True

        except Exception as err:
            print(err)
            return False

    def delete_enrollment(self, user_id: str, code: str) -> Enrollment:
        resp = self.dynamo.delete_item(partition_key=self.enrollment_partition_key_format(code),
                                       sort_key=self.enrollment_sort_key_format(user_id))

        if "Attributes" not in resp:
            raise NoItemsFound("user_id")

        return EnrollmentDynamoDTO.from_dynamo(resp['Attributes']).to_entity()

    def delete_certificates(self, email: str) -> True:
        client_s3 = boto3.client('s3', region_name=os.environ.get('AWS_REGION'))
        bucket = os.environ.get('BUCKET_NAME')
        hash_key = os.environ.get('HASH_KEY')
        prefix = hashlib.sha256((email + hash_key).encode('utf-8')).hexdigest()

        try:

            itens = client_s3.list_objects_v2(
                Bucket=bucket,
                Prefix=prefix
            )

            print(itens)

            for item in itens['Contents']:
                client_s3.delete_object(
                    Bucket=bucket,
                    Key=item['Key']
                )


            return True

        except Exception as err:
            print(err)
            return False
        
    def batch_get_activities(self, codes: List[str]) -> List[Activity]:
        codes = [{self.dynamo.partition_key: self.activity_partition_key_format(code), self.dynamo.sort_key: self.activity_sort_key_format(code)} for code in codes]
        if len(codes) == 0:
            return []

        response = self.dynamo.batch_get_items(keys=codes)
        activities = list()
        for item in response["Responses"][self.dynamo.dynamo_table.name]:
            activities.append(ActivityDynamoDTO.from_dynamo(item).to_entity())

        return activities
    
    def batch_delete_enrollments(self, users_ids: List[str], code: str) -> List[Enrollment]:
        users_ids = [{self.dynamo.partition_key: self.enrollment_partition_key_format(code), self.dynamo.sort_key: self.enrollment_sort_key_format(user_id)} for user_id in users_ids]

        response = self.dynamo.batch_delete_items(keys=users_ids)
        
        return None
