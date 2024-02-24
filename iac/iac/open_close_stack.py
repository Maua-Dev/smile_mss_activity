from constructs import Construct

from aws_cdk import (
    aws_lambda as lambda_,
)


class OpenCloseStack(Construct):
    def __init__(self, scope: Construct, id: str,  environment_variables: dict, activity_layer, power_tools_layer, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
