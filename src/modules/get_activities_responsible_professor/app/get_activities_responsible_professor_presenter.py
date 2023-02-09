from .get_activities_responsible_professor_controller import \
    GetActivitiesResponsibleProfessorController
from .get_activities_responsible_professor_usecase import \
    GetActivitiesResponsibleProfessorUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()
usecase = GetActivitiesResponsibleProfessorUsecase(repo_activity, repo_user)
controller = GetActivitiesResponsibleProfessorController(usecase)

def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    httpRequest.data['requester_user'] = event.get('requestContext', {}).get('authorizer', {}).get('claims', None)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
