from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from src.shared.helpers.external_interfaces.http_codes import InternalServerError, BadRequest, Forbidden, NotFound, OK
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .manual_attendance_change_usecase import ManualAttendanceChangeUsecase
from .manual_attendance_change_viewmodel import ManualAttendanceChangeViewmodel


class ManualAttendanceChangeController:
    def __init__(self, usecase: ManualAttendanceChangeUsecase):
        self.ManualAttendanceChangeUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:

        try:
            if request.data.get('code') is None:
                raise MissingParameters('code')

            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            if request.data.get('new_state') is None:
                raise MissingParameters('new_state')

            if request.data.get('new_state') not in [state.value for state in ENROLLMENT_STATE]:
                raise EntityError("new_state")

            new_state = ENROLLMENT_STATE[request.data.get('new_state')]

            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            activity_dict_with_enrollments = self.ManualAttendanceChangeUsecase(
                code=request.data.get('code'), requester_user=requester_user, new_state=new_state,
                user_id=request.data.get('user_id'))

            viewmodel = ManualAttendanceChangeViewmodel(activity_dict=activity_dict_with_enrollments)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            message = err.message.lower()

            if message == "enrollment":
                return NotFound(body=f"Inscri????o n??o encontrada")

            elif message == "activity":
                return NotFound(body=f"Atividade n??o encontrada")

            elif message == "user":
                return NotFound(body=f"Usu??rio n??o encontrado")

            else:
                return NotFound(body=f"{message} n??o encontrada")


        except MissingParameters as err:

            return BadRequest(body=f"Par??metro ausente: {err.message}")

        except ForbiddenAction as err:
            message = err.message.lower()
            if message == "completed":
                return Forbidden(body=f"N??o ?? poss??vel confirmar presen??a deste usu??rio")

            elif message == "enrolled":
                return Forbidden(body=f"N??o ?? poss??vel cancelar presen??a deste usu??rio")

            elif message == "user":
                return Forbidden(body=f"Apenas professores respons??veis da atividade e administradores podem gerar c??ddigo de confirma????o para atividade")

            else:
                return Forbidden(body=f"A????o n??o permitida: {err.message}")

        except EntityError as err:

            return BadRequest(body=f"Par??metro inv??lido: {err.message}")

        except Exception as err:

            return InternalServerError(body=err.args[0])



