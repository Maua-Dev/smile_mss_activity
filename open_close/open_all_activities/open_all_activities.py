import json

from src.shared.environments import Environments

repo_activity = Environments.get_activity_repo()()

def lambda_handler(event, context):

    all_activities = repo_activity.get_all_activities()

    activities_to_update = []

    for activity in all_activities:
        if not activity.accepting_new_enrollments:
            activity.accepting_new_enrollments = True
            activities_to_update.append(activity)


    if len(activities_to_update) == 0:
        return {
            'statusCode': 200,
            'body': json.dumps('Nenhuma atividade encontrada para atualizar')
        }

    repo_activity.batch_update_activities(activities_to_update)

    activities_title = [f"{activity.code} - {activity.title}"for activity in activities_to_update]

    return {
        'statusCode': 200,
        'body': json.dumps('Inscrições abertas com sucesso para as atividades encontradas'
                            f' {" ".join(activities_title)}')
    }
