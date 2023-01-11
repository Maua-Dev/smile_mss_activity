import abc
import datetime

from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.activity import Activity
from src.shared.domain.repositories.activity_repository_interface import IActivityRepository
from src.shared.domain.entities.user import User
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.infra.repositories.activity_repository_mock import get_activity, get_user

class EnrollActivity:
    def __init__(self, repo: IActivityRepository):
        self.repo = repo
    

    def __call__(self, user_id: str, code: str) -> Enrollment:
        if not User.validate_user_id(user_id):
            raise EntityError('user_id')
    
        if type(code) is not str:
            raise EntityError('code')



        if  Activity.taken_slots >= Activity.total_slots:

            enrollement = Enrollment(
                activity =get_activity(code),
                user = get_user(user_id),
                state = ENROLLMENT_STATE.IN_QUEUE,
                date_subscribed = datetime.datetime
            )
            return self.enrollment   

        if  Activity.taken_slots < Activity.total_slots:


                enrollement = Enrollment(
                    activity =get_activity(code),
                    user = get_user(user_id),
                    state = ENROLLMENT_STATE.ENROLLED,
                    date_subscribed = datetime.datetime
                )
                return self.enrollment                      

        return self.repo.create_enrollment(enrollement)


    def get_user(self, user_id : str) -> User:
        for user in self.user:
            if User.user_id == user_id:
                return user
        return None

    def get_activity(self, code : str) -> Activity:
        for activity in self.activity:
            if Activity.code == code:
                return activity
        return None
    
    

