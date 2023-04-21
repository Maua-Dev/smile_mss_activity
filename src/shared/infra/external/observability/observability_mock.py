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
        
    def log_controller_out(self, input) -> None:
        self._log_info(f"Out of Controller with this input: {input}")
        
    def log_usecase_in(self) -> None:
        self._log_info("In Usecase")
        
    def log_usecase_out(self) -> None:
        self._log_info("Out of Usecase")
            
    def log_exception(self, message: str) -> None:
        print("Exception message: " + message)
            
    def _add_metric(self, name: str, unit: str, value: float) -> None:
        print(f"Metric {name} added with value {value} in {unit}")
            
    def add_error_count_metric(self, statusCode:int) -> None:
        self._add_metric(name="ErrorCount", unit="Count", value=1) if statusCode != 200 else None # ErrorCount metrics
            
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