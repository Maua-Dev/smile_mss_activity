from .get_activities_responsible_professor_usecase import \
    GetActivitiesResponsibleProfessorUsecase
from .get_activities_responsible_professor_viewmodel import \
    GetActivitiesResponsibleProfessorViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import BadRequest, InternalServerError, OK, Forbidden
from src.shared.infra.dto.user_api_gateway_dto import UserApiGatewayDTO


class GetActivitiesResponsibleProfessorController:

    def __init__(self, usecase: GetActivitiesResponsibleProfessorUsecase):
        self.GetActivitiesResponsibleProfessorUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('requester_user') is None:
                raise MissingParameters('requester_user')

            requester_user = UserApiGatewayDTO.from_api_gateway(request.data.get('requester_user')).to_entity()

            specific_professor_activities_with_enrollments_dict = self.GetActivitiesResponsibleProfessorUsecase(requester_user)

            viewmodel = GetActivitiesResponsibleProfessorViewmodel(specific_professor_activities_with_enrollments_dict)

            return OK(viewmodel.to_dict())

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except ForbiddenAction as err:

            return Forbidden(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
