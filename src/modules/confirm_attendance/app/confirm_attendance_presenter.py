from src.shared.environments import Environments
from .confirm_attendance_controller import ConfirmAttendanceController
from .confirm_attendance_usecase import ConfirmAttendanceUsecase
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo_activity = Environments.get_activity_repo()()
usecase = ConfirmAttendanceUsecase(repo_activity)
controller = ConfirmAttendanceController(usecase)

def lambda_handler(event, context):

    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

