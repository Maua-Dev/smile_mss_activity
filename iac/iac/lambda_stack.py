
from aws_cdk import (
    aws_lambda as lambda_,
    NestedStack, Duration
)
from constructs import Construct
from aws_cdk.aws_apigateway import Resource, LambdaIntegration, CognitoUserPoolsAuthorizer


class LambdaStack(Construct):

    functions_that_need_dynamo_permissions = []
    functions_that_need_cognito_permissions = []

    def create_lambda_api_gateway_integration(self, module_name: str, method: str, mss_student_api_resource: Resource, environment_variables: dict = {"STAGE": "TEST"}, authorizer=None):
        function = lambda_.Function(
            self, module_name.title(),
            code=lambda_.Code.from_asset(f"../src/modules/{module_name}"),
            handler=f"app.{module_name}_presenter.lambda_handler",
            memory_size=512,
            runtime=lambda_.Runtime.PYTHON_3_9,
            layers=[self.lambda_layer],
            environment=environment_variables,
            timeout=Duration.seconds(15)
        )

        mss_student_api_resource.add_resource(module_name.replace("_", "-")).add_method(method,
                                                                                        integration=LambdaIntegration(
                                                                                            function),
                                                                                        authorizer=authorizer)

        return function

    def __init__(self, scope: Construct, api_gateway_resource: Resource, environment_variables: dict, authorizer: CognitoUserPoolsAuthorizer) -> None:
        super().__init__(scope, "Smile_Lambdas")

        self.lambda_layer = lambda_.LayerVersion(self, "Smile_Layer",
                                                 code=lambda_.Code.from_asset("./lambda_layer_out_temp"),
                                                 compatible_runtimes=[lambda_.Runtime.PYTHON_3_9]
                                                 )

        self.enroll_activity_function = self.create_lambda_api_gateway_integration(
            module_name="enroll_activity",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.drop_activity_function = self.create_lambda_api_gateway_integration(
            module_name="drop_activity",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_enrollment_function = self.create_lambda_api_gateway_integration(
            module_name="get_enrollment",
            method="GET",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.create_activity_function = self.create_lambda_api_gateway_integration(
            module_name="create_activity",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.delete_activity_function = self.create_lambda_api_gateway_integration(
            module_name="delete_activity",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.update_activity_function = self.create_lambda_api_gateway_integration(
            module_name="update_activity",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_all_activities_function = self.create_lambda_api_gateway_integration(
            module_name="get_all_activities",
            method="GET",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables
        )

        self.get_all_activities_admin_function = self.create_lambda_api_gateway_integration(
            module_name="get_all_activities_admin",
            method="GET",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_enrollments_by_user_function = self.create_lambda_api_gateway_integration(
            module_name="get_enrollments_by_user",
            method="GET",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
            )

        self.get_activity_with_enrollments_function = self.create_lambda_api_gateway_integration(
            module_name="get_activity_with_enrollments",
            method="GET",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.get_all_activities_logged_function = self.create_lambda_api_gateway_integration(
            module_name="get_all_activities_logged",
            method="GET",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.generate_attendance_confirmation_function = self.create_lambda_api_gateway_integration(
            module_name="generate_attendance_confirmation",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.confirm_attendance_function = self.create_lambda_api_gateway_integration(
            module_name="confirm_attendance",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.delete_attendance_confirmation_function = self.create_lambda_api_gateway_integration(
            module_name="delete_attendance_confirmation",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.manual_attendance_change_function = self.create_lambda_api_gateway_integration(
            module_name="manual_attendance_change",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )
        self.manual_drop_activity_function = self.create_lambda_api_gateway_integration(
            module_name="manual_drop_activity",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.enroll_activity_admin_function = self.create_lambda_api_gateway_integration(
            module_name="enroll_activity_admin",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.delete_user_function = self.create_lambda_api_gateway_integration(
            module_name="delete_user",
            method="POST",
            mss_student_api_resource=api_gateway_resource,
            environment_variables=environment_variables,
            authorizer=authorizer
        )

        self.functions_that_need_dynamo_permissions = [
            self.enroll_activity_function,
            self.drop_activity_function,
            self.get_enrollment_function,
            self.create_activity_function,
            self.delete_activity_function,
            self.update_activity_function,
            self.get_all_activities_function,
            self.get_all_activities_admin_function,
            self.get_enrollments_by_user_function,
            self.get_all_activities_logged_function,
            self.generate_attendance_confirmation_function,
            self.confirm_attendance_function,
            self.delete_attendance_confirmation_function,
            self.manual_attendance_change_function,
            self.get_activity_with_enrollments_function,
            self.manual_drop_activity_function,
            self.enroll_activity_admin_function,
            self.delete_user_function
        ]

        self.functions_that_need_cognito_permissions = [
            self.create_activity_function,
            self.update_activity_function,
            self.get_all_activities_admin_function,
            self.get_activity_with_enrollments_function,
            self.manual_attendance_change_function,
            self.manual_drop_activity_function,
            self.enroll_activity_admin_function,
            self.delete_user_function
        ]


