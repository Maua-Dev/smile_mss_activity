from datetime import datetime, timedelta

from src.shared.helpers.external_interfaces.http_codes import InternalServerError
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpResponse

from .send_email import send_email_notification
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.environments import Environments
import json

from .send_sms import send_sms_notification

repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()

observability = Environments.get_observability()(module_name="send_notifications")

@observability.presenter_decorators
def send_notifications_presenter(event, context):
    try:
        observability.log_simple_lambda_in() 
        all_activities = repo_activity.get_all_activities_admin()

        now_timestamp = datetime.now().timestamp() * 1000
        activities_to_send = list(filter(
            lambda x: x[0].start_date - now_timestamp <= timedelta(minutes=15).total_seconds() * 1000 and now_timestamp <=
                    x[0].start_date, all_activities))

        if len(activities_to_send) != 0:
            activities_to_send_enrolled = list()

            for activity, enrollments in activities_to_send:
                activities_to_send_enrolled.append(
                    (activity, [enrollment for enrollment in enrollments if enrollment.state == ENROLLMENT_STATE.ENROLLED]))

            user_id_list = list()
            for activity, enrollments in activities_to_send_enrolled:
                user_id_list.extend(
                    [enrollment.user_id for enrollment in enrollments if enrollment.state == ENROLLMENT_STATE.ENROLLED])

            user_id_list = list(set(user_id_list))

            if len(user_id_list) != 0:

                users = repo_user.get_users_info(user_id_list)

                users_dict = {user.user_id: user for user in users}

                for activity, enrollments in activities_to_send_enrolled:
                    users = [users_dict.get(enrollment.user_id, "NOT_FOUND") for enrollment in enrollments]
                    send_email_notification(activity, users)
                    # send_sms_notification(activity, users)

                observability.log_simple_lambda_out()
                return {
                    'statusCode': 200,
                    'body': json.dumps('Notificações enviadas!')
                }

            else:
                print("Nenhum usuário da atividade")
                return {
                    'statusCode': 404,
                    'body': json.dumps("Nenhum usuário da atividade")
                }
        else:
            print("Nenhuma atividade para enviar notificações!")
            return {
                'statusCode': 404,
                'body': json.dumps("Nenhuma atividade para enviar notificações!")
            }
    except Exception as err:
        observability.log_exception(message="Error 500 - "+err.args[0])
        response = InternalServerError(body=err.args[0])
        httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)
        return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = send_notifications_presenter(event, context)
    observability.add_error_count_metric(response["statusCode"]) # ErrorCount metrics
    
    return response
