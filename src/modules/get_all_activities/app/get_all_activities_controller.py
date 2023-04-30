from src.shared.domain.observability.observability_interface import IObservability
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, InternalServerError
from .get_all_activities_usecase import GetAllActivitiesUsecase
from .get_all_activities_viewmodel import GetAllActivitiesViewmodel


class GetAllActivitiesController:

    def __init__(self, usecase: GetAllActivitiesUsecase, observability: IObservability):
        self.GetAllActivitiesUsecase = usecase
        self.observability = observability

    def __call__(self, request: IRequest) -> IResponse:
        try:
            self.observability.log_controller_in()
            all_activities = self.GetAllActivitiesUsecase()

            viewmodel = GetAllActivitiesViewmodel(all_activities)
            self.observability.log_controller_out(input='', status_code=200)
            return OK(viewmodel.to_dict())

        except Exception as err:
            self.observability.log_exception(status_code=500, exception_name=err.__class__.__name__, message=err.args[0])
            return InternalServerError(body=err.args[0])
