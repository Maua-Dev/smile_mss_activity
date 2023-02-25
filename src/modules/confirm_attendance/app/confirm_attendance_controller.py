from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, Forbidden, NotFound, BadRequest, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .confirm_attendance_usecase import ConfirmAttendanceUsecase


class ConfirmAttendanceController:
    def __init__(self, usecase: ConfirmAttendanceUsecase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
    
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')
            if request.data.get('code') is None:
                raise MissingParameters('code')
            if request.data.get('confirmation_code') is None:
                raise MissingParameters('confirmation_code')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()
            
            resp = self.usecase(
                user_id=requester_user.user_id,
                confirmation_code=request.data.get('confirmation_code'),
                code=request.data.get('code')
            )

            if not resp:
                return BadRequest('Failed to Confirm Attendance.')

            return OK('Success to Confirm Attendance!')

        except NoItemsFound as err:
            message = err.message.lower()

            if message == "enrollment":
                return NotFound(body=f"Inscrição não encontrada")

            elif message == "activity":
                return NotFound(body=f"Atividade não encontrada")

            elif message == "user":
                return NotFound(body=f"Usuário não encontrado")

            else:
                return NotFound(body=f"{message} não encontrada")
        except MissingParameters as err:

            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except ForbiddenAction as err:

            return Forbidden(body=err.message)

        except DuplicatedItem as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:

            return InternalServerError(body=err.args[0])
