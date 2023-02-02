from src.shared.domain.entities.activity import Activity
from src.shared.domain.entities.speaker import Speaker
from src.shared.domain.entities.user import User
from src.shared.domain.enums.activity_type_enum import ACTIVITY_TYPE
from src.shared.domain.enums.delivery_model_enum import DELIVERY_MODEL
from src.shared.domain.enums.role_enum import ROLE
from src.shared.infra.dto.activity_dynamo_dto import ActivityDynamoDTO


class Test_ActivityDynamoDTO:

    def test_from_entity(self):
        activity = Activity(
            code="ELET355",
            title="Atividade da ELET 355",
            description="Isso é uma atividade, sério.",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.HYBRID,
            start_date=1671661013000,
            duration=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"), User(name="Lucas Vitor", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"), Speaker(name="Lucas Vitor", bio="Daora", company="Microsoft")],
            total_slots=10,
            taken_slots=1,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None
        )

        activity_dynamo_dto = ActivityDynamoDTO.from_entity(activity)

        expected_activity_dynamo_dto = ActivityDynamoDTO(
            code="ELET355",
            title="Atividade da ELET 355",
            description="Isso é uma atividade, sério.",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.HYBRID,
            start_date=1671661013000,
            duration=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"), User(name="Lucas Vitor", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"), Speaker(name="Lucas Vitor", bio="Daora", company="Microsoft")],
            total_slots=10,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None
        )

        assert activity_dynamo_dto == expected_activity_dynamo_dto

    def test_to_dynamo(self):
        activity_dynamo_dto = ActivityDynamoDTO(
            code="ELET355",
            title="Atividade da ELET 355",
            description="Isso é uma atividade, sério.",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.HYBRID,
            start_date=1671661013000,
            duration=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"), User(name="Lucas Vitor", role=ROLE.PROFESSOR, user_id="5bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"), Speaker(name="Lucas Vitor", bio="Daora", company="Microsoft")],
            total_slots=10,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None
        )

        expected_dynamo = {
            "code": "ELET355",
            "title": "Atividade da ELET 355",
            "description": "Isso é uma atividade, sério.",
            "activity_type": "LECTURES",
            "is_extensive": True,
            "delivery_model": "HYBRID",
            "start_date": 1671661013000,
            "duration": 400,
            "link": "https://devmaua.com",
            "place": "H332",
            "responsible_professors": [
                {
                    "name": "Patricia Santos",
                    "role": "PROFESSOR",
                    "user_id": "6bb122d4-a110-11ed-a8fc-0242ac120002"
                },
                {
                    "name": "Lucas Vitor",
                    "role": "PROFESSOR",
                    "user_id": "5bb122d4-a110-11ed-a8fc-0242ac120002"
                }
            ],
            "speakers": [
                {
                    "name": "Lucas Soller",
                    "bio": "Daora",
                    "company": "Microsoft"
                },
                {
                    "name": "Lucas Vitor",
                    "bio": "Daora",
                    "company": "Microsoft"
                }
            ],
            "total_slots": 10,
            "accepting_new_enrollments": True,
            "stop_accepting_new_enrollments_before": None
        }

        assert expected_dynamo == activity_dynamo_dto.to_dynamo()

    def test_from_entity_to_dynamo(self):
        activity = Activity(
            code="ELET355",
            title="Atividade da ELET 355",
            description="Isso é uma atividade, sério.",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.HYBRID,
            start_date=1671661013000,
            duration=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"), User(name="Lucas Vitor", role=ROLE.PROFESSOR, user_id="5bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"), Speaker(name="Lucas Vitor", bio="Daora", company="Microsoft")],
            total_slots=10,
            taken_slots=1,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None
        )

        activity_dynamo_dto = ActivityDynamoDTO.from_entity(activity)

        expected_dynamo = {
            "code": "ELET355",
            "title": "Atividade da ELET 355",
            "description": "Isso é uma atividade, sério.",
            "activity_type": "LECTURES",
            "is_extensive": True,
            "delivery_model": "HYBRID",
            "start_date": 1671661013000,
            "duration": 400,
            "link": "https://devmaua.com",
            "place": "H332",
            "responsible_professors": [
                {
                    "name": "Patricia Santos",
                    "role": "PROFESSOR",
                    "user_id": "6bb122d4-a110-11ed-a8fc-0242ac120002"
                },
                {
                    "name": "Lucas Vitor",
                    "role": "PROFESSOR",
                    "user_id": "5bb122d4-a110-11ed-a8fc-0242ac120002"
                }
            ],
            "speakers": [
                {
                    "name": "Lucas Soller",
                    "bio": "Daora",
                    "company": "Microsoft"
                },
                {
                    "name": "Lucas Vitor",
                    "bio": "Daora",
                    "company": "Microsoft"
                }
            ],
            "total_slots": 10,
            "accepting_new_enrollments": True,
            "stop_accepting_new_enrollments_before": None
        }

        assert expected_dynamo == activity_dynamo_dto.to_dynamo()
