import pytest

from src.shared.domain.entities.enrollment import Enrollment, User, Activity, ENROLLMENT_STATE
from src.shared.helpers.errors.domain_errors import EntityError
import datetime 


class Test_Enrollment:
    def test_enrollment(self):
        Enrollment(activity=Activity, user=User, state=ENROLLMENT_STATE, date_subscribed='')
    
    """ 
    ???
    """