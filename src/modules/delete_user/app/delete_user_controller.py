from .delete_user_usecase import DeleteUserUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import InternalServerError, OK
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class DeleteUserController:

    def __init__(self, usecase: DeleteUserUsecase):
        self.DeleteUserUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            user = self.DeleteUserUsecase(
                user=requester_user,
            )

            message = {"message": f"Usuário '{requester_user.user_id}' deletado com sucesso."}

            return OK(message)

        except Exception as err:

            return InternalServerError(body=f"Erro favor contato o suporte. - {err}")
