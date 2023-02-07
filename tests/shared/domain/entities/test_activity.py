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
            start_date=1671728165000,
            duration=120,
            link="https://devmaua.com",
            place="H333",
            responsible_professors=[
                User(
                    name="Marcos",
                    role=ROLE.PROFESSOR,
                    user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=1671724560000,
            confirmation_code="123456"
        )

        assert type(activity) == Activity
        assert activity.code == "1234"
        assert activity.title == "Palestra Microsoft"
        assert activity.description == "Palestra informacional de como usar a Azure"
        assert activity.activity_type == ACTIVITY_TYPE.LECTURES
        assert activity.is_extensive == True
        assert activity.delivery_model == DELIVERY_MODEL.IN_PERSON
        assert activity.start_date == 1671728165000
        assert activity.duration == 120
        assert activity.responsible_professors[0].name == "Marcos"
        assert activity.speakers[0].name == "Marcos Tales"
        assert activity.total_slots == 120
        assert activity.taken_slots == 33
        assert activity.accepting_new_enrollments == True
        assert activity.stop_accepting_new_enrollments_before == 1671724560000

    def test_activity_link_none(self):
        activity = Activity(
            code="1234",
            title="Palestra Microsoft",
            description="Palestra informacional de como usar a Azure",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.IN_PERSON,
            start_date=1671728165000,
            duration=120,
            link=None,
            place="H333",
            responsible_professors=[
                User(
                    name="Marcos",
                    role=ROLE.PROFESSOR,
                    user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=1671724565000,
            confirmation_code=None
        )

        assert type(activity) == Activity
        assert activity.code == "1234"
        assert activity.title == "Palestra Microsoft"
        assert activity.description == "Palestra informacional de como usar a Azure"
        assert activity.activity_type == ACTIVITY_TYPE.LECTURES
        assert activity.is_extensive == True
        assert activity.delivery_model == DELIVERY_MODEL.IN_PERSON
        assert activity.start_date == 1671728165000
        assert activity.duration == 120
        assert activity.responsible_professors[0].name == "Marcos"
        assert activity.speakers[0].name == "Marcos Tales"
        assert activity.total_slots == 120
        assert activity.taken_slots == 33
        assert activity.accepting_new_enrollments == True
        assert activity.stop_accepting_new_enrollments_before == 1671724565000

    def test_activity_none_place(self):
        activity = Activity(
            code="1234",
            title="Palestra Microsoft",
            description="Palestra informacional de como usar a Azure",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.IN_PERSON,
            start_date=1671728165000,
            duration=120,
            link="https://devmaua.com",
            place=None,
            responsible_professors=[
                User(
                    name="Marcos",
                    role=ROLE.PROFESSOR,
                    user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=1671724565000,
            confirmation_code=None
        )

        assert type(activity) == Activity
        assert activity.code == "1234"
        assert activity.title == "Palestra Microsoft"
        assert activity.description == "Palestra informacional de como usar a Azure"
        assert activity.activity_type == ACTIVITY_TYPE.LECTURES
        assert activity.is_extensive == True
        assert activity.delivery_model == DELIVERY_MODEL.IN_PERSON
        assert activity.start_date == 1671728165000
        assert activity.duration == 120
        assert activity.responsible_professors[0].name == "Marcos"
        assert activity.speakers[0].name == "Marcos Tales"
        assert activity.total_slots == 120
        assert activity.taken_slots == 33
        assert activity.accepting_new_enrollments == True
        assert activity.stop_accepting_new_enrollments_before == 1671724565000


    def test_activity_none_link_place(self):
        with pytest.raises(EntityError):
            activity = Activity(
            code="1234",
            title="Palestra Microsoft",
            description="Palestra informacional de como usar a Azure",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.IN_PERSON,
            start_date=1671728165000,
            duration=120,
            link=None,
            place=None,
            responsible_professors=[
                User(
                    name="Marcos",
                    role=ROLE.PROFESSOR,
                    user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
        )

    def test_activity_invalid_code_none(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code=None,
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                    start_date=1671728165000,
                    duration=120,
                    link="https://devmaua.com",
                    place="H333",
                    responsible_professors=[
                        User(
                            name="Marcos",
                            role=ROLE.PROFESSOR,
                            user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                    accepting_new_enrollments=True,
                    stop_accepting_new_enrollments_before=1671724565000,
                    confirmation_code=None
                )

    def test_activity_invalid_title_none(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title=None,
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration="DUAS HORAS",
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
            )

    def test_activity_invalid_place(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place=123,
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
            )

    def test_activity_invalid_link(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link=123,
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
            )

    def test_activity_invalid_responsible_professors(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=None,
                speakers=[
                    Speaker(
                        name="Marcos Tales",
                        bio="Salve",
                        company="Microsoft"
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
            )

    def test_activity_invalid_responsible_professors_not_users(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    Speaker(
                        name="Marcos Tales",
                        bio="Salve",
                        company="Microsoft"
                    ),
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
                    )],
                speakers=[
                    Speaker(
                        name="Marcos Tales",
                        bio="Salve",
                        company="Microsoft"
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
            )
    def test_activity_invalid_responsible_professors_not_professor(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.STUDENT,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
                    ),
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
                    )],
                speakers=[
                    Speaker(
                        name="Marcos Tales",
                        bio="Salve",
                        company="Microsoft"
                    )],
                total_slots=120,
                taken_slots=33,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
                    ),
                    Speaker(
                        name="Marcos Tales",
                        bio="Salve",
                        company="Microsoft"
                    )
                ],
                speakers=None,
                total_slots=120,
                taken_slots=33,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
                    )
                ],
                speakers=[
                    User(
                        name="Marcos",
                        role=ROLE.STUDENT,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
                    )
                ],
                total_slots=120,
                taken_slots=33,
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
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
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
            )

    def test_activity_invalid_accepting_new_enrollments(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=None,
                stop_accepting_new_enrollments_before=1671724565000,
                confirmation_code=None
            )

    def test_activity_invalid_stop_accepting_new_enrollments_before_none(self):
        activity = Activity(
            code="1234",
            title="Palestra Microsoft",
            description="Palestra informacional de como usar a Azure",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.IN_PERSON,
            start_date=1671728165000,
            duration=120,
            link="https://devmaua.com",
            place="H333",
            responsible_professors=[
                User(
                    name="Marcos",
                    role=ROLE.PROFESSOR,
                    user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None,
            confirmation_code=None
        )

        assert activity.stop_accepting_new_enrollments_before is None

    def test_activity_invalid_stop_accepting_new_enrollments_before_int(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before="2",
                confirmation_code=None
            )
    def test_activity_invalid_stop_accepting_new_enrollments_before_after_start(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671728165001,
                confirmation_code=None
            )
    def test_activity_invalid_confirmation_code(self):
        with pytest.raises(EntityError):
            activity = Activity(
                code="1234",
                title="Palestra Microsoft",
                description="Palestra informacional de como usar a Azure",
                activity_type=ACTIVITY_TYPE.LECTURES,
                is_extensive=True,
                delivery_model=DELIVERY_MODEL.IN_PERSON,
                start_date=1671728165000,
                duration=120,
                link="https://devmaua.com",
                place="H333",
                responsible_professors=[
                    User(
                        name="Marcos",
                        role=ROLE.PROFESSOR,
                        user_id="7f52e72c-a111-11ed-a8fc-0242ac120002"
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
                accepting_new_enrollments=True,
                stop_accepting_new_enrollments_before=1671728164000,
                confirmation_code=2
            )
