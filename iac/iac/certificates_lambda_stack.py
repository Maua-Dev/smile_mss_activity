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

        self.aws_account_id = os.environ.get("AWS_ACCOUNT_ID")
        self.aws_region = os.environ.get("AWS_REGION")

        self.lambda_layer_PyPDF2 = lambda_.LayerVersion.from_layer_version_arn(
            self, "PyPDF2_layer", f"arn:aws:lambda:{self.aws_region}:{self.aws_account_id}:layer:PyPDF2:2"
        )

        self.lambda_layer_reportlab = lambda_.LayerVersion.from_layer_version_arn(
            self, "reportlab_layer", f"arn:aws:lambda:{self.aws_region}:770693421928:layer:Klayers-p38-reportlab:8"
        )

        self.lambda_layer_pillow = lambda_.LayerVersion.from_layer_version_arn(
            self, "pillow_layer", f"arn:aws:lambda:{self.aws_region}:770693421928:layer:Klayers-p39-pillow:1"
        )

        # pdf_layers = PythonLayerVersion(
        #     self,
        #     'CertificatesLayer',
        #     entry='.certificates/common_layer',
        #     compatible_runtimes=[lambda_.Runtime.PYTHON_3_9],
        #     removal_policy=RemovalPolicy.DESTROY,
        # )

        self.lambda_layer_activity = lambda_.LayerVersion(self, "Smile_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                 )


        self.generate_certificate_function = lambda_.Function(
            self, "generate_certificate",
            code=lambda_.Code.from_asset(f"../certificates/generate_certificates"),
            handler=f"generate_certifificates.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer_activity, self.lambda_layer_PyPDF2, self.lambda_layer_reportlab,
                    self.lambda_layer_pillow],
            environment=environment_variables,
            timeout=Duration.seconds(15),
        )

        self.get_certificate_function = lambda_.Function(
            self, "get_certificate",
            code=lambda_.Code.from_asset(f"../certificates/get_certificates"),
            handler=f"get_certificate.lambda_handler",
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer_activity],
            environment=environment_variables,
            timeout=Duration.seconds(15),
        )

        api_gateway_resource.add_resource("get-certificate").add_method("GET",
                                                                        integration=LambdaIntegration(
                                                                            self.get_certificate_function),
                                                                        authorizer=authorizer,
                                                                        )


