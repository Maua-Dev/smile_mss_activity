from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Forbidden, InternalServerError, OK, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .manual_drop_activity_usecase import ManualDropActivityUsecase
from .manual_drop_activity_viewmodel import ManualDropActivityViewmodel


class ManualDropActivityController:
    def __init__(self, usecase: ManualDropActivityUsecase):
        self.ManualDropActivityUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:

        try:
            if request.data.get('code') is None:
                raise MissingParameters('code')

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            activity_dict_with_enrollments = self.ManualDropActivityUsecase(
                code=request.data.get('code'), requester_user=requester_user,
                user_id=request.data.get('user_id'))

            viewmodel = ManualDropActivityViewmodel(activity_dict=activity_dict_with_enrollments)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except ForbiddenAction as err:

            return Forbidden(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])






