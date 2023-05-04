from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_all_activities_admin_controller import GetAllActivitiesAdminController
from .get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase

observability = Environments.get_observability()(module_name="get_all_activities_admin")

repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()
usecase = GetAllActivitiesAdminUsecase(repo_activity, repo_user, observability=observability)
controller = GetAllActivitiesAdminController(usecase, observability=observability)

@observability.presenter_decorators
def get_all_activities_admin_presenter(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = get_all_activities_admin_presenter(event, context)
    observability.add_error_count_metric(statusCode=response.get('statusCode', 500))
    
    
    return response