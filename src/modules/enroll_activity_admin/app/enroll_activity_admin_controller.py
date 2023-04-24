import json
from src.shared.domain.observability.observability_interface import IObservability
from .enroll_activity_admin_usecase import EnrollActivityAdminUsecase
from .enroll_activity_admin_viewmodel import EnrollActivityAdminViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ClosedActivity, UserAlreadyCompleted, \
    UserAlreadyEnrolled, ActivityEnded, UserNotAdmin, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, Forbidden, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class EnrollActivityAdminController:

    def __init__(self, usecase: EnrollActivityAdminUsecase, observability: IObservability):
        self.EnrollActivityAdminUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')

            if not request.data.get('code'):
                raise MissingParameters('code')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            enrollment, enrolled_user = self.EnrollActivityAdminUsecase(
                user_id=request.data.get('user_id'),
                code=request.data.get('code'),
                requester_user=requester_user
            )

            viewmodel = EnrollActivityAdminViewmodel(enrollment, enrolled_user)
            response = OK(viewmodel.to_dict()) 
            self.observability.log_controller_out(input=json.dumps(response.body))
            return response

        except NoItemsFound as err:
            self.observability.log_exception(status_code=404, exception_name="NoItemsFound", message=err.message), 
            message = err.message.lower()

            if message == "enrollment":
                return NotFound(body=f"Inscrição não encontrada")

            elif message == "activity":
                return NotFound(body=f"Atividade não encontrada")

            elif message == "user":
                return NotFound(body=f"Usuário não encontrado")

            else:
                return NotFound(body=f"{message} não encontrada")

        except UserNotAdmin as err:
            self.observability.log_exception(status_code=403, exception_name="UserNotAdmin", message=err.message)
            return Forbidden(body=f"Usuário não é administrador")

        except MissingParameters as err:
            self.observability.log_exception(status_code=400, exception_name="MissingParameters", message=err.message)
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except ForbiddenAction as err:
            self.observability.log_exception(status_code=403, exception_name="ForbiddenAction", message=err.message)
            return Forbidden(body=f"Ação proibida: {err.message}")

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
            self.observability.log_exception(status_code=500, exception_name="InternalServerError", message=err.args[0])
            return InternalServerError(body=err.args[0])
