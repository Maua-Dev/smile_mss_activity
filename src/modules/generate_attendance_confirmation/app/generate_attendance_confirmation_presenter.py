from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .generate_attendance_confirmation_controller import \
    GenerateAttendanceConfirmationController
from .generate_attendance_confirmation_usecase import \
    GenerateAttendanceConfirmationUsecase

observability = Environments.get_observability()(module_name="generate_attendance_confirmation")

repo_activity = Environments.get_activity_repo()()
usecase = GenerateAttendanceConfirmationUsecase(repo_activity, observability=observability)
controller = GenerateAttendanceConfirmationController(usecase, observability=observability)


@observability.presenter_decorators
def generate_attendance_confirmation_presenter(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
    
@observability.handler_decorators
def lambda_handler(event, context):
    
    response = generate_attendance_confirmation_presenter(event, context)
    observability.add_error_count_metric(response["statusCode"]) # ErrorCount metrics
    
    return response
