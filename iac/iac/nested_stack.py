from aws_cdk.aws_apigateway import IntegrationResponse, MethodResponse, IntegrationResponse, MethodResponse
from constructs import Construct
from aws_cdk import App, CfnOutput, NestedStack, NestedStackProps, Stack
from aws_cdk.aws_apigateway import Deployment, Method, MockIntegration, PassthroughBehavior, RestApi, Stage

#
# This file showcases how to split up a RestApi's Resources and Methods across nested stacks.
#
# The root stack 'RootStack' first defines a RestApi.
# Two nested stacks BooksStack and PetsStack, create corresponding Resources '/books' and '/pets'.
# They are then deployed to a 'prod' Stage via a third nested stack - DeployStack.
#
# To verify this worked, go to the APIGateway
#

class RootStack(Stack):
    def __init__(self, scope):
        super().__init__(scope, "integ-restapi-import-RootStack")

        rest_api = RestApi(self, "RestApi",
            cloud_watch_role=True,
            deploy=False
        )
        rest_api.root.add_method("ANY")

        certificate_db_stack = CertificateDBStack(self,
            rest_api_id=rest_api.rest_api_id,
            root_resource_id=rest_api.rest_api_root_resource_id
        )
        certificate_lambda_stack = CertificateLambdaStack(self,
            rest_api_id=rest_api.rest_api_id,
            root_resource_id=rest_api.rest_api_root_resource_id
        )
        DeployStack(self,
            rest_api_id=rest_api.rest_api_id,
            methods=certificate_db_stack.methods.concat(certificate_lambda_stack.methods)
        )

        CfnOutput(self, "SmileActivity2024Stackdev",
            value=f"https://q05zkbsv0g.execute-api.sa-east-1.amazonaws.com/prod/")

        CfnOutput(self, "SmileActivity2024Stackdev-certificates-s3",
            value=f"https://d1yjyfuur24yxm.cloudfront.net/")
        
#SmileActivity2024Stackdev
class SmileLambdaStack(NestedStack):

    def __init__(self, scope, *, restApiId, rootResourceId, parameters=None, timeout=None, notificationArns=None, removalPolicy=None, description=None):
        super().__init__(scope, "integ-restapi-import-PetsStack", restApiId=restApiId, rootResourceId=rootResourceId, parameters=parameters, timeout=timeout, notificationArns=notificationArns, removalPolicy=removalPolicy, description=description)

        api = RestApi.from_rest_api_attributes(self, "RestApi",
            rest_api_id=rest_api_id,
            root_resource_id=root_resource_id
        )

        method = api.root.add_resource("pets").add_method("GET", MockIntegration(
            integration_responses=[IntegrationResponse(
                status_code="200"
            )],
            passthrough_behavior=PassthroughBehavior.NEVER,
            request_templates={
                "application/json": "{ "statusCode": 200 }"
            }
        ),
            method_responses=[MethodResponse(status_code="200")]
        )

        self.methods.push(method)

class BooksStack(NestedStack):

    def __init__(self, scope, *, restApiId, rootResourceId, parameters=None, timeout=None, notificationArns=None, removalPolicy=None, description=None):
        super().__init__(scope, "integ-restapi-import-BooksStack", restApiId=restApiId, rootResourceId=rootResourceId, parameters=parameters, timeout=timeout, notificationArns=notificationArns, removalPolicy=removalPolicy, description=description)

        api = RestApi.from_rest_api_attributes(self, "RestApi",
            rest_api_id=rest_api_id,
            root_resource_id=root_resource_id
        )

        method = api.root.add_resource("books").add_method("GET", MockIntegration(
            integration_responses=[IntegrationResponse(
                status_code="200"
            )],
            passthrough_behavior=PassthroughBehavior.NEVER,
            request_templates={
                "application/json": "{ "statusCode": 200 }"
            }
        ),
            method_responses=[MethodResponse(status_code="200")]
        )

        self.methods.push(method)

class DeployStack(NestedStack):
    def __init__(self, scope, *, restApiId, methods=None, parameters=None, timeout=None, notificationArns=None, removalPolicy=None, description=None):
        super().__init__(scope, "integ-restapi-import-DeployStack", restApiId=restApiId, methods=methods, parameters=parameters, timeout=timeout, notificationArns=notificationArns, removalPolicy=removalPolicy, description=description)

        deployment = Deployment(self, "Deployment",
            api=RestApi.from_rest_api_id(self, "RestApi", rest_api_id)
        )
        if methods:
            for method in methods:
                deployment.node.add_dependency(method)
        Stage(self, "Stage", deployment=deployment)

RootStack(App())