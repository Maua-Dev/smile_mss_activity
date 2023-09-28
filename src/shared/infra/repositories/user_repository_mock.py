from typing import List

from src.shared.domain.entities.user import User
from src.shared.domain.entities.user_info import UserInfo
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.user_repository_interface import IUserRepository


class UserRepositoryMock(IUserRepository):
    users: List[User]

    def __init__(self):
        self.users = [
            User(name="João Vilas", role=ROLE.ADMIN, user_id="d61dbf66-a10f-11ed-a8fc-0242ac120002"),
            User(name="Bruno Soller", role=ROLE.STUDENT, user_id="0355535e-a110-11ed-a8fc-0242ac120002"),
            User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002"),
            User(name="Pedro Marcelino", role=ROLE.INTERNATIONAL_STUDENT,
                 user_id="0355573c-a110-11ed-a8fc-0242ac120002"),
            User(name="Hector Guerrini", role=ROLE.EXTERNAL, user_id="03555872-a110-11ed-a8fc-0242ac120002"),
            User(name="Ricardo Soller", role=ROLE.EMPLOYEE, user_id="2f0df47e-a110-11ed-a8fc-0242ac120002"),
            User(name="Marcos Romanato", role=ROLE.STUDENT, user_id="38c3d7fe-a110-11ed-a8fc-0242ac120002"),
            User(name="Marco Briquez", role=ROLE.STUDENT, user_id="452a5f9a-a110-11ed-a8fc-0242ac120002"),
            User(name="Simone Romanato", role=ROLE.EXTERNAL, user_id="4d1d64ae-a110-11ed-a8fc-0242ac120002"),
            User(name="Viviani Soller", role=ROLE.EXTERNAL, user_id="5a49ad2c-a110-11ed-a8fc-0242ac120002"),
            User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"),
            User(name="Rafael Santos", role=ROLE.PROFESSOR, user_id="62cafdd4-a110-11ed-a8fc-0242ac120002"),
            User(name="Rodrigo Santos", role=ROLE.PROFESSOR, user_id="71f06f24-a110-11ed-a8fc-0242ac120002"),
            UserInfo(user_id="7"*36, name="João Vilas", role=ROLE.ADMIN, email="teste@teste.com", phone="+5511999999999", accepted_notifications_email=True, accepted_notifications_sms=True),
        ]

    def get_user(self, user_id: str) -> User:
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_users(self, user_ids: List[str]) -> List[User]:
        users = list()
        for user in self.users:
            if user.user_id in user_ids:
                users.append(user)
        return users

    def get_users_info(self, user_ids: List[str]) -> List[User]:
        users = list()
        for user in self.users:
            if user.user_id in user_ids:
                user_info = UserInfo(user_id=user.user_id, name=user.name, role=user.role, email="teste@teste.com", phone="+5511999999999", accepted_notifications_email=True, accepted_notifications_sms=True)
                users.append(user_info)
        return users

    def get_user_info(self, user_id: str) -> UserInfo:
        for user in self.users:
            if user.user_id == user_id:
                user_info = UserInfo(user_id=user.user_id, name=user.name, role=user.role, email="teste@teste.com", phone="+5511999999999", accepted_notifications_email=True, accepted_notifications_sms=True)

                return user_info

        return None

    def delete_user(self, email: str) -> bool:
        for idx, user in enumerate(self.users):
            if type(user) == UserInfo:
                if user.email == email:
                    self.users.pop(idx)
                    return True


