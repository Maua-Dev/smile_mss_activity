from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError
from .get_all_activities_admin_usecase import GetAllActivitiesAdminUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .get_all_activities_admin_viewmodel import GetAllActivitiesAdminViewmodel


class GetAllActivitiesAdminController:

    def __init__(self, usecase: GetAllActivitiesAdminUsecase):
        self.GetAllActivitiesAdminUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:

            all_activities_with_enrollments = self.GetAllActivitiesAdminUsecase()

            viewmodel = GetAllActivitiesAdminViewmodel(all_activities_with_enrollments)

            return OK(viewmodel.to_dict())

        except Exception as err:

            return InternalServerError(body=err.args[0])
