from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .delete_activity_usecase import DeleteActivityUsecase
from .delete_activity_viewmodel import DeleteActivityViewmodel


class DeleteActivityController:

    def __init__(self, usecase: DeleteActivityUsecase):
        self.DeleteActivityUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            if not request.data.get('code'):
                raise MissingParameters('code')

            enrollment = self.DeleteActivityUsecase(
                code=request.data.get('code'),
                user=requester_user
            )

            viewmodel = DeleteActivityViewmodel(enrollment)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except ForbiddenAction as err:

            return Forbidden(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except EntityError as err:

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:

            return InternalServerError(body=err.args[0])
