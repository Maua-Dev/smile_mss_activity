from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, ClosedActivity, UserAlreadyEnrolled
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .enroll_activity_usecase import EnrollActivityUsecase
from .enroll_activity_viewmodel import EnrollActivityViewmodel


class EnrollActivityController:

    def __init__(self, usecase: EnrollActivityUsecase):
        self.EnrollActivityUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
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

        except ClosedActivity as err:

            return Forbidden(body=f"Inscrições fechadas")

        except UserAlreadyEnrolled as err:

            return Forbidden(body=f"Usuário já inscrito")

        except ForbiddenAction as err:

            return Forbidden(body=f"Impossível inscrever usuário")

        except EntityError as err:

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:

            return InternalServerError(body=err.args[0])
