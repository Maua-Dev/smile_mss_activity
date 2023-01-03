from src.modules.get_enrollment.app.get_enrollment_usecase import GetEnrollmentUsecase
from src.modules.get_enrollment.app.get_enrollment_viewmodel import GetEnrollmentViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError


class GetEnrollmentController:

    def __init__(self, usecase: GetEnrollmentUsecase):
        self.GetEnrollmentUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('user_id') is None:
                raise MissingParameters('user_id')

            if type(request.data.get('user_id')) != str:
                raise WrongTypeParameter(
                    fieldName="user_id",
                    fieldTypeExpected="str",
                    fieldTypeReceived=request.data.get('user_id').__class__.__name__
                )

            if not request.data.get('code'):
                raise MissingParameters('code')

            user = self.GetEnrollmentUsecase(
                user_id=request.data.get('user_id'),
                code=request.data.get('code')
            )

            viewmodel = GetEnrollmentViewmodel(user)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
