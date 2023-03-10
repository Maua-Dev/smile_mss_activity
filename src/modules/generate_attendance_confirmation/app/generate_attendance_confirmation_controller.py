from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .generate_attendance_confirmation_usecase import \
    GenerateAttendanceConfirmationUsecase
from .generate_attendance_confirmation_viewmodel import \
    GenerateAttendanceConfirmationViewmodel


class GenerateAttendanceConfirmationController:

    def __init__(self, usecase: GenerateAttendanceConfirmationUsecase):
        self.GenerateAttendanceConfirmationUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            if request.data.get("code") is None:
                raise MissingParameters("code")

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            confirmation_code = self.GenerateAttendanceConfirmationUsecase(
                code=request.data.get("code"),
                requester_user=requester_user
            )

            viewmodel = GenerateAttendanceConfirmationViewmodel(confirmation_code=confirmation_code, activity_code=request.data.get("code"))

            return OK(viewmodel.to_dict())

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

            message = err.message.lower()

            if message == "confirmation_code":

                return Forbidden(body=f"Já existe um código de confirmação para esta atividade")

            elif message == "user":

                return Forbidden(
                    body=f"Apenas professores responsáveis da atividade e administradores podem gerar códdigo de confirmação para atividades")

            else:

                return Forbidden(body=f"Ação não permitida: {err.message}")

        except EntityError as err:

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:

            return InternalServerError(body=err.args[0])
