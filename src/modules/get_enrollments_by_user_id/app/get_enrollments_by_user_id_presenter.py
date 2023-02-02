from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_enrollments_by_user_id_controller import \
    GetEnrollmentsByUserIdController
from .get_enrollments_by_user_id_usecase import GetEnrollmentsByUserIdUsecase
from src.shared.environments import Environments

repo = Environments.get_activity_repo()()
usecase = GetEnrollmentsByUserIdUsecase(repo)
controller = GetEnrollmentsByUserIdController(usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
