import json
import os
from datetime import datetime

import boto3
from boto3.dynamodb.conditions import Key

from src.shared.environments import Environments

repo_activity = Environments.get_activity_repo()()


def lambda_handler(event, context):

    activities = repo_activity.get_all_activities()

    activities_to_update = []

    for activity in activities:
        if activity.stop_accepting_new_enrollments_before is None:
            continue
        if activity.stop_accepting_new_enrollments_before < datetime.now().timestamp()*1000 and activity.accepting_new_enrollments:
            activity.accepting_new_enrollments = False
            activities_to_update.append(activity)

    print(activities_to_update)

    if len(activities_to_update) != 0:
        repo_activity.batch_update_activities(activities_to_update)

    return {
        'statusCode': 200,
        'body': json.dumps('Salve da Lambda!')
    }
