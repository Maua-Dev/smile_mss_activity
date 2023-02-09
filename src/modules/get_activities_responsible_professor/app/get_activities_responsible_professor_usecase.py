from typing import List

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.user import User
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.helpers.errors.usecase_errors import ForbiddenAction


class GetActivitiesResponsibleProfessorUsecase:
    def __init__(self, repo_activity: IActivityRepository):
        self.repo_activity = repo_activity

    def __call__(self, requester_user: User) -> List[Activity]:
        if requester_user.role != ROLE.PROFESSOR:
            raise ForbiddenAction("requester_user, only professor can do that")

        all_activities = self.repo_activity.get_all_activities()

        specific_professor_activities = [activity_with for activity_with in
                                          all_activities
                                          if requester_user in activity_with.responsible_professors]

        return specific_professor_activities
