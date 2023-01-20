from .get_all_activities_admin_controller import GetAllActivitiesAdminController
from .get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_activity_repo()()
usecase = GetAllActivitiesAdminUsecase(repo)
controller = GetAllActivitiesAdminController(usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
