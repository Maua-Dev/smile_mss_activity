from .drop_activity_usecase import DropActivityUsecase
from .drop_activity_viewmodel import DropActivityViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound, ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class DropActivityController:

    def __init__(self, usecase: DropActivityUsecase):
        self.DropActivityUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')

            if not request.data.get('code'):
                raise MissingParameters('code')

            enrollment = self.DropActivityUsecase(
                user_id=request.data.get('user_id'),
                code=request.data.get('code')
            )

            viewmodel = DropActivityViewmodel(enrollment)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except ForbiddenAction as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
