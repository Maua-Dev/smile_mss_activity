from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from .get_all_activities_admin_viewmodel import GetAllActivitiesAdminViewmodel


class GetAllActivitiesAdminController:

    def __init__(self, usecase: GetAllActivitiesAdminUsecase, observability: IObservability):
        self.GetAllActivitiesAdminUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            all_activities_with_enrollments = self.GetAllActivitiesAdminUsecase(requester_user)

            viewmodel = GetAllActivitiesAdminViewmodel(all_activities_with_enrollments)
            response = OK(viewmodel.to_dict())
            self.observability.log_controller_out(input='')

            return response

        except ForbiddenAction as err:
            self.observability.log_exception(message=err.message)
            return Forbidden(body="Apenas administradores podem realizar essa ação")

        except MissingParameters as err:
            self.observability.log_exception(message=err.message)
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except Exception as err:
            self.observability.log_exception(message=err.args[0])
            return InternalServerError(body=err.args[0])
