import json
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_all_activities_logged_usecase import GetAllActivitiesLoggedUsecase
from .get_all_activities_logged_viewmodel import GetAllActivitiesLoggedViewmodel


class GetAllActivitiesLoggedController:

    def __init__(self, usecase: GetAllActivitiesLoggedUsecase, observability: IObservability):
        self.GetAllActivitiesLoggedUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            all_activities_with_enrollments = self.GetAllActivitiesLoggedUsecase(user_id=requester_user.user_id)

            viewmodel = GetAllActivitiesLoggedViewmodel(all_activities_with_enrollments)
            response = OK(viewmodel.to_dict())
            self.observability.log_controller_out(input=json.dumps(response.body))
            
            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            self.observability.log_exception(status_code=400, exception_name="MissingParameters", message=err.message)
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name=err.__class__.__name__, message=err.args[0])
            
            return InternalServerError(body=err.args[0])
