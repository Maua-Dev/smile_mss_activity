import json
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from .delete_user_usecase import DeleteUserUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import InternalServerError, OK, NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class DeleteUserController:

    def __init__(self, usecase: DeleteUserUsecase, observability: IObservability):
        self.DeleteUserUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            user = self.DeleteUserUsecase(
                user=requester_user,
            )

            message = {"message": f"Usuário '{user.user_id}' deletado com sucesso."}
            response = OK(message) 
            self.observability.log_controller_out(input=json.dumps(response.body), status_code=response.status_code)

            return response

        except NoItemsFound as err:
            self.observability.log_exception(status_code=404, exception_name="NoItemsFound", message=err.message)
            return NotFound(body=f"Usuário já deletado")

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name="Exception", message=err.args[0])

            return InternalServerError(body=f"Erro favor contato o suporte. - {err}")
