"""
usecase: verificar role, verificar se a pessoa está inscrita, checar o status da inscrição da pessoa,
UPDATE a depender do status da pessoa.



manuel change attendance (user_id, code (da atv), state (futuro)) -> Briqz

    - ENROLLED <--> COMPLETED (unitária)
    - prof responsible verificação
    - um por um
    - update_enrollment do cara -> STATE
        return activity with enrollments

"""
from src.shared.domain.entities.user import User
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.repositories.user_repository_interface import IUserRepository
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import ForbiddenAction, NoItemsFound


class ManualAttendanceChangeUsecase:
    def __init__(self, repo_activity: IActivityRepository, repo_user: IUserRepository):
        self.repo_activity = repo_activity
        self.repo_user = repo_user

    def __call__(self, code: str, requester_user: User, user_id: str, new_state: ENROLLMENT_STATE):

        if type(code) != str:
            raise EntityError('activity_code')

        if type(user_id) != str:
            raise EntityError('user_id')

        if type(new_state) != ENROLLMENT_STATE:
            raise EntityError('enrollment_state')

        if requester_user.role != ROLE.PROFESSOR:
            raise ForbiddenAction("user: only responsible professors can do that")

        enrollment = self.repo_activity.get_enrollment(code=code, user_id=user_id)

        if enrollment is None:
            raise NoItemsFound('enrollment')

        if new_state != ENROLLMENT_STATE.COMPLETED and new_state != ENROLLMENT_STATE.ENROLLED:
            raise EntityError('state')

        if new_state == ENROLLMENT_STATE.COMPLETED:
            if enrollment.state != ENROLLMENT_STATE.ENROLLED:
                raise ForbiddenAction("enrollment: can\'t confirm it")

        if new_state == ENROLLMENT_STATE.ENROLLED:
            if enrollment.state != ENROLLMENT_STATE.COMPLETED:
                raise ForbiddenAction('enrollment: can\'t enroll')

        new_enrollment = self.repo_activity.update_enrollment(
            user_id=enrollment.user_id,
            code=enrollment.activity_code,
            new_state=new_state
        )


        activity, all_enrollments = self.repo_activity.get_activity_with_enrollments(code=code) #!! to do refat in future, less requests

        enrollments = [enrollment for enrollment in all_enrollments if enrollment.state == ENROLLMENT_STATE.ENROLLED or
                       enrollment.state == ENROLLMENT_STATE.COMPLETED]

        user_id_list = list()
        for enrollment in enrollments:
            user_id_list.append(enrollment.user_id)
        users = self.repo_user.get_users(user_id_list)
        users_dict = {user.user_id: user for user in users}
        activity_dict = {
            "activity": activity,
            "enrollments": [
                (enrollment, users_dict.get(enrollment.user_id, "NOT_FOUND")) for enrollment in enrollments
                ]
        }

        return new_enrollment
