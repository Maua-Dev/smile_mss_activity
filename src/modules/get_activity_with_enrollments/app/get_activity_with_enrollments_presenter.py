from src.shared.domain.observability.observability_interface import IObservability
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_activity_with_enrollments_controller import \
    GetActivityWithEnrollmentsController
from .get_activity_with_enrollments_usecase import \
    GetActivityWithEnrollmentsUsecase

observability = Environments.get_observability()(module_name="get_activity_with_enrollments")

repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()
usecase = GetActivityWithEnrollmentsUsecase(repo_activity, repo_user, observability=observability)
controller = GetActivityWithEnrollmentsController(usecase, observability=observability)

@observability.presenter_decorators
def get_activity_with_enrollments_presenter(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = get_activity_with_enrollments_presenter(event, context)
    observability.add_error_count_metric(response["statusCode"]) # ErrorCount metrics
    
    return response
 