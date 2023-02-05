from src.shared.environments import Environments

import os
import boto3

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
    for enrollemnt in mock_repo.enrollments:
        print(f'Loading enrollment {enrollemnt.activity_code} | {enrollemnt.user_id}...')
        dynamo_repo.create_enrollment(enrollemnt)
        count += 1
    print(f'{count} enrollments loaded!\n')

    print('Done!')


if __name__ == '__main__':
    load_mock_to_local_dynamo()
