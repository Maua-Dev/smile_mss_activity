import pytest
import datetime

from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.enrollment import Enrollment
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.enrollment_state_enum import ENROLLMENT_STATE
from src.shared.domain.enums.role_enum import ROLE
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Enrollment:
    def test_enrollment(self):
        enrollment = Enrollment(activity_code="1234", user_id="7f52e72c-a111-11ed-a8fc-0242ac120002", state=ENROLLMENT_STATE.ENROLLED, date_subscribed=1671728165000)

        assert type(enrollment) == Enrollment
        assert enrollment.activity_code == "1234"
        assert enrollment.user_id == "7f52e72c-a111-11ed-a8fc-0242ac120002"
        assert enrollment.state == ENROLLMENT_STATE.ENROLLED
        assert enrollment.date_subscribed == 1671728165000


    def test_enrollment_with_invalid_activity(self):
        with pytest.raises(EntityError):
            enrollment = Enrollment(activity_code=1, user_id="7f52e72c-a111-11ed-a8fc-0242ac120002", state=ENROLLMENT_STATE.ENROLLED, date_subscribed=1671728165000)

    def test_enrollment_with_invalid_user(self):
        with pytest.raises(EntityError):
            enrollment = Enrollment(activity_code="1234", user_id=1, state=ENROLLMENT_STATE.ENROLLED,
                                    date_subscribed=1671728165000)

    def test_enrollment_with_invalid_state(self):
        with pytest.raises(EntityError):
            enrollment = Enrollment(activity_code="1234", user_id="7f52e72c-a111-11ed-a8fc-0242ac120002", state="ENROLLED", date_subscribed=1671728165000)

    def test_enrollment_with_invalid_date_subscribed(self):
        with pytest.raises(EntityError):
            enrollment = Enrollment(activity_code="1234", user_id="7f52e72c-a111-11ed-a8fc-0242ac120002", state=ENROLLMENT_STATE.ENROLLED, date_subscribed="2022-12-22 13:56:05.430523")


