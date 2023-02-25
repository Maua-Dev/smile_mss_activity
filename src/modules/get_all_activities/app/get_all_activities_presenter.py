from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_all_activities_controller import GetAllActivitiesController
from .get_all_activities_usecase import GetAllActivitiesUsecase

repo = Environments.get_activity_repo()()
usecase = GetAllActivitiesUsecase(repo)
controller = GetAllActivitiesController(usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
