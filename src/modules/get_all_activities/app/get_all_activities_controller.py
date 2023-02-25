from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, InternalServerError
from .get_all_activities_usecase import GetAllActivitiesUsecase
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
