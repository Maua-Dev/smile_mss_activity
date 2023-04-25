from src.shared.domain.observability.observability_interface import IObservability


class ObservabilityMock(IObservability):
    module_name: str
    mss_name: str
    
    def __init__(self, module_name: str) -> None:
        super().__init__(module_name=module_name)
    
    def _log_info(self, message: str) -> None:
        print(message)
        
    def log_controller_in(self) -> None:
        self._log_info("In Controller")
        
    def log_controller_out(self, input: str, status_code: int) -> None:
        self._log_info(
            {
                "statusCode": status_code,
                "message": f"Out of Controller with this input: {input}"
            }
        )
        
    def log_usecase_in(self) -> None:
        self._log_info("In Usecase")
        
    def log_usecase_out(self) -> None:
        self._log_info("Out of Usecase")
            
    def log_exception(self, status_code: int, exception_name: str, message: str) -> None:
        print(f"{exception_name} with status code {status_code} was raised because {message}")
        
    def log_simple_lambda_in(self) -> None:
        print("In Lambda")
    
    def log_simple_lambda_out(self) -> None:
        print("Out of Lambda")
            
    def _add_metric(self, name: str, unit: str, value: float) -> None:
        print(f"Metric {name} added with value {value} in {unit}")
            
    def add_confirm_attendance_count_metric(self) -> None:
        self._add_metric(name="ConfirmAttendanceCount", unit="Count", value=1)
            
    def add_drop_activity_count_metric(self) -> None:
        self._add_metric(name="DropActivityCount", unit="Count", value=1)
    
    def add_enroll_activity_count_metric(self) -> None:
        self._add_metric(name="EnrollActivityCount", unit="Count", value=1)
    
    def add_get_all_activities_count_metric(self) -> None:
        self._add_metric(name="GetAllActivitiesCount", unit="Count", value=1)
    
    def add_user_email_notified_count_metric(self) -> None:
        self._add_metric(name="UsersEmailNotified", unit="Count", value=1)
    
    def presenter_decorators(self, presenter) -> None:
        def presenter_wrapper(event, context):    
            response = presenter(event, context)
            
            return response
        return presenter_wrapper
    
    def handler_decorators(self, handler) -> None:
        def handler_wrapper(event, context):    
            response = handler(event, context)
            
            return response
        return handler_wrapper