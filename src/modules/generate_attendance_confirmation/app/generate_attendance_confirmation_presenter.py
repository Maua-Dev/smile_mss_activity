from .generate_attendance_confirmation_controller import \
    GenerateAttendanceConfirmationController
from .generate_attendance_confirmation_usecase import \
    GenerateAttendanceConfirmationUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_activity = Environments.get_activity_repo()()
usecase = GenerateAttendanceConfirmationUsecase(repo_activity)
controller = GenerateAttendanceConfirmationController(usecase)

def lambda_handler(event, context):
       httpRequest = LambdaHttpRequest(data=event)
       httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
       response = controller(httpRequest)
       httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

       return httpResponse.toDict()
