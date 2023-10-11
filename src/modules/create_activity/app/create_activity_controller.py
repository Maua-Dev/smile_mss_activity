import json
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, DuplicatedItem, \
    ConflictingInformation
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, Forbidden, InternalServerError, \
    NotFound
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO
from .create_activity_usecase import CreateActivityUsecase
from .create_activity_viewmodel import CreateActivityViewmodel


class CreateActivityController:

    def __init__(self, usecase: CreateActivityUsecase, observability: IObservability):
        self.CreateActivityUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            if request.data.get('code') is None:
                raise MissingParameters('code')
            if request.data.get('title') is None:
                raise MissingParameters('title')
            if request.data.get('description') is None:
                raise MissingParameters('description')
            if request.data.get('activity_type') is None:
                raise MissingParameters('activity_type')
                
            activity_type = request.data.get('activity_type')
            if activity_type not in [activity_type_value.value for activity_type_value in ACTIVITY_TYPE]:
                raise EntityError('activity_type')
            activity_type = ACTIVITY_TYPE[activity_type]

            if request.data.get('is_extensive') is None:
                raise MissingParameters('is_extensive')

            delivery_model = request.data.get('delivery_model')
            if delivery_model is None:
                raise MissingParameters('delivery_model')
            if delivery_model not in [delivery_model_value.value for delivery_model_value in DELIVERY_MODEL]:
                raise EntityError('delivery_model')
            delivery_model = DELIVERY_MODEL[delivery_model]   

            if request.data.get('start_date') is None:
                raise MissingParameters('start_date')

            start_date = request.data.get('start_date')

            if request.data.get('end_date') is None:
                raise MissingParameters('end_date')
            if request.data.get('responsible_professors') is None:
                raise MissingParameters('responsible_professors')

            speakers = request.data.get('speakers')
            if speakers is None:
                raise MissingParameters('speakers')

            if type(speakers) != list:
                raise EntityError('speakers')

            try:
                speakers = [Speaker(**speaker) for speaker in speakers]
            except:
                raise EntityError("speakers")

            if request.data.get('total_slots') is None:
                raise MissingParameters('total_slots')
            if request.data.get('accepting_new_enrollments') is None:
                raise MissingParameters('accepting_new_enrollments')

            stop_accepting_new_enrollments_before = request.data.get('stop_accepting_new_enrollments_before')

            activity = self.CreateActivityUsecase(
                    code = request.data.get('code'), 
                    title = request.data.get('title'),
                    description = request.data.get('description'),
                    activity_type = activity_type,
                    is_extensive = request.data.get('is_extensive'),
                    delivery_model = delivery_model,
                    start_date = start_date,    
                    end_date = request.data.get('end_date'),
                    link = request.data.get('link'),
                    place = request.data.get('place'),
                    responsible_professors_user_id = request.data.get('responsible_professors'),
                    speakers = speakers,
                    total_slots = request.data.get('total_slots'),
                    accepting_new_enrollments = request.data.get('accepting_new_enrollments'),
                    stop_accepting_new_enrollments_before = stop_accepting_new_enrollments_before,
                    user = requester_user
                    )
                    
            viewmodel = CreateActivityViewmodel(activity)
            response = Created(viewmodel.to_dict())
            self.observability.log_controller_out(input=json.dumps(response.body), status_code=response.status_code)
            
            return response

            if (delivery_model == DELIVERY_MODEL.ONLINE or delivery_model == DELIVERY_MODEL.HYBRID) and link is None:
                raise NoItemsFound('link')

            if (delivery_model == DELIVERY_MODEL.IN_PERSON or delivery_model == DELIVERY_MODEL.HYBRID) and place is None:
                raise NoItemsFound('local')

        except NoItemsFound as err:
            self.observability.log_exception(status_code=404, exception_name="NoItemsFound", message=err.message)
            message = err.message.lower()

            if message == "enrollment":
                return NotFound(body=f"Inscrição não encontrada")

            elif message == "activity":
                return NotFound(body=f"Atividade não encontrada")

            elif message == "user":
                return NotFound(body=f"Usuário não encontrado")

            elif message == "responsible_professors":
                return NotFound(body=f"Professores responsáveis não encontrados")

            else:
                return NotFound(body=f"{message} não encontrada")



        except MissingParameters as err:
            self.observability.log_exception(status_code=400, exception_name="MissingParameters", message=err.message)
            return BadRequest(body=f"Parâmetro ausente: {err.message}")

        except ConflictingInformation as err:
            self.observability.log_exception(status_code=400, exception_name="ConflictingInformation", message=err.message)
            return BadRequest(body=f"Parâmetro a mais está gerando um conflito: {err.message}")

        except ForbiddenAction as err:
            self.observability.log_exception(status_code=403, exception_name="ForbiddenAction", message=err.message)
            return Forbidden(body="Apenas administradores podem criar atividades")

        except DuplicatedItem as err:
            self.observability.log_exception(status_code=400, exception_name="DuplicatedItem", message=err.message)
            return BadRequest(body="Já existe uma atividade com esse código" if err.message == "activity_code" else "Já existe uma atividade com essas informaçãos")

        except EntityError as err:
            self.observability.log_exception(status_code=400, exception_name="EntityError", message=err.message)
            return BadRequest(body=f"Parâmetro inválido: {err.message}")

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name=err.__class__.__name__, message=err.args[0])
            return InternalServerError(body=err.args[0])
