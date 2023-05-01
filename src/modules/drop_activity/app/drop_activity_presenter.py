from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .drop_activity_controller import DropActivityController
from .drop_activity_usecase import DropActivityUsecase

observability = Environments.get_observability()(module_name="drop_activity")

repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()
usecase = DropActivityUsecase(repo_activity, repo_user, observability=observability)
controller = DropActivityController(usecase, observability=observability)

@observability.presenter_decorators
def drop_activity_presenter(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = drop_activity_presenter(event, context)
    
    
    return response
