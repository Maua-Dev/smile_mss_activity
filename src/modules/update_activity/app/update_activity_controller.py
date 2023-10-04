import json
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .update_activity_usecase import UpdateActivityUsecase
from .update_activity_viewmodel import UpdateActivityViewmodel


class UpdateActivityController:
    UpdateActivityUsecase: UpdateActivityUsecase

    def __init__(self, usecase: UpdateActivityUsecase, observability: IObservability) -> None:
        self.UpdateActivityUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            if request.data.get('code') is None:
                raise MissingParameters('code') 

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            new_activity_type = request.data.get('new_activity_type')
            if request.data.get("new_activity_type") is not None:
                if new_activity_type not in [activity_type_value.value for activity_type_value in ACTIVITY_TYPE]:
                    raise EntityError('new_activity_type')
                new_activity_type = ACTIVITY_TYPE[new_activity_type]
            
            new_delivery_model = request.data.get('new_delivery_model')
            if request.data.get("new_delivery_model") is not None:
                if new_delivery_model not in [delivery_model_value.value for delivery_model_value in DELIVERY_MODEL]:
                    raise EntityError('new_delivery_model')
                new_delivery_model = DELIVERY_MODEL[new_delivery_model]


            new_speakers = request.data.get('new_speakers')
            if request.data.get("new_speakers") is not None:
                if type(new_speakers) != list:
                    raise EntityError('new_speakers')
                try:
                    new_speakers = [Speaker(**speaker) for speaker in new_speakers]
                except:
                    raise EntityError("new_speakers")
            

            updated_activity = self.UpdateActivityUsecase(
                code=request.data.get('code'),
                new_title=request.data.get('new_title'),
                new_description=request.data.get('new_description'),
                new_activity_type=new_activity_type,
                new_is_extensive=request.data.get('new_is_extensive'),
                new_delivery_model=new_delivery_model,
                new_start_date=request.data.get('new_start_date'),
                new_duration=request.data.get('new_duration'),
                new_link=request.data.get('new_link'),
                new_place=request.data.get('new_place'),
                new_responsible_professors_user_id=request.data.get('new_responsible_professors'),
                new_speakers=new_speakers,
                new_total_slots=request.data.get('new_total_slots'),
                user=requester_user,
                new_accepting_new_enrollments=request.data.get('new_accepting_new_enrollments'),
                new_stop_accepting_new_enrollments_before=request.data.get('new_stop_accepting_new_enrollments_before'),
            )

            viewmodel = UpdateActivityViewmodel(updated_activity)

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

        except ForbiddenAction as err:
            self.observability.log_exception(status_code=403, exception_name="ForbiddenAction", message=err.message)

            return Forbidden(body="Apenas administradores podem atualizar atividades")

        except MissingParameters as err:
            self.observability.log_exception(status_code=400, exception_name="MissingParameters", message=err.message)

            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except EntityError as err:
            self.observability.log_exception(status_code=400, exception_name="EntityError", message=err.message)

            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name=err.__class__.__name__, message=err.args[0])

            return InternalServerError(body=err.args[0])
