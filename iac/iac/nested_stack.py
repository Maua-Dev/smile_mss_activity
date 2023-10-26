from aws_cdk.aws_apigateway import IntegrationResponse, MethodResponse, MockIntegration, PassthroughBehavior
from aws_cdk.core import App, CfnOutput, NestedStack, Stack
from aws_cdk.aws_apigateway import Deployment, RestApi, Stage

#pip install aws-cdk.core aws-cdk.aws-apigateway

class RootStack(Stack):
    def __init__(self, scope, id):
        super().__init__(scope, id)

        rest_api = RestApi(self, "RestApi", cloud_watch_role=True, deploy=False)
        rest_api.root.add_method("ANY")

        certificate_db_stack = CertificateDBStack(self, "CertificateDBStack",
            rest_api_id=rest_api.rest_api_id,
            root_resource_id=rest_api.root.resource_id
        )
        certificate_lambda_stack = CertificateLambdaStack(self, "CertificateLambdaStack",
            rest_api_id=rest_api.rest_api_id,
            root_resource_id=rest_api.root.resource_id
        )
        DeployStack(self, "DeployStack",
            rest_api_id=rest_api.rest_api_id,
            methods=certificate_db_stack.methods + certificate_lambda_stack.methods
        )

        CfnOutput(self, "SmileActivity2024Stackdev",
            value=f"https://{rest_api.rest_api_id}.execute-api.sa-east-1.amazonaws.com/prod/")

        CfnOutput(self, "SmileActivity2024Stackdev-certificates-s3",
            value=f"https://d1yjyfuur24yxm.cloudfront.net/")


class CertificateLambdaStack(NestedStack):
    def __init__(self, scope, id, *, rest_api_id, root_resource_id, parameters=None, timeout=None, notificationArns=None, removalPolicy=None, description=None):
        super().__init__(scope, id, parameters=parameters, timeout=timeout, notificationArns=notificationArns, removalPolicy=removalPolicy, description=description)

        api = RestApi.from_rest_api_id(self, "RestApi", rest_api_id, root_resource_id=root_resource_id)

        method = api.root.add_resource("prod").add_method("GET", MockIntegration(
            integration_responses=[IntegrationResponse(status_code="200")],
            passthrough_behavior=PassthroughBehavior.NEVER,
            request_templates={
                "application/json": '{ "statusCode": 200 }'
            }
        ),
            method_responses=[MethodResponse(status_code="200")]
        )

        self.methods = [method]


class CertificateDBStack(NestedStack):
    def __init__(self, scope, id, *, rest_api_id, root_resource_id, parameters=None, timeout=None, notificationArns=None, removalPolicy=None, description=None):
        super().__init__(scope, id, parameters=parameters, timeout=timeout, notificationArns=notificationArns, removalPolicy=removalPolicy, description=description)

        api = RestApi.from_rest_api_id(self, "RestApi", rest_api_id, root_resource_id=root_resource_id)

        method = api.root.add_resource("").add_method("GET", MockIntegration(
            integration_responses=[IntegrationResponse(status_code="200")],
            passthrough_behavior=PassthroughBehavior.NEVER,
            request_templates={
                "application/json": '{ "statusCode": 200 }'
            }
        ),
            method_responses=[MethodResponse(status_code="200")]
        )

        self.methods = [method]


class DeployStack(NestedStack):
    def __init__(self, scope, id, *, rest_api_id, methods=None, parameters=None, timeout=None, notificationArns=None, removalPolicy=None, description=None):
        super().__init__(scope, id, parameters=parameters, timeout=timeout, notificationArns=notificationArns, removalPolicy=removalPolicy, description=description)

        deployment = Deployment(self, "Deployment",
            api=RestApi.from_rest_api_id(self, "RestApi", rest_api_id)
        )
        if methods:
            for method in methods:
                deployment.node.add_dependency(method)
        Stage(self, "Stage", deployment=deployment)





