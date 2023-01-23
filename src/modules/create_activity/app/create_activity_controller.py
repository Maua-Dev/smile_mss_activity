import datetime
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from .create_activity_usecase import CreateActivityUsecase
from .create_activity_viewmodel import CreateActivityViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound, DuplicatedItem
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, Forbidden, InternalServerError, NotFound


class CreateActivityController:

    def __init__(self, usecase: CreateActivityUsecase):
        self.CreateActivityUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
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
            if type(start_date) != int:
                raise WrongTypeParameter('start_date', 'int', type(start_date).__class__.__name__)
            start_date = datetime.datetime.fromtimestamp(start_date)

            if request.data.get('duration') is None:
                raise MissingParameters('duration')
            if request.data.get('responsible_professors') is None:
                raise MissingParameters('responsible_professors')
            if request.data.get('speakers') is None:
                raise MissingParameters('speakers')
            if request.data.get('total_slots') is None:
                raise MissingParameters('total_slots')
            if request.data.get('accepting_new_enrollments') is None:
                raise MissingParameters('accepting_new_enrollments')

            stop_accepting_new_enrollments_before = request.data.get('stop_accepting_new_enrollments_before')
            if stop_accepting_new_enrollments_before is not None:
                if type(stop_accepting_new_enrollments_before) != int:
                    raise WrongTypeParameter('stop_accepting_new_enrollments_before', 'int', type(stop_accepting_new_enrollments_before).__class__.__name__)
                stop_accepting_new_enrollments_before = datetime.datetime.fromtimestamp(stop_accepting_new_enrollments_before)
            
            activity = self.CreateActivityUsecase(
                    code = request.data.get('code'), 
                    title = request.data.get('title'),
                    description = request.data.get('description'),
                    activity_type = activity_type,
                    is_extensive = request.data.get('is_extensive'),
                    delivery_model = delivery_model,
                    start_date = start_date,    
                    duration = request.data.get('duration'),
                    link = request.data.get('link'),
                    place = request.data.get('place'),
                    responsible_professors_user_id = request.data.get('responsible_professors'),
                    speakers = request.data.get('speakers'),
                    total_slots = request.data.get('total_slots'),
                    accepting_new_enrollments = request.data.get('accepting_new_enrollments'),
                    stop_accepting_new_enrollments_before = stop_accepting_new_enrollments_before
                    )
                    
            viewmodel = CreateActivityViewmodel(activity)

            return Created(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except DuplicatedItem as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
