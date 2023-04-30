from src.shared.helpers.external_interfaces.http_codes import InternalServerError
import json
import os
from datetime import datetime, timedelta

import boto3
from boto3.dynamodb.conditions import Key

from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpResponse

observability = Environments.get_observability()(module_name="close_activity_by_date")
repo_activity = Environments.get_activity_repo()()

@observability.presenter_decorators
def close_activity_by_date_presenter(event, context):
    try:
        observability.log_simple_lambda_in() 
        
        activities = repo_activity.get_all_activities()

        activities_to_update = []

        for activity in activities:
            if activity.stop_accepting_new_enrollments_before is None:
                continue
            if activity.stop_accepting_new_enrollments_before < datetime.now().timestamp()*1000 and activity.accepting_new_enrollments:
                activity.accepting_new_enrollments = False
                activities_to_update.append(activity)

        for activity in activities_to_update:
            print(f"""
                Atualizando atividade {activity.code}
                Inscrição fechou as {datetime.fromtimestamp(activity.stop_accepting_new_enrollments_before/1000) - timedelta(hours=3)}
                Agora são {datetime.now() - timedelta(hours=3)}
            """)

        if len(activities_to_update) == 0:
            print("Nenhuma atividade encontrada para atualizar")

        if len(activities_to_update) != 0:
            repo_activity.batch_update_activities(activities_to_update)

        observability.log_simple_lambda_out()
        observability.add_error_count_metric(statusCode=200)

        return {
            'statusCode': 200,
            'body': json.dumps('Inscrições fechadas com sucesso')
        }
    except Exception as err:
        observability.log_exception(status_code=500, exception_name=err.__class__.__name__, message=err.args[0])
        response = InternalServerError(body=err.args[0])
        httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
        return httpResponse.toDict()
    
@observability.handler_decorators
def lambda_handler(event, context):
    
    response = close_activity_by_date_presenter(event, context)
    
    
    return response