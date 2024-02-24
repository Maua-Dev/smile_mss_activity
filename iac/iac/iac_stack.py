import os


from aws_cdk import (
    # Duration,
    Stack, aws_cognito,
    # aws_sqs as sqs,
    aws_iam, Fn, aws_s3
)
from constructs import Construct

from .certificates_lambda_stack import CertificatesLambdaStack
from .activity_s3_bucket import ActivityS3Bucket
from .dynamo_stack import DynamoStack
from .event_bridge_stack import EventBridgeStack
from .lambda_stack import LambdaStack
from .open_close_stack import OpenCloseStack
from aws_cdk.aws_apigateway import RestApi, Cors, CognitoUserPoolsAuthorizer

class IacStack(Stack):
    lambda_stack: LambdaStack

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.user_pool_name = os.environ.get("USER_POOL_NAME")
        self.user_pool_arn = os.environ.get("USER_POOL_ARN")
        self.user_pool_id = os.environ.get("USER_POOL_ID")
        self.github_ref = os.environ.get("GITHUB_REF")
        self.aws_region = os.environ.get("AWS_REGION")
        self.ses_region = os.environ.get("SES_REGION")
        self.mss_name = os.environ.get("MSS_NAME")

        if 'prod' in self.github_ref:
            stage = 'PROD'

        elif 'homolog' in self.github_ref:
            stage = 'HOMOLOG'

        elif 'dev' in self.github_ref:
            stage = 'DEV'

        else:
            stage = 'TEST'

        self.rest_api = RestApi(self, "Smile_RestApi",
                                rest_api_name="Smile_RestApi",
                                description="This is the Smile RestApi",
                                default_cors_preflight_options=
                                {
                                    "allow_origins": Cors.ALL_ORIGINS,
                                    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                                    "allow_headers": ["*"]
                                }
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
            "STAGE": stage,
            "DYNAMO_GSI_PARTITION_KEY": "GSI1-PK",
            "DYNAMO_GSI_SORT_KEY": "GSI1-SK",
            "USER_POOL":  self.user_pool_id,
            "SES_REGION": self.ses_region,
            "REGION": self.aws_region,
            "MSS_NAME": self.mss_name
        }

        auth = CognitoUserPoolsAuthorizer(self, f"smile_cognito_stack_{self.github_ref}",
                                                     cognito_user_pools=[aws_cognito.UserPool.from_user_pool_id(self, id=self.user_pool_name, user_pool_id=self.user_pool_id)]
                                                     )

        self.lambda_stack = LambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=ENVIRONMENT_VARIABLES, authorizer=auth)

        self.event_bridge = EventBridgeStack(self, "SmileEventBridge", environment_variables=ENVIRONMENT_VARIABLES, lambda_layer=self.lambda_stack.lambda_layer, power_tools_layer=self.lambda_stack.lambda_power_tools)

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

        self.lambda_stack.drop_activity_function.add_to_role_policy(cognito_admin_policy)

        self.lambda_stack.manual_drop_activity_function.add_to_role_policy(cognito_admin_policy)

        ses_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "ses:*",
            ],
            resources=[
                "*"
            ]
        )

        functions_that_need_email_permissions = [
            self.lambda_stack.drop_activity_function,
            self.lambda_stack.manual_drop_activity_function,
            self.event_bridge.send_notification_function,
            self.lambda_stack.delete_user_function
        ]

        for f in functions_that_need_email_permissions:
            f.add_environment("HIDDEN_COPY", os.environ.get("HIDDEN_COPY"))
            f.add_environment("FROM_EMAIL", os.environ.get("FROM_EMAIL"))
            f.add_environment("REPLY_TO_EMAIL", os.environ.get("REPLY_TO_EMAIL"))
            f.add_to_role_policy(ses_admin_policy)

        sns_admin_policy = aws_iam.PolicyStatement(
            effect=aws_iam.Effect.ALLOW,
            actions=[
                "sns:*",
            ],
            resources=[
                "*"
            ]
        )

        self.event_bridge.send_notification_function.add_to_role_policy(sns_admin_policy)

        bucket_name = Fn.import_value(f"CertificateBucketNameValue2024")

        cdn_url = Fn.import_value(f"CertificateBucketCdnUrlValue2024")

        environment_variables_certificate = {
            "STAGE": stage,
            "BUCKET_NAME": bucket_name,
            "DYNAMO_TABLE_NAME": self.dynamo_stack.dynamo_table.table_name,
            "DYNAMO_PARTITION_KEY": "PK",
            "DYNAMO_SORT_KEY": "SK",
            "DYNAMO_GSI_PARTITION_KEY": "GSI1-PK",
            "DYNAMO_GSI_SORT_KEY": "GSI1-SK",
            "USER_POOL": self.user_pool_id,
            "REGION": self.aws_region,
            "HASH_KEY": os.environ.get("HASH_KEY"),
            "CDN_URL": cdn_url
        }

        self.lambda_stack_certificate = CertificatesLambdaStack(self, api_gateway_resource=api_gateway_resource,
                                        environment_variables=environment_variables_certificate, authorizer=auth)

        self.lambda_stack_certificate.generate_certificate_function.add_to_role_policy(cognito_admin_policy)

        bucket = aws_s3.Bucket.from_bucket_name(self, "MyBucket", bucket_name)

        bucket.grant_put(self.lambda_stack_certificate.generate_certificate_function)

        bucket_all_policy = aws_iam.PolicyStatement(
            actions=["*", "s3:*"],
            resources=[bucket.bucket_arn + "/*"]
        )

        self.lambda_stack_certificate.generate_certificate_function.add_to_role_policy(bucket_all_policy)

        # grant read bucket
        bucket.grant_read(self.lambda_stack_certificate.get_certificate_function)
        self.lambda_stack_certificate.get_certificate_function.add_to_role_policy(aws_iam.PolicyStatement(
            actions=['s3:GetObject', 's3:listObjects'],
            resources=[bucket.bucket_arn + "/*"]
        ))

        self.dynamo_stack.dynamo_table.grant_read_write_data(self.lambda_stack_certificate.generate_certificate_function)
        self.dynamo_stack.dynamo_table.grant_read_write_data(self.lambda_stack_certificate.get_certificate_function)

        delete_user_variables = {
            "BUCKET_NAME": bucket_name,
            "HASH_KEY": os.environ.get("HASH_KEY"),
            "CDN_URL": cdn_url
        }

        for key, value in delete_user_variables.items():
            self.lambda_stack.delete_user_function.add_environment(key, value)

        self.lambda_stack.delete_user_function.add_to_role_policy(bucket_all_policy)
        
        bucket.grant_read_write(self.lambda_stack.delete_user_function)
        
