from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
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
            return Forbidden(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
