import os


from aws_cdk import (
    aws_lambda as lambda_,
    Duration,
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration, CognitoUserPoolsAuthorizer, Cors


class CertificatesLambdaStack(Construct):

    def __init__(self, scope: Construct, api_gateway_resource: Resource, environment_variables: dict, authorizer: CognitoUserPoolsAuthorizer) -> None:
        super().__init__(scope, "Certificates_Lambdas")

        self.lambda_power_tools = lambda_.LayerVersion.from_layer_version_arn(self, "Lambda_Power_Tools", layer_version_arn=f"arn:aws:lambda:{os.environ.get('AWS_REGION')}:017000801446:layer:AWSLambdaPowertoolsPythonV2:22")
        self.aws_account_id = os.environ.get("AWS_ACCOUNT_ID")
        self.aws_region = os.environ.get("AWS_REGION")

        self.lambda_layer_activity = lambda_.LayerVersion(self, "Smile_Layer",
                                                          code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                          compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                          )

        self.lambda_layer_pillow = lambda_.LayerVersion(self, "pillow_Layer",
                                                                   code=lambda_.Code.from_asset(
                                                                       "./lambda_requirements_layer_temp/pillow"),
                                                                   compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                                   )

        self.generate_certificate_function = lambda_.Function(
            self, "generate_certificate",
            code=lambda_.Code.from_asset(f"../certificates/generate_certificates"),
            handler=f"generate_certifificates.lambda_handler",
            memory_size=2048,
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer_activity, self.lambda_layer_pillow, self.lambda_power_tools],
            environment=environment_variables,
            timeout=Duration.seconds(60),
        )

        self.get_certificate_function = lambda_.Function(
            self, "get_certificate",
            code=lambda_.Code.from_asset(f"../certificates/get_certificates"),
            handler=f"get_certificate.lambda_handler",
            memory_size=512,
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer_activity, self.lambda_power_tools],
            environment=environment_variables,
            timeout=Duration.seconds(15),
        )

        api_gateway_resource.add_resource("get-certificate").add_method("GET",
                                                                        integration=LambdaIntegration(
                                                                            self.get_certificate_function),
                                                                        authorizer=authorizer,
                                                                        )


