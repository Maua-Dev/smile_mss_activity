from datetime import datetime, timezone, timedelta
from typing import List

import boto3
from botocore.exceptions import ClientError

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL

client = boto3.client('sns', region_name='us-east-1')


def compose_sms_message(activity: Activity, user: UserInfo) -> str:
    name = user.name.split(" ")[0]
    gmt3_tz = timezone(timedelta(hours=-3))

    if activity.delivery_model == DELIVERY_MODEL.IN_PERSON:
        place = activity.place
    elif activity.delivery_model == DELIVERY_MODEL.HYBRID:
        place = f"{activity.place} ou Online"
    else:
        place = "Online"

    message = f"""Olá, {name}!\n\nSua atividade {activity.title} começa às {datetime.fromtimestamp(activity.start_date / 1000).astimezone(gmt3_tz).strftime("%H:%M")}\nLocal: {place}\nEsperamos você lá!\n\nEquipe SMILE 2023 ;)"""

    return message


def send_sms_notification(activity: Activity, users: List[UserInfo]):
    try:
        for user in users:
            if not type(user) == UserInfo or user.phone is None or user.accepted_notifications_sms is False:
                continue

            message = compose_sms_message(activity, user)

            client.publish(PhoneNumber=user.phone, Message=message)

    except ClientError as e:
        print(e.response['Error']['Message'])

    else:
        print("SMS -> Activity: ", activity.title),

    print("Sending SMS notification")
