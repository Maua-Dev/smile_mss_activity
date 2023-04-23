import hashlib
import json
import os

import boto3

from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

observability = Environments.get_observability()(module_name="get_certificates")
hash_key = os.environ.get("HASH_KEY")
bucket_name = os.environ.get("BUCKET_NAME")
cdn_url = os.environ.get("CDN_URL")
repo = Environments.get_activity_repo()()

def get_s3_objects(email: str):
    s3_client = boto3.client("s3")
    hash_name = hashlib.sha256((email + hash_key).encode('utf-8')).hexdigest()

    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=f"{hash_name}")

    if "Contents" not in response:
        return []


    resp = []
    for file in response["Contents"]:
        if file.get("Key") and file.get("Key").endswith(".pdf"):
            resp.append(file["Key"])

    return resp


@observability.presenter_decorators
def get_certificates_presenter(event, context):
    observability.log_simple_lambda_in() 
    print(event)
    try:
        all_activities = repo.get_all_activities()

        activities_dict = {activity.code: activity.title for activity in all_activities}

        httpRequest = LambdaHttpRequest(data=event)

        httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
        requester_user = httpRequest.data['requester_user']

        if not requester_user:
            observability.log_exception(message=err.message)
            return LambdaHttpResponse(status_code=400, body="Parâmetro ausente: requester_user").toDict()
        email = requester_user.get('email')

        files = get_s3_objects(email)

        response = list()

        for file in files:
            title = activities_dict.get(file.split("/")[1].split("_")[0])
            response.append({
                "url": f"{cdn_url}/{file}",
                "activity": title if title else "Atividade não encontrada"
            })
        observability.log_simple_lambda_out()

        return LambdaHttpResponse(status_code=200, body={"certificates": response}).toDict()

    except Exception as err:
        observability.log_exception(message="Error 500 - "+err.args[0])
        return LambdaHttpResponse(status_code=500, body=err.args[0]).toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = get_certificates_presenter(event, context)
    observability.add_error_count_metric(response["statusCode"]) # ErrorCount metrics
    
    return response
