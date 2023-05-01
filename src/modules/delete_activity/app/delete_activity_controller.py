import json
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .delete_activity_usecase import DeleteActivityUsecase
from .delete_activity_viewmodel import DeleteActivityViewmodel


class DeleteActivityController:

    def __init__(self, usecase: DeleteActivityUsecase, observability: IObservability):
        self.DeleteActivityUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
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
            response = OK(viewmodel.to_dict())
            self.observability.log_controller_out(input=json.dumps(response.body))
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
        except ForbiddenAction as err:
            self.observability.log_exception(status_code=403, exception_name="ForbiddenAction", message=err.message)
            return Forbidden(body="Apenas administradores podem apagar atividades")

        except MissingParameters as err:
            self.observability.log_exception(status_code=400, exception_name="MissingParameters", message=err.message)
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except EntityError as err:
            self.observability.log_exception(status_code=400, exception_name="EntityError", message=err.message)
            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name="Exception", message=err.args[0])
            return InternalServerError(body=err.args[0])
