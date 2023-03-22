from src.modules.enroll_activity_admin.app.enroll_activity_admin_usecase import EnrollActivityAdminUsecase
from src.modules.enroll_activity_admin.app.enroll_activity_admin_viewmodel import EnrollActivityAdminViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ClosedActivity, UserAlreadyCompleted, \
    UserAlreadyEnrolled, ActivityEnded, UserNotAdmin, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, Forbidden, InternalServerError
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class EnrollActivityAdminController:

    def __init__(self, usecase: EnrollActivityAdminUsecase):
        self.EnrollActivityAdminUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
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

        except UserNotAdmin as err:

            return Forbidden(body=f"Usuário não é administrador")

        except MissingParameters as err:

            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except ForbiddenAction as err:

            return Forbidden(body=f"Ação proibida: {err.message}")

        except ClosedActivity as err:

            return Forbidden(body=f"Inscrições fechadas")

        except UserAlreadyCompleted as err:

            return Forbidden(body=f"Usuário já completou a atividade")

        except UserAlreadyEnrolled as err:

            return Forbidden(body=f"Usuário já inscrito")

        except EntityError as err:

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except ActivityEnded as err:

            return Forbidden(body=f"Impossível inscrever usuário em atividade que já terminou")

        except Exception as err:

            return InternalServerError(body=err.args[0])
