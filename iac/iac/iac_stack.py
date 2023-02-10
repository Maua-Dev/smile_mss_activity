from aws_cdk import (
    # Duration,
    Stack, aws_cognito
    # aws_sqs as sqs,
)
from aws_cdk.aws_cognito import IUserPool
from constructs import Construct

from .dynamo_stack import DynamoStack
from .lambda_stack import LambdaStack
from aws_cdk.aws_apigateway import RestApi, Cors, CognitoUserPoolsAuthorizer


class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.rest_api = RestApi(self, "Smile_RestApi",
                                rest_api_name="Smile_RestApi",
                                description="This is the Smile RestApi",
                                default_cors_preflight_options=
                                {
                                    "allow_origins": Cors.ALL_ORIGINS,
                                    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                                    "allow_headers": ["*"]
                                },
                                )

        api_gateway_resource = self.rest_api.root.add_resource("mss-activity", default_cors_preflight_options=
        {
            "allow_origins": Cors.ALL_ORIGINS,
            "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": Cors.DEFAULT_HEADERS
        }
                                                                   )

        self.dynamo_stack = DynamoStack(self)

        ENVIRONMENT_VARIABLES = {
            "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table.table_name,
            "DYNAMO_PARTITION_KEY": "PK",
            "DYNAMO_SORT_KEY": "SK",
            "STAGE": "DEV",
            "DYNAMO_GSI_PARTITION_KEY": "GSI1-PK",
            "DYNAMO_GSI_SORT_KEY": "GSI1-SK",
            "USER_POOL": "us-east-2_uxbW9MaCL",
            "REGION": self.region,
        }

        auth = CognitoUserPoolsAuthorizer(self, "SmileCognitoAuthorizer",
                                                     cognito_user_pools=[aws_cognito.UserPool.from_user_pool_id(self, id="smilecognitostacksmileuserpool5E2198EB-lATo3d8qwZx0" ,user_pool_id="us-east-2_uxbW9MaCL")] #todo use envs
                                                     )

        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES, authorizer=auth)





