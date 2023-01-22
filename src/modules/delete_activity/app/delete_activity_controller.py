from .delete_activity_usecase import DeleteActivityUsecase
from .delete_activity_viewmodel import DeleteActivityViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class DeleteActivityController:

    def __init__(self, usecase: DeleteActivityUsecase):
        self.DeleteActivityUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            if not request.data.get('code'):
                raise MissingParameters('code')

            enrollment = self.DeleteActivityUsecase(
                code=request.data.get('code')
            )

            viewmodel = DeleteActivityViewmodel(enrollment)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
