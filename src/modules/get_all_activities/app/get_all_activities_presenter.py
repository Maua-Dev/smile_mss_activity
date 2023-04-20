from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_all_activities_controller import GetAllActivitiesController
from .get_all_activities_usecase import GetAllActivitiesUsecase

observability = Environments.get_observability()(module_name="get_all_activities")

repo = Environments.get_activity_repo()()
usecase = GetAllActivitiesUsecase(repo, observability=observability)
controller = GetAllActivitiesController(usecase, observability=observability)

@observability.presenter_decorators
def get_user_presenter(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(
        status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = get_user_presenter(event, context)
    observability.add_error_count_metric(response["statusCode"]) # ErrorCount metrics
    
    return response
