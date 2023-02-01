from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_enrollment_usecase import GetEnrollmentUsecase
from .get_enrollment_viewmodel import GetEnrollmentViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class GetEnrollmentController:

    def __init__(self, usecase: GetEnrollmentUsecase):
        self.GetEnrollmentUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            if not request.data.get('code'):
                raise MissingParameters('code')

            request_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            enrollment = self.GetEnrollmentUsecase(
                user_id=request_user.user_id,
                code=request.data.get('code')
            )

            viewmodel = GetEnrollmentViewmodel(enrollment)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
