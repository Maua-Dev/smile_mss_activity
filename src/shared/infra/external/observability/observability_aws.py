import os
import time
from aws_lambda_powertools import Logger, Tracer, Metrics
from src.shared.domain.observability.observability_interface import IObservability

class ObservabilityAWS(IObservability):
    tracer: Tracer
    logger: Logger
    metrics: Metrics
    module_name: str
    mss_name: str
     
    def __init__(self, module_name: str):
        self.logger = Logger(service=module_name)
        self.tracer = Tracer(service=module_name)
        self.metrics = Metrics(namespace=module_name)
        
        super().__init__(module_name=module_name)
       
    def _log_info(self, message: str) -> None:
        self.logger.info(message)
        
    def log_controller_in(self) -> None:
        self._log_info(f"In Controller")
        
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
        self.logger.exception(
            {
                "statusCode": status_code,
                "name": exception_name,
                "message": message
            }
        )
    
    def log_simple_lambda_in(self) -> None:
        self._log_info("In Lambda")
    
    def log_simple_lambda_out(self) -> None:
        self._log_info("Out of Lambda")
            
    def _add_metric(self, name: str, unit: str, value: float) -> None:
        self.metrics.add_metric(name, unit, value)
        
    def add_user_email_notified_count_metric(self) -> None:
        self._add_metric(name="UsersEmailNotified", unit="Count", value=1)
        
    def add_error_count_metric(self, statusCode:int) -> None:
        self._add_metric(name="ErrorCount", unit="Count", value=1) if statusCode not in [200, 201] else None

    def presenter_decorators(self, presenter) -> None:
        @self.tracer.capture_method
        def presenter_wrapper(event, context):    
            
            response = presenter(event, context)
            
            return response
        return presenter_wrapper
    
    def handler_decorators(self, handler) -> None:
        @self.tracer.capture_lambda_handler
        @self.metrics.log_metrics(capture_cold_start_metric=True, default_dimensions={"environment": os.getenv("STAGE", "dev"), "mss": self.mss_name, "module": self.module_name}) # ColdStart metrics and adding dimensions
        @self.logger.inject_lambda_context(log_event=True) # Log event
        def handler_wrapper(event, context):    
            
            response = handler(event, context)
            
            return response
        return handler_wrapper