import boto3
import time

from src.shared.environments import Environments
from src.shared.infra.repositories.activity_repository_dynamo import ActivityRepositoryDynamo
from src.shared.infra.repositories.activity_repository_mock import ActivityRepositoryMock


def setup_dynamo_table():
    print('Setting up dynamo table...')
    dynamo_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    tables = dynamo_client.list_tables()['TableNames']

    if not tables:
        print('Creating table...')
        dynamo_client.create_table(
            TableName="smile_mss_activity-table",
            KeySchema=[
                {
                    'AttributeName': 'PK',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'SK',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'SK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI1-PK',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'GSI1-SK',
                    'AttributeType': 'S'
                }
            ],
            BillingMode='PAY_PER_REQUEST',
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'GSI1',
                    'KeySchema': [
                        {
                            'AttributeName': 'GSI1-PK',
                            'KeyType': 'HASH'
                        },
                        {
                            'AttributeName': 'GSI1-SK',
                            'KeyType': 'RANGE'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    }
                }
            ]
        )
        print('Table "Smile_Activity-table" created!\n')
    else:
        print('Table already exists!\n')


def load_mock_to_local_dynamo():

    if Environments.get_envs().endpoint_url == 'http://localhost:8000':
        setup_dynamo_table()

    mock_repo = ActivityRepositoryMock()
    dynamo_repo = ActivityRepositoryDynamo()

    print('Loading mock data to dynamo...')

    print('Loading activities...')
    count = 0
    for activity in mock_repo.activities:
        print(f'Loading activity {activity.code} | {activity.title}...')
        dynamo_repo.create_activity(activity)
        count += 1
    print(f'{count} activities loaded!\n')

    print('Loading enrollment...')
    count = 0
    for enrollment in mock_repo.enrollments:
        print(f'Loading enrollment {enrollment.activity_code} | {enrollment.user_id}...')
        dynamo_repo.create_enrollment(enrollment)
        count += 1
    print(f'{count} enrollments loaded!\n')

    print('Done!')

def load_test():

    if Environments.get_envs().endpoint_url == 'http://localhost:8000':
        setup_dynamo_table()

    mock_repo = ActivityRepositoryMock()
    dynamo_repo = ActivityRepositoryDynamo()

    print('Loading mock data to dynamo...')

    print('Loading activities with enrollments...')
    
    activity_example = mock_repo.activities[0]
    enrollment_example = mock_repo.enrollments[0]

    start = time.time()
    for i in range(1000):
        activity_example.code = f"ACT{i}"
        activity_example.title = f"Activity {i}"
        dynamo_repo.create_activity(activity_example)

        for j in range(50):
            enrollment_example.activity_code = f"ACT{i}"
            enrollment_example.user_id = f"USER{i}{j}"
            dynamo_repo.create_enrollment(enrollment_example)
        
        print(f'Loading activity {activity_example.code} | {activity_example.title}...')
    end = time.time()
    
    print(f'1000 activities with 50 enrollments each loaded in {end - start} seconds!\n')

if __name__ == '__main__':
    # load_test()
