import json
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ClosedActivity, UserAlreadyEnrolled, \
    UserAlreadyCompleted, ActivityEnded
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .enroll_activity_usecase import EnrollActivityUsecase
from .enroll_activity_viewmodel import EnrollActivityViewmodel

 
class EnrollActivityController:

    def __init__(self, usecase: EnrollActivityUsecase, observability: IObservability):
        self.EnrollActivityUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            if not request.data.get('code'):
                raise MissingParameters('code')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            enrollment = self.EnrollActivityUsecase(
                user_id = requester_user.user_id,
                code =  request.data.get('code')
            )

            viewmodel = EnrollActivityViewmodel(enrollment, requester_user)
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
        
        except MissingParameters as err:
            self.observability.log_exception(status_code=400, exception_name="MissingParameters", message=err.message)
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except ClosedActivity as err:
            self.observability.log_exception(status_code=403, exception_name="ClosedActivity", message=err.message)
            return Forbidden(body=f"Inscrições fechadas")

        except UserAlreadyCompleted as err:
            self.observability.log_exception(status_code=403, exception_name="UserAlreadyCompleted", message=err.message)
            return Forbidden(body=f"Usuário já completou a atividade")

        except UserAlreadyEnrolled as err:
            self.observability.log_exception(status_code=403, exception_name="UserAlreadyEnrolled", message=err.message)
            return Forbidden(body=f"Usuário já inscrito")

        except EntityError as err:
            self.observability.log_exception(status_code=400, exception_name="EntityError", message=err.message)
            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except ActivityEnded as err:
            self.observability.log_exception(status_code=403, exception_name="ActivityEnded", message=err.message)
            return Forbidden(body=f"Impossível inscrever usuário em atividade que já terminou")

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name=type(err).__name__, message=err.args[0])
            return InternalServerError(body=err.args[0])
