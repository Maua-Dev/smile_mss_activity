from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError


class GetActivitiesResponsibleProfessorUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user=IUserRepository):
        self.repo_activity = repo_activity
        self.repo_user = repo_user

    def __call__(self, requester_user: User) -> dict:

        if requester_user.role != ROLE.PROFESSOR:
            raise EntityError("requester_user")

        all_activities_with_enrollments = self.repo_activity.get_all_activities_admin()

        specific_professor_activities_with_enrollments = [activity_with_enrollments for activity_with_enrollments in
                                                          all_activities_with_enrollments
                                                          if requester_user in activity_with_enrollments[0].responsible_professors]
        user_id_list = list()

        for activity, enrollments in specific_professor_activities_with_enrollments:
            user_id_list.extend([enrollment.user_id for enrollment in enrollments if enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.COMPLETED])

        set_user_id_list = set(user_id_list)

        users = self.repo_user.get_users(list(set_user_id_list))

        users_dict = {user.user_id: user for user in users}

        specific_professor_activities_with_enrollments_dict = dict()
        for activity, enrollments in specific_professor_activities_with_enrollments:
            specific_professor_activities_with_enrollments_dict[activity.code] = {
                "activity": activity,
                "enrollments": [
                    (enrollment, users_dict.get(enrollment.user_id, "NOT_FOUND")) for enrollment in enrollments if enrollment.state == ENROLLMENT_STATE.ENROLLED or enrollment.state == ENROLLMENT_STATE.COMPLETED
                ]
            }

        return specific_professor_activities_with_enrollments_dict







