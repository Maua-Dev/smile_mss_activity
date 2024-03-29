import json
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .get_enrollment_usecase import GetEnrollmentUsecase
from .get_enrollment_viewmodel import GetEnrollmentViewmodel


class GetEnrollmentController:

    def __init__(self, usecase: GetEnrollmentUsecase, observability: IObservability):
        self.GetEnrollmentUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            if not request.data.get('code'):
                raise MissingParameters('code')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            enrollment = self.GetEnrollmentUsecase(
                user_id=requester_user.user_id,
                code=request.data.get('code')
            )

            viewmodel = GetEnrollmentViewmodel(enrollment, requester_user)
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



        except EntityError as err:
            self.observability.log_exception(status_code=400, exception_name="EntityError", message=err.message)

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name=err.__class__.__name__, message=err.args[0])

            return InternalServerError(body=err.args[0])
