from typing import List

import boto3

from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.environments import Environments
from src.shared.infra.dto.user_cognito_dto import UserCognitoDTO


class UserRepositoryCognito(IUserRepository):
    client: boto3.client
    user_pool_id: str

    def __init__(self):
        self.client = boto3.client('cognito-idp')
        self.user_pool_id = Environments.get_envs().user_pool_id

    def get_user(self, user_id: str) -> User:
        response = self.client.list_users(
            UserPoolId=self.user_pool_id,
            Filter=f"sub = \"{user_id}\""
        )

        if len(response.get("Users")) == 0:
            return None

        user = UserCognitoDTO.from_cognito(response.get("Users")[0]).to_entity()

        return user

    def get_users(self, user_ids: List[str]) -> List[User]:

        kwargs = {
            'UserPoolId': self.user_pool_id
        }

        users_remain = True
        next_page = None
        response_users = list()

        while users_remain:
            if next_page:
                kwargs['PaginationToken'] = next_page
            response = self.client.list_users(**kwargs)

            response_users.extend(response["Users"])
            next_page = response.get('PaginationToken', None)
            users_remain = next_page is not None

        users = list()
        for user_data in response_users:
            user = UserCognitoDTO.from_cognito(user_data).to_entity()
            if user.user_id in user_ids:
                users.append(user)
                if len(users) == len(user_ids):
                    break

        return users

    def get_users_info(self, user_ids: List[str]) -> List[UserInfo]:
        kwargs = {
            'UserPoolId': self.user_pool_id
        }

        users_remain = True
        next_page = None
        response_users = list()

        while users_remain:
            if next_page:
                kwargs['PaginationToken'] = next_page
            response = self.client.list_users(**kwargs)

            response_users.extend(response["Users"])
            next_page = response.get('PaginationToken', None)
            users_remain = next_page is not None

        users = list()
        for user_data in response_users:
            user = UserCognitoDTO.from_cognito(user_data).to_entity_info()
            if user.user_id in user_ids:
                users.append(user)
                if len(users) == len(user_ids):
                    break

        return users

    def get_user_info(self, user_id: str) -> UserInfo:
        response = self.client.list_users(
            UserPoolId=self.user_pool_id,
            Filter=f"sub = \"{user_id}\""
        )

        if len(response.get("Users")) == 0:
            return None

        user = UserCognitoDTO.from_cognito(response.get("Users")[0]).to_entity_info()

        return user

    def delete_user(self, email: str) -> bool:
        try:
            response = self.client.admin_delete_user(
                UserPoolId=self.user_pool_id,
                Username=email
            )

            return response.get("ResponseMetadata").get("HTTPStatusCode") == 200

        except Exception as e:
            print(e)
            return False
