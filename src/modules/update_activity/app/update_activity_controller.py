from .update_activity_viewmodel import UpdateActivityViewmodel
from .update_activity_usecase import UpdateActivityUsecase
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Forbidden

class UpdateActivityController:
       def __init__(self, usecase: UpdateActivityUsecase) -> None:
              self.UpdateActivityUsecase = usecase

       def __call__(self, request: IRequest) -> IResponse:
              try:
                     if not request.data.get('code'):
                            raise MissingParameters('code')

                     update_activity = self.UpdateActivityUsecase(**request.data)

                     viewmodel = UpdateActivityViewmodel(update_activity)

                     return OK(viewmodel.to_dict())
              
              except NoItemsFound as err:
                     return NotFound(body=err.message)
                     
              except MissingParameters as err:

                     return BadRequest(body=err.message)

              except ForbiddenAction as err:

                     return Forbidden(body=err.message)

              except WrongTypeParameter as err:

                     return BadRequest(body=err.message)

              except EntityError as err:

                     return BadRequest(body=err.message)

              except Exception as err:

                     return InternalServerError(body=err.args[0])