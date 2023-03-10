from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from .get_all_activities_admin_viewmodel import GetAllActivitiesAdminViewmodel


class GetAllActivitiesAdminController:

    def __init__(self, usecase: GetAllActivitiesAdminUsecase):
        self.GetAllActivitiesAdminUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            all_activities_with_enrollments = self.GetAllActivitiesAdminUsecase(requester_user)

            viewmodel = GetAllActivitiesAdminViewmodel(all_activities_with_enrollments)

            return OK(viewmodel.to_dict())

        except ForbiddenAction as err:
            return Forbidden(body="Apenas administradores podem realizar essa ação")

        except MissingParameters as err:

            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except Exception as err:
            return InternalServerError(body=err.args[0])
