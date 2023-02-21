from constructs import Construct
from aws_cdk import (
    aws_lambda as lambda_,
    aws_events as events,
    aws_events_targets as targets,
    Duration
)


class EventBridgeStack(Construct):
    def __init__(self, scope: Construct, id: str, environment_variables: dict, lambda_layer, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        rule = events.Rule(self, "CloseActivityByDateRule",
                           enabled=False,
                           schedule=events.Schedule.cron(minute="0/30", hour="7-21", month="*", week_day="*", year="*"),
                           description="Close activity which date has already passed every 30 minutes between 7am and 9pm"
                           )
        self.close_activity_date_function = lambda_.Function(
                    self, "CloseActivityDateFunction",
                    code=lambda_.Code.from_asset("../lambda_functions"),
                    handler="close_activity_by_date.lambda_handler",
                    runtime=lambda_.Runtime.PYTHON_3_9,
                    layers=[lambda_layer],
                    timeout=Duration.seconds(15),
                    environment=environment_variables
                )

        rule.add_target(
            targets.LambdaFunction(
                self.close_activity_date_function
            )
        )
