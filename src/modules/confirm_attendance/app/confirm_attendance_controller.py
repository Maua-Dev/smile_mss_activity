import json
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem, ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, Forbidden, NotFound, BadRequest, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .confirm_attendance_usecase import ConfirmAttendanceUsecase


class ConfirmAttendanceController:
    def __init__(self, usecase: ConfirmAttendanceUsecase, observability: IObservability):
        self.usecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
    
        try:
            self.observability.log_controller_in()
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

            self.observability.log_controller_out(input=json.dumps({
                "requester_user":request.data.get('requester_user'),
                "code":request.data.get('code'),
                "confirmation_code":request.data.get('confirmation_code')
            }), status_code=200)
            self.observability.add_error_count_metric()
            return OK('Success to Confirm Attendance!')

        except NoItemsFound as err:
            message = err.message.lower()
            self.observability.log_exception(status_code=404, exception_name="NoItemsFound", message=message)
            if message == "enrollment":
                return NotFound(body=f"Inscrição não encontrada")

            elif message == "activity":
                return NotFound(body=f"Atividade não encontrada")

            elif message == "user":
                return NotFound(body=f"Usuário não encontrado")

            else:
                return NotFound(body=f"{message} não encontrada")
            
        except MissingParameters as err:
            self.observability.log_exception(status_code=400, exception_name="MissingParameters", message=err.message)
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except ForbiddenAction as err:
            self.observability.log_exception(status_code=403, exception_name="ForbiddenAction", message=err.message)
            message = err.message.lower()

            if message == "not_enrolled":

                return Forbidden(body=f"Usuário não está inscrito nesta atividade")

            elif message == "completed":

                return Forbidden(body=f"Presença já confirmada")

            elif message == "enrolled":

                return Forbidden(body=f"Impossível confirmar presença")

            elif message == "confirmation_code":

                return Forbidden(
                    body=f"Código de confirmação inválido")

            else:

                return Forbidden(body=f"Ação não permitida: {err.message}")

        except DuplicatedItem as err:
            self.observability.log_exception(status_code=400, exception_name="DuplicatedItem", message=err.message)
            return BadRequest(body=err.message)

        except EntityError as err:
            self.observability.log_exception(status_code=400, exception_name="EntityError", message=err.message)
            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name=err.__class__.__name__, message=err.args[0])
            return InternalServerError(body=err.args[0])
