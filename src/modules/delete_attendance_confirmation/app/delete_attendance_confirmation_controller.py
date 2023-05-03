import json
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .delete_attendance_confirmation_usecase import DeleteAttendanceConfirmationUsecase
from .delete_attendance_confirmation_viewmodel import DeleteAttendanceConfirmationViewmodel


class DeleteAttendanceConfirmationController:
    def __init__(self, usecase: DeleteAttendanceConfirmationUsecase, observability: IObservability):
        self.DeleteAttendanceConfirmationUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
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

            response = OK(viewmodel.to_dict())
            self.observability.log_controller_out(input=json.dumps(response.body), status_code=response.status_code)
            return response

        except NoItemsFound as err:
            self.observability.log_exception(status_code=404, exception_name="NoItemsFound", message=err.message)
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
            self.observability.log_exception(status_code=400, exception_name="MissingParameters", message=err.message)
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except ForbiddenAction as err:
            self.observability.log_exception(status_code=403, exception_name="ForbiddenAction", message=err.message)
            message = err.message.lower()

            if message == "confirmation_code":
                return Forbidden(body=f"Atividade não possui um código de confirmação")

            elif message == "user":
                return Forbidden(body=f"Apenas professores responsáveis da atividade e administradores podem deletar o código de confirmação")

            else:
                return Forbidden(body=f"Ação não permitida: {message}")

        except EntityError as err:
            self.observability.log_exception(status_code=400, exception_name="EntityError", message=err.message)
            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name=type(err).__name__, message=err.args[0])
            return InternalServerError(body=err.args[0])
