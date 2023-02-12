from src.modules.get_all_activites_logged.app.get_all_activites_logged_usecase import GetAllActivitiesLoggedUsecase
from src.modules.get_all_activites_logged.app.get_all_activites_logged_viewmodel import GetAllActivitiesLoggedViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse


class GetAllActivitiesLoggedController:

    def __init__(self, usecase: GetAllActivitiesLoggedUsecase):
        self.GetAllActivitiesLoggedUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            all_activities_with_enrollments = self.GetAllActivitiesLoggedUsecase(user_id=requester_user.user_id)

            viewmodel = GetAllActivitiesLoggedViewmodel(all_activities_with_enrollments)

            return OK(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
