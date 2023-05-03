from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .delete_activity_controller import DeleteActivityController
from .delete_activity_usecase import DeleteActivityUsecase

observability = Environments.get_observability()(module_name="delete_activity")

repo = Environments.get_activity_repo()()
usecase = DeleteActivityUsecase(repo, observability=observability)
controller = DeleteActivityController(usecase, observability=observability)

@observability.presenter_decorators
def delete_activity_presenter(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

@observability.handler_decorators
def lambda_handler(event, context):
    
    response = delete_activity_presenter(event, context)
    observability.add_error_count_metric(statusCode=response.get('statusCode', 500))
    
    return response