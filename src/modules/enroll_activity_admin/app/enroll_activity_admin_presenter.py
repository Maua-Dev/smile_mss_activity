from .enroll_activity_admin_controller import EnrollActivityAdminController
from .enroll_activity_admin_usecase import EnrollActivityAdminUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

observability = Environments.get_observability()(module_name="enroll_activity_admin")

repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()
usecase = EnrollActivityAdminUsecase(repo_activity, repo_user, observability=observability)
controller = EnrollActivityAdminController(usecase, observability=observability)

@observability.presenter_decorators
def enroll_activity_admin_presenter(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = enroll_activity_admin_presenter(event, context)
    observability.add_error_count_metric(response["statusCode"]) # ErrorCount metrics
    
    return response
