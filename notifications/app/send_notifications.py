from datetime import datetime, timedelta

from .send_email import send_email_notification
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.environments import Environments


repo_activity = Environments.get_activity_repo()()
repo_user = Environments.get_user_repo()()


def lambda_handler(event, context):
    all_activities = repo_activity.get_all_activities_admin()

    now_timestamp = datetime.now().timestamp()*1000
    activities_to_send = list(filter(lambda x: x[0].start_date - now_timestamp <= timedelta(minutes=15).total_seconds()*1000 and now_timestamp <= x[0].start_date, all_activities))

    activities_to_send_enrolled = list()

    for activity, enrollments in activities_to_send:
        activities_to_send_enrolled.append((activity, [enrollment for enrollment in enrollments if enrollment.state == ENROLLMENT_STATE.ENROLLED]))

    user_id_list = list()
    for activity, enrollments in activities_to_send_enrolled:
        user_id_list.extend([enrollment.user_id for enrollment in enrollments if enrollment.state == ENROLLMENT_STATE.ENROLLED])

    user_id_list = list(set(user_id_list))

    users = repo_user.get_users_info(user_id_list)

    users_dict = {user.user_id: user for user in users}

    for activity, enrollments in activities_to_send_enrolled:
        send_email_notification(activity, [users_dict.get(enrollment.user_id, "NOT_FOUND") for enrollment in enrollments])
