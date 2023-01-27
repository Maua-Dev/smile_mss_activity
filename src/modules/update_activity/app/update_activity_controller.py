import datetime

from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from .update_activity_viewmodel import UpdateActivityViewmodel
from .update_activity_usecase import UpdateActivityUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden


class UpdateActivityController:
    UpdateActivityUsecase: UpdateActivityUsecase

    def __init__(self, usecase: UpdateActivityUsecase) -> None:
        self.UpdateActivityUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if not request.data.get('code'):
                raise MissingParameters('code')

            if request.data.get('new_title') is None:
                raise MissingParameters('new_title')

            if request.data.get('new_description') is None:
                raise MissingParameters('new_description')

            if request.data.get('new_activity_type') is None:
                raise MissingParameters('new_activity_type')

            new_activity_type = request.data.get('new_activity_type')
            if new_activity_type not in [activity_type_value.value for activity_type_value in ACTIVITY_TYPE]:
                raise EntityError('new_activity_type')
            new_activity_type = ACTIVITY_TYPE[new_activity_type]

            if request.data.get('new_is_extensive') is None:
                raise MissingParameters('new_is_extensive')

            new_delivery_model = request.data.get('new_delivery_model')
            if new_delivery_model is None:
                raise MissingParameters('new_delivery_model')
            if new_delivery_model not in [delivery_model_value.value for delivery_model_value in DELIVERY_MODEL]:
                raise EntityError('new_delivery_model')
            new_delivery_model = DELIVERY_MODEL[new_delivery_model]

            if request.data.get('new_start_date') is None:
                raise MissingParameters('new_start_date')

            new_start_date = request.data.get('new_start_date')

            if request.data.get('new_duration') is None:
                raise MissingParameters('new_duration')

            if request.data.get('new_responsible_professors') is None:
                raise MissingParameters('new_responsible_professors')

            new_speakers = request.data.get('new_speakers')
            if new_speakers is None:
                raise MissingParameters('new_speakers')

            if type(new_speakers) != list:
                raise EntityError('new_speakers')

            try:
                new_speakers = [Speaker(**speaker) for speaker in new_speakers]
            except:
                raise EntityError("new_speakers")

            if request.data.get('new_total_slots') is None:
                raise MissingParameters('new_total_slots')

            if request.data.get('new_accepting_new_enrollments') is None:
                raise MissingParameters('new_accepting_new_enrollments')

            new_stop_accepting_new_enrollments_before = request.data.get('new_stop_accepting_new_enrollments_before')

            updated_activity = self.UpdateActivityUsecase(
                code=request.data.get('code'),
                new_title=request.data.get('new_title'),
                new_description=request.data.get('new_description'),
                new_activity_type=new_activity_type,
                new_is_extensive=request.data.get('new_is_extensive'),
                new_delivery_model=new_delivery_model,
                new_start_date=new_start_date,
                new_duration=request.data.get('new_duration'),
                new_link=request.data.get('new_link'),
                new_place=request.data.get('new_place'),
                new_responsible_professors_user_id=request.data.get('new_responsible_professors'),
                new_speakers=new_speakers,
                new_total_slots=request.data.get('new_total_slots'),
                new_accepting_new_enrollments=request.data.get('new_accepting_new_enrollments'),
                new_stop_accepting_new_enrollments_before=new_stop_accepting_new_enrollments_before
            )

            viewmodel = UpdateActivityViewmodel(updated_activity)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:
            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
