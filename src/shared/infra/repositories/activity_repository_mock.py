from typing import List

from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository


class ActivityRepositoryMock(IActivityRepository):
    speakers: List[Speaker]
    users: List[User]


    def __init__(self):
        self.speakers = [
            Speaker(name="Vitor Briquez", bio="Incrível", company="Apple"),
            Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"),
            Speaker(name="Daniel Romanato", bio="Buscando descobrir o mundo", company="Samsung")
        ]
        self.users = [
            User(name="João Vilas", role=ROLE.ADMIN, user_id="db43"),
            User(name="Bruno Soller", role=ROLE.STUDENT, user_id="b16f"),
            User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="d7f1"),
            User(name="Pedro Marcelino", role=ROLE.INTERNATIONAL_STUDENT, user_id="80fb"),
            User(name="Hector Guerrini", role=ROLE.EXTERNAL, user_id="9257"),
            User(name="Ricardo Soller", role=ROLE.EMPLOYEE, user_id="f664"),
            User(name="Marcos Romanato", role=ROLE.STUDENT, user_id="bea2"),
            User(name="Marco Briquez", role=ROLE.STUDENT, user_id="f26f"),
            User(name="Simone Romanato", role=ROLE.EXTERNAL, user_id="d23a"),
            User(name="Viviani Soller", role=ROLE.EXTERNAL, user_id="d673"),
        ]
