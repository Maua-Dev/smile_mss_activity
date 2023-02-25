from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, Forbidden, BadRequest, InternalServerError, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_activity_with_enrollments_usecase import \
    GetActivityWithEnrollmentsUsecase
from .get_activity_with_enrollments_viewmodel import \
    GetActivityWithEnrollmentsViewmodel


class GetActivityWithEnrollmentsController:
    def __init__(self, usecase: GetActivityWithEnrollmentsUsecase):
        self.GetActivityWithEnrollmentsUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            if request.data.get('code') is None:
                raise MissingParameters('code')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            activity_with_enrollments = self.GetActivityWithEnrollmentsUsecase(user=requester_user,
                                                                               code=request.data.get('code'))

            viewmodel = GetActivityWithEnrollmentsViewmodel(activity_with_enrollments)

            return OK(viewmodel.to_dict())

        except MissingParameters as err:

            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except ForbiddenAction as err:

            return Forbidden(body=err.message)

        except EntityError as err:

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:

            return InternalServerError(body=err.args[0])
