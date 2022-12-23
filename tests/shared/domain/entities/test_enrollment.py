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
        enrollment = Enrollment(
            activity=Activity(
            code="1234",
            title="Palestra Microsoft",
            description="Palestra informacional de como usar a Azure",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.IN_PERSON,
            start_date=datetime.datetime(2022, 12, 23, 13, 56, 5, 430523),
            duration=120,
            responsible_professors=[
                User(
                    name="Marcos",
                    role=ROLE.PROFESSOR,
                    user_id="123d"
                )
            ],
            speakers=[
                Speaker(
                    name="Marcos Tales",
                    bio="Salve",
                    company="Microsoft"
                )
            ],
            total_slots=120,
            taken_slots=33,
            accepting_new_subscriptions=True,
            stop_accepting_new_subscriptions_before=datetime.datetime(2022, 12, 21, 13, 56, 5, 430523)
        ),
            user=User(
                name="Marcos",
                role=ROLE.PROFESSOR,
                user_id="123d"
            ),
            state=ENROLLMENT_STATE.ENROLLED,
            date_subscribed=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523)
        )

        assert type(enrollment) == Enrollment
        assert enrollment.activity.code == "1234"
        assert enrollment.user.name == "Marcos"
        assert enrollment.state == ENROLLMENT_STATE.ENROLLED
        assert enrollment.date_subscribed == datetime.datetime(2022, 12, 22, 13, 56, 5, 430523)


    def test_enrollment_with_invalid_activity(self):
        with pytest.raises(EntityError):
            enrollment = Enrollment(
                activity="1234",
                user=User(
                    name="Marcos",
                    role=ROLE.PROFESSOR,
                    user_id="123d"
                ),
                state=ENROLLMENT_STATE.ENROLLED,
                date_subscribed=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523)
            )

    def test_enrollment_with_invalid_user(self):
        with pytest.raises(EntityError):
            enrollment = Enrollment(
                activity=Activity(
                    code="1234",
                    title="Palestra Microsoft",
                    description="Palestra informacional de como usar a Azure",
                    activity_type=ACTIVITY_TYPE.LECTURES,
                    is_extensive=True,
                    delivery_model=DELIVERY_MODEL.IN_PERSON,
                    start_date=datetime.datetime(2022, 12, 23, 13, 56, 5, 430523),
                    duration=120,
                    responsible_professors=[
                        User(
                            name="Marcos",
                            role=ROLE.PROFESSOR,
                            user_id="123d"
                        )
                    ],
                    speakers=[
                        Speaker(
                            name="Marcos Tales",
                            bio="Salve",
                            company="Microsoft"
                        )
                    ],
                    total_slots=120,
                    taken_slots=33,
                    accepting_new_subscriptions=True,
                    stop_accepting_new_subscriptions_before=datetime.datetime(22, 12, 21, 13, 56, 5, 430523)
                ),
                user="Marcos",
                state=ENROLLMENT_STATE.ENROLLED,
                date_subscribed=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523)
            )

    def test_enrollment_with_invalid_state(self):
        with pytest.raises(EntityError):
            enrollment = Enrollment(
                activity=Activity(
                    code="1234",
                    title="Palestra Microsoft",
                    description="Palestra informacional de como usar a Azure",
                    activity_type=ACTIVITY_TYPE.LECTURES,
                    is_extensive=True,
                    delivery_model=DELIVERY_MODEL.IN_PERSON,
                    start_date=datetime.datetime(2022, 12, 23, 13, 56, 5, 430523),
                    duration=120,
                    responsible_professors=[
                        User(
                            name="Marcos",
                            role=ROLE.PROFESSOR,
                            user_id="123d"
                        )
                    ],
                    speakers=[
                        Speaker(
                            name="Marcos Tales",
                            bio="Salve",
                            company="Microsoft"
                        )
                    ],
                    total_slots=120,
                    taken_slots=33,
                    accepting_new_subscriptions=True,
                    stop_accepting_new_subscriptions_before=datetime.datetime(22, 12, 21, 13, 56, 5, 430523)
                ),
                user=User(
                    name="Marcos",
                    role=ROLE.PROFESSOR,
                    user_id="123d"
                ),
                state="ENROLLED",
                date_subscribed=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523)
            )

    def test_enrollment_with_invalid_date_subscribed(self):
        with pytest.raises(EntityError):
            enrollment = Enrollment(
                activity=Activity(
                    code="1234",
                    title="Palestra Microsoft",
                    description="Palestra informacional de como usar a Azure",
                    activity_type=ACTIVITY_TYPE.LECTURES,
                    is_extensive=True,
                    delivery_model=DELIVERY_MODEL.IN_PERSON,
                    start_date=datetime.datetime(2022, 12, 23, 13, 56, 5, 430523),
                    duration=120,
                    responsible_professors=[
                        User(
                            name="Marcos",
                            role=ROLE.PROFESSOR,
                            user_id="123d"
                        )
                    ],
                    speakers=[
                        Speaker(
                            name="Marcos Tales",
                            bio="Salve",
                            company="Microsoft"
                        )
                    ],
                    total_slots=120,
                    taken_slots=33,
                    accepting_new_subscriptions=True,
                    stop_accepting_new_subscriptions_before=datetime.datetime(22, 12, 21, 13, 56, 5, 430523)
                ),
                user=User(
                    name="Marcos",
                    role=ROLE.PROFESSOR,
                    user_id="123d"
                ),
                state=ENROLLMENT_STATE.ENROLLED,
                date_subscribed="2022-12-22 13:56:05.430523"
            )


