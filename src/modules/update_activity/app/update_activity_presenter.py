from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .update_activity_controller import UpdateActivityController
from .update_activity_usecase import UpdateActivityUsecase
observability = Environments.get_observability()(module_name="update_activity")

repo_activity = Environments.get_activity_repo()()
repo_users = Environments.get_user_repo()()
usecase = UpdateActivityUsecase(repo_activity, repo_users, observability=observability)
controller = UpdateActivityController(usecase, observability=observability)

@observability.presenter_decorators
def update_activity_presenter(event, context):
       httpRequest = LambdaHttpRequest(data=event)
       httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
       response = controller(httpRequest)
       httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

       return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = update_activity_presenter(event, context)
    observability.add_error_count_metric(statusCode=response.get('statusCode', 500))
    
    
    return response
