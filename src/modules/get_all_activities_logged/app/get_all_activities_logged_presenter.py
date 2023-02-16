from .get_all_activities_logged_controller import \
    GetAllActivitiesLoggedController
from .get_all_activities_logged_usecase import GetAllActivitiesLoggedUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_activity_repo()()
usecase = GetAllActivitiesLoggedUsecase(repo)
controller = GetAllActivitiesLoggedController(usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
