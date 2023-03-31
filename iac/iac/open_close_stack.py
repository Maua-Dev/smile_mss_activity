from constructs import Construct

from aws_cdk import (
    aws_lambda as lambda_,
)


class OpenCloseStack(Construct):
    def __init__(self, scope: Construct, id: str,  environment_variables: dict, activity_layer, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.open_all_activities_function = lambda_.Function(self, "Open_all_activities",
                                                             code=lambda_.Code.from_asset(
                                                                 "../open_close/open_all_activities"),
                                                             handler="open_all_activities.lambda_handler",
                                                             runtime=lambda_.Runtime.PYTHON_3_9,
                                                             environment=environment_variables,
                                                             layers=[activity_layer]
                                                             )

        self.close_all_activities_function = lambda_.Function(self, "Close_all_activities",
                                                              code=lambda_.Code.from_asset(
                                                                  "../open_close/close_all_activities"),
                                                              handler="close_all_activities.lambda_handler",
                                                              runtime=lambda_.Runtime.PYTHON_3_9,
                                                              environment=environment_variables,
                                                              layers=[activity_layer]
                                                              )

