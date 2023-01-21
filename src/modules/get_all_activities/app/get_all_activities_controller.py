from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError
from .get_all_activities_usecase import GetAllActivitiesUsecase
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .get_all_activities_viewmodel import GetAllActivitiesViewmodel


class GetAllActivitiesController:

    def __init__(self, usecase: GetAllActivitiesUsecase):
        self.GetAllActivitiesUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            all_activities = self.GetAllActivitiesUsecase()

            viewmodel = GetAllActivitiesViewmodel(all_activities)

            return OK(viewmodel.to_dict())

        except Exception as err:
            return InternalServerError(body=err.args[0])
