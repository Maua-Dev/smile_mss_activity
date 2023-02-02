from src.shared.environments import Environments
from .create_activity_controller import CreateActivityController
from .create_activity_usecase import CreateActivityUsecase
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_activity_repo()()
usecase = CreateActivityUsecase(repo)
controller = CreateActivityController(usecase)

def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

