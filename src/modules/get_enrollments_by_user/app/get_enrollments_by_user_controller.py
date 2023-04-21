import json
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_enrollments_by_user_usecase import GetEnrollmentsByUserUsecase
from .get_enrollments_by_user_viewmodel import \
    GetEnrollmentsByUserViewmodel


class GetEnrollmentsByUserController:

    def __init__(self, usecase: GetEnrollmentsByUserUsecase, observability: IObservability):
        self.GetEnrollmentsByUserUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            enrollments = self.GetEnrollmentsByUserUsecase(
                user_id=requester_user.user_id
            )

            viewmodel = GetEnrollmentsByUserViewmodel(enrollments, requester_user)

            response = OK(viewmodel.to_dict())

            self.observability.log_controller_out(input=json.dumps(response.body))
            return response

        except NoItemsFound as err:
            self.observability.log_exception(message=err.message)
            
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
            self.observability.log_exception(message=err.message)

            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except EntityError as err:
            self.observability.log_exception(message=err.message)

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:
            self.observability.log_exception(message=err.args[0])

            return InternalServerError(body=err.args[0])
