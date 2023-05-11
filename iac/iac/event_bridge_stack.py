from constructs import Construct
from aws_cdk import (
    aws_lambda as lambda_,
    aws_events as events,
    aws_events_targets as targets,
    Duration
)


class EventBridgeStack(Construct):
    def __init__(self, scope: Construct, id: str, environment_variables: dict, lambda_layer, power_tools_layer, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        rule_close_activity = events.Rule(self, "CloseActivityByDateRule",
                           enabled=False,
                           schedule=events.Schedule.cron(minute="0/30", hour="10-00", month="*", week_day="*", year="*"),
                           description="Close activity which date has already passed every 30 minutes between 7am and 9pm in GMT -3"
                           )
        self.close_activity_date_function = lambda_.Function(
                    self, "CloseActivityDateFunction",
                    code=lambda_.Code.from_asset("../lambda_functions"),
                    handler="close_activity_by_date.lambda_handler",
                    runtime=lambda_.Runtime.PYTHON_3_9,
                    layers=[lambda_layer, power_tools_layer],
                    timeout=Duration.seconds(60),
                    environment=environment_variables
                )

        rule_close_activity.add_target(
            targets.LambdaFunction(
                self.close_activity_date_function
            )
        )

        rule_send_notification = events.Rule(self, "SendNotificationRule",
                            enabled=False,
                            schedule=events.Schedule.cron(minute="0/15", hour="09-00", month="*", week_day="*", year="*"),
                            description="Send notification to users every 15 minutes between 6am and 9pm in GMT -3"
                            )

        self.send_notification_function = lambda_.Function(
                    self, "SendNotificationFunction",
                    code=lambda_.Code.from_asset("../notifications"),
                    handler="app.send_notifications.lambda_handler",
                    runtime=lambda_.Runtime.PYTHON_3_9,
                    layers=[lambda_layer, power_tools_layer],
                    timeout=Duration.minutes(10),
                    environment=environment_variables,
                    memory_size=2048
                )

        rule_send_notification.add_target(
            targets.LambdaFunction(
                self.send_notification_function
            )
        )


