from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from .delete_attendance_confirmation_viewmodel import DeleteAttendanceConfirmationViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from .delete_attendance_confirmation_usecase import DeleteAttendanceConfirmationUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class DeleteAttendanceConfirmationController:
       def __init__(self, usecase: DeleteAttendanceConfirmationUsecase):
              self.DeleteAttendanceConfirmationUsecase = usecase

       def __call__(self, request: IRequest) -> IResponse:
              try:
                     if request.data.get("code") is None:
                            raise MissingParameters("code")

                     if request.data.get("requester_user") is None:
                            raise MissingParameters("requester_user")

                     requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

                     confirmation_code = self.DeleteAttendanceConfirmationUsecase(
                            code=request.data.get("code"),
                            requester_user=requester_user
                     )

                     viewmodel = DeleteAttendanceConfirmationViewmodel(
                            activity_code=request.data.get("code"),
                            confirmation_code=confirmation_code
                     )

                     return OK(viewmodel.to_dict())
              
              except NoItemsFound as err:

                     return NotFound(body=err.message)

              except MissingParameters as err:

                     return BadRequest(body=err.message)

              except ForbiddenAction as err:

                     return Forbidden(body=err.message)

              except EntityError as err:

                     return BadRequest(body=err.message)

              except Exception as err:

                     return InternalServerError(body=err.args[0])