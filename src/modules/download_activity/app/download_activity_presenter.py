from src.modules.download_activity.app.download_activity_controller import DownloadActivityController
from src.modules.download_activity.app.download_activity_usecase import DownloadActivityUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

observability = Environments.get_observability()(module_name="download_activity")

repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()
usecase = DownloadActivityUsecase(repo_activity, observability=observability)
controller = DownloadActivityController(usecase, observability=observability)

@observability.presenter_decorators
def delete_user_presenter(event, context):
    print(event)

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = delete_user_presenter(event, context)
    observability.add_error_count_metric(statusCode=response.get('statusCode', 500))
    
    return response