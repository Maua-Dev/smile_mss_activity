from .enroll_activity_controller import EnrollActivityController
from .enroll_activity_usecase import EnrollActivityUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

repo = Environments.get_activity_repo()()
usecase = EnrollActivityUsecase(repo)
controller = EnrollActivityController(usecase)

def lambda_handler(event, context):
       httpRequest = LambdaHttpRequest(data=event)
       response = controller(httpRequest)
       httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

       return httpResponse.toDict()