from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .update_activity_controller import UpdateActivityController
from .update_activity_usecase import UpdateActivityUsecase

repo_activity = Environments.get_activity_repo()()
repo_users = Environments.get_user_repo()()
usecase = UpdateActivityUsecase(repo_activity, repo_users)
controller = UpdateActivityController(usecase)

def lambda_handler(event, context):
       httpRequest = LambdaHttpRequest(data=event)
       httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
       response = controller(httpRequest)
       httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

       return httpResponse.toDict()
