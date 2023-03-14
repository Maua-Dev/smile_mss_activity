import os

from aws_cdk import (
    # Duration,
    Stack, aws_cognito,
    # aws_sqs as sqs,
    aws_iam
)
from aws_cdk.aws_cognito import IUserPool
from constructs import Construct

from .dynamo_stack import DynamoStack
from .event_bridge_stack import EventBridgeStack
from .lambda_stack import LambdaStack
from aws_cdk.aws_apigateway import RestApi, Cors, CognitoUserPoolsAuthorizer

class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.user_pool_name = os.environ.get("USER_POOL_NAME")
        self.user_pool_arn = os.environ.get("USER_POOL_ARN")
        self.user_pool_id = os.environ.get("USER_POOL_ID")
        self.github_ref = os.environ.get("GITHUB_REF")

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
            "USER_POOL":  self.user_pool_id,
            "REGION": self.region,
        }

        auth = CognitoUserPoolsAuthorizer(self, f"smile_cognito_stack_{self.github_ref}",
                                                     cognito_user_pools=[aws_cognito.UserPool.from_user_pool_id(self, id=self.user_pool_name, user_pool_id=self.user_pool_id)]
                                                     )

        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES, authorizer=auth)

        self.event_bridge = EventBridgeStack(self, "SmileEventBridge", environment_variables=ENVIRONMENT_VARIABLES, lambda_layer=self.lambda_stack.lambda_layer)

        self.dynamo_stack.dynamo_table.grant_read_write_data(self.event_bridge.close_activity_date_function)
        self.dynamo_stack.dynamo_table.grant_read_write_data(self.event_bridge.send_notification_function)

        for f in self.lambda_stack.functions_that_need_dynamo_permissions:
            self.dynamo_stack.dynamo_table.grant_read_write_data(f)

        cognito_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "cognito-idp:*",
            ],
            resources=[
                self.user_pool_arn
            ]
        )

        for f in self.lambda_stack.functions_that_need_cognito_permissions:
            f.add_to_role_policy(cognito_admin_policy)

        self.event_bridge.send_notification_function.add_to_role_policy(cognito_admin_policy)

        ses_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "ses:*",
            ],
            resources=[
                "*"
            ]
        )

        self.event_bridge.send_notification_function.add_to_role_policy(ses_admin_policy)

        self.event_bridge.send_notification_function.add_environment(
            "FROM_EMAIL", os.environ.get("FROM_EMAIL")
        )

        self.event_bridge.send_notification_function.add_environment(
            "HIDDEN_COPY", os.environ.get("HIDDEN_COPY")
        )
