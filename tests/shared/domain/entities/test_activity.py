import datetime

import pytest

from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.domain.entities.activity import Activity
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Activity:

    def test_activity(self):
        activity = Activity(
            code="1234",
            title="Palestra Microsoft",
            description="Palestra informacional de como usar a Azure",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.IN_PERSON,
            start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
            duration=120,
            encharged_professors=[
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
            stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
        )

        assert type(activity) == Activity
        assert activity.code == "1234"

    def test_activity_invalid_code_none(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code=None,
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_code_int(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code=1234,
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_title(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title=1234,
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )


    def test_activity_invalid_description(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description=1234,
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_activity_type(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type="LECTURES",
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_is_extensive(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive="True",
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_delivery_model(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model="IN_PERSON",
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_start_date(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date="2022-12-22 13:56:05.430523",
                duration=120,
                encharged_professors=[
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
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_duration(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration="DUAS HORAS",
                encharged_professors=[
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
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_encharged_professors(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=None,
                speakers=[
                    Speaker(
                        name="Marcos Tales",
                        bio="Salve",
                        company="Microsoft"
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_enchard_professor_not_users(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
                    Speaker(
                        name="Marcos Tales",
                        bio="Salve",
                        company="Microsoft"
                    )],
                speakers=[
                    Speaker(
                        name="Marcos Tales",
                        bio="Salve",
                        company="Microsoft"
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )
    def test_activity_invalid_encharged_professors_not_professor(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.STUDENT,
                        user_id="123d"
                    )
                ],
                speakers=[
                    Speaker(
                        name="Marcos Tales",
                        bio="Salve",
                        company="Microsoft"
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_speakers(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="123d"
                    )
                ],
                speakers=None,
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )


    def test_activity_invalid_speakers_not_speaker(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="123d"
                    )
                ],
                speakers=[
                    User(
                        name="Marcos",
                        role=ROLE.STUDENT,
                        user_id="123d"
                    )
                ],
                total_slots=120,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_total_slots(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                total_slots=None,
                taken_slots=33,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_taken_slots(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                taken_slots=None,
                accepting_new_subscriptions=True,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_accepting_new_subscriptions(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                accepting_new_subscriptions=None,
                stop_accepting_new_subscriptions_before=datetime.datetime(2025, 12, 25, 13, 56, 5, 430523)
            )

    def test_activity_invalid_stop_accepting_new_subscriptions_before(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=datetime.datetime(2022, 12, 22, 13, 56, 5, 430523),
                duration=120,
                encharged_professors=[
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
                stop_accepting_new_subscriptions_before=None
            )
