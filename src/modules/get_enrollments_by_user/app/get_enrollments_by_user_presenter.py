from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .get_enrollments_by_user_controller import \
    GetEnrollmentsByUserController
from .get_enrollments_by_user_usecase import GetEnrollmentsByUserUsecase

repo = Environments.get_activity_repo()()
usecase = GetEnrollmentsByUserUsecase(repo)
controller = GetEnrollmentsByUserController(usecase)


def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
