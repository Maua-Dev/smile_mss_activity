from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_enrollments_by_user_controller import \
    GetEnrollmentsByUserController
from .get_enrollments_by_user_usecase import GetEnrollmentsByUserUsecase
observability = Environments.get_observability()(module_name="get_enrollments_by_user")

repo = Environments.get_activity_repo()()
usecase = GetEnrollmentsByUserUsecase(repo, observability=observability)
controller = GetEnrollmentsByUserController(usecase, observability=observability)


@observability.presenter_decorators
def get_enrollments_by_user_presenter(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = get_enrollments_by_user_presenter(event, context)
    observability.add_error_count_metric(response["statusCode"]) # ErrorCount metrics
    
    return response
