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
            end_date=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"),
                User(name="Lucas Vitor", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"),
                      Speaker(name="Lucas Vitor", bio="Daora", company="Microsoft")],
            total_slots=10,
            taken_slots=1,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None,
            confirmation_code="123456"
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
            end_date=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"),
                User(name="Lucas Vitor", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"),
                      Speaker(name="Lucas Vitor", bio="Daora", company="Microsoft")],
            total_slots=10,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None,
            confirmation_code="123456"
        )

        assert activity_dynamo_dto.code == expected_activity_dynamo_dto.code
        assert activity_dynamo_dto.title == expected_activity_dynamo_dto.title
        assert activity_dynamo_dto.description == expected_activity_dynamo_dto.description
        assert activity_dynamo_dto.activity_type == expected_activity_dynamo_dto.activity_type
        assert activity_dynamo_dto.is_extensive == expected_activity_dynamo_dto.is_extensive
        assert activity_dynamo_dto.delivery_model == expected_activity_dynamo_dto.delivery_model
        assert activity_dynamo_dto.start_date == expected_activity_dynamo_dto.start_date
        assert activity_dynamo_dto.end_date == expected_activity_dynamo_dto.end_date
        assert activity_dynamo_dto.link == expected_activity_dynamo_dto.link
        assert activity_dynamo_dto.place == expected_activity_dynamo_dto.place
        assert activity_dynamo_dto.responsible_professors == expected_activity_dynamo_dto.responsible_professors
        assert activity_dynamo_dto.speakers == expected_activity_dynamo_dto.speakers
        assert activity_dynamo_dto.total_slots == expected_activity_dynamo_dto.total_slots
        assert activity_dynamo_dto.accepting_new_enrollments == expected_activity_dynamo_dto.accepting_new_enrollments
        assert activity_dynamo_dto.stop_accepting_new_enrollments_before == expected_activity_dynamo_dto.stop_accepting_new_enrollments_before
        assert activity_dynamo_dto.confirmation_code == expected_activity_dynamo_dto.confirmation_code
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
            end_date=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"),
                User(name="Lucas Vitor", role=ROLE.PROFESSOR, user_id="5bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"),
                      Speaker(name="Lucas Vitor", bio="Daora", company="Microsoft")],
            total_slots=10,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None,
            confirmation_code="123456"
        )

        expected_dynamo = {
            "activity_code": "ELET355",
            "title": "Atividade da ELET 355",
            "description": "Isso é uma atividade, sério.",
            "activity_type": "LECTURES",
            "is_extensive": True,
            "delivery_model": "HYBRID",
            "start_date": 1671661013000,
            "end_date": 400,
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
            "confirmation_code": "123456",
            "entity": "activity"
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
            end_date=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002"),
                User(name="Lucas Vitor", role=ROLE.PROFESSOR, user_id="5bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft"),
                      Speaker(name="Lucas Vitor", bio="Daora", company="Microsoft")],
            total_slots=10,
            taken_slots=1,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None,
            confirmation_code=None
        )

        activity_dynamo_dto = ActivityDynamoDTO.from_entity(activity)

        expected_dynamo = {
            "activity_code": "ELET355",
            "title": "Atividade da ELET 355",
            "description": "Isso é uma atividade, sério.",
            "activity_type": "LECTURES",
            "is_extensive": True,
            "delivery_model": "HYBRID",
            "start_date": 1671661013000,
            "end_date": 400,
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
            "entity": "activity"
        }

        assert expected_dynamo == activity_dynamo_dto.to_dynamo()

    def test_from_entity_to_dynamo_2(self):
        activity = Activity(
            code="ECM2345",
            title="Atividade da ECM 2345",
            description="Isso é uma atividade",
            activity_type=ACTIVITY_TYPE.COURSES,
            is_extensive=False,
            delivery_model=DELIVERY_MODEL.IN_PERSON,
            start_date=1671747413000,
            end_date=120,
            link=None,
            place="H332",
            responsible_professors=[
                User(name="Caio Toledo", role=ROLE.PROFESSOR, user_id="03555624-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Vitor Briquez", bio="Incrível", company="Apple")],
            total_slots=4,
            taken_slots=4,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=1671743812000,
            confirmation_code=None
        )

        activity_dynamo_dto = ActivityDynamoDTO.from_entity(activity)

        expected_dynamo = {
            "activity_code": "ECM2345",
            "title": "Atividade da ECM 2345",
            "description": "Isso é uma atividade",
            "activity_type": "COURSES",
            "is_extensive": False,
            "delivery_model": "IN_PERSON",
            "start_date": 1671747413000,
            "end_date": 120,
            "place": "H332",
            "responsible_professors": [
                {
                    "name": "Caio Toledo",
                    "role": "PROFESSOR",
                    "user_id": "03555624-a110-11ed-a8fc-0242ac120002"
                }
            ],
            "speakers": [
                {
                    "name": "Vitor Briquez",
                    "bio": "Incrível",
                    "company": "Apple"
                }
            ],
            "total_slots": 4,
            "accepting_new_enrollments": True,
            "stop_accepting_new_enrollments_before": 1671743812000,
            "entity": "activity"
        }

        assert expected_dynamo == activity_dynamo_dto.to_dynamo()

    def test_from_dynamo(self):
        dynamo_data = {
            'Item': {
                'activity_code': 'ELET355',
                'link': 'https://devmaua.com',
                'total_slots': '10',
                'description': 'Isso é uma atividade, sério.',
                'responsible_professors': [
                    {
                        'name': 'Patricia Santos',
                        'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002',
                        'role': 'PROFESSOR'
                    }
                ],
                'accepting_new_enrollments': True,
                'delivery_model': 'HYBRID',
                'title': 'Atividade da ELET 355',
                'is_extensive': True,
                'end_date': '400',
                'activity_type': 'LECTURES',
                'speakers': [
                    {
                        'name': 'Lucas Soller',
                        'bio': 'Daora',
                        'company': 'Microsoft'
                    }
                ],
                'SK': 'activity#ELET355',
                'place': 'H332',
                'PK': 'ELET355',
                'stop_accepting_new_enrollments_before': None,
                'start_date': '1671661013000',
                "confirmation_code": "123456",
                "entity": "activity"
            },
            'ResponseMetadata': {
                'RequestId': 'a955a01d-28d9-4da3-964e-801672d847df',
                'HTTPStatusCode': 200,
                'HTTPHeaders': {
                    'date': 'Thu, 02 Feb 2023 19:11:33 GMT',
                    'content-type': 'application/x-amz-json-1.0',
                    'x-amz-crc32': '4255886215',
                    'x-amzn-requestid': 'a955a01d-28d9-4da3-964e-801672d847df',
                    'content-length': '759',
                    'server': 'Jetty(9.4.48.v20220622)'
                },
                'RetryAttempts': 0
            }
        }

        dynamo_data['Item']['taken_slots'] = 1

        activity_dto = ActivityDynamoDTO.from_dynamo(dynamo_data['Item'])

        expected_activity = ActivityDynamoDTO(
            code="ELET355",
            title="Atividade da ELET 355",
            description="Isso é uma atividade, sério.",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.HYBRID,
            start_date=1671661013000,
            end_date=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
            total_slots=10,
            taken_slots=1,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None,
            confirmation_code="123456"
        )

        assert expected_activity == activity_dto

    def test_to_entity(self):
        activity_dynamo_dto = ActivityDynamoDTO(
            code="ELET355",
            title="Atividade da ELET 355",
            description="Isso é uma atividade, sério.",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.HYBRID,
            start_date=1671661013000,
            end_date=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
            total_slots=10,
            taken_slots=1,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None,
            confirmation_code="123456"
        )

        expected_activity = Activity(
            code="ELET355",
            title="Atividade da ELET 355",
            description="Isso é uma atividade, sério.",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.HYBRID,
            start_date=1671661013000,
            end_date=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
            total_slots=10,
            taken_slots=1,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None,
            confirmation_code="123456"
        )

        assert expected_activity == activity_dynamo_dto.to_entity()

    def test_from_dynamo_to_entity(self):
        dynamo_data = {
            'Item': {
                'activity_code': 'ELET355',
                'link': 'https://devmaua.com',
                'total_slots': '10',
                'description': 'Isso é uma atividade, sério.',
                'responsible_professors': [
                    {
                        'name': 'Patricia Santos',
                        'user_id': '6bb122d4-a110-11ed-a8fc-0242ac120002',
                        'role': 'PROFESSOR'
                    }
                ],
                'accepting_new_enrollments': True,
                'delivery_model': 'HYBRID',
                'title': 'Atividade da ELET 355',
                'is_extensive': True,
                'end_date': '400',
                'activity_type': 'LECTURES',
                'speakers': [
                    {
                        'name': 'Lucas Soller',
                        'bio': 'Daora',
                        'company': 'Microsoft'
                    }
                ],
                'SK': 'activity#ELET355',
                'place': 'H332',
                'PK': 'ELET355',
                'stop_accepting_new_enrollments_before': None,
                'start_date': '1671661013000',
                "confirmation_code": "123456",
                "entity": "activity"
            },
            'ResponseMetadata': {
                'RequestId': 'a955a01d-28d9-4da3-964e-801672d847df',
                'HTTPStatusCode': 200,
                'HTTPHeaders': {
                    'date': 'Thu, 02 Feb 2023 19:11:33 GMT',
                    'content-type': 'application/x-amz-json-1.0',
                    'x-amz-crc32': '4255886215',
                    'x-amzn-requestid': 'a955a01d-28d9-4da3-964e-801672d847df',
                    'content-length': '759',
                    'server': 'Jetty(9.4.48.v20220622)'
                },
                'RetryAttempts': 0
            }
        }

        dynamo_data['Item']['taken_slots'] = 1

        activity_dto = ActivityDynamoDTO.from_dynamo(dynamo_data['Item'])

        expected_activity = Activity(
            code="ELET355",
            title="Atividade da ELET 355",
            description="Isso é uma atividade, sério.",
            activity_type=ACTIVITY_TYPE.LECTURES,
            is_extensive=True,
            delivery_model=DELIVERY_MODEL.HYBRID,
            start_date=1671661013000,
            end_date=400,
            link="https://devmaua.com",
            place="H332",
            responsible_professors=[
                User(name="Patricia Santos", role=ROLE.PROFESSOR, user_id="6bb122d4-a110-11ed-a8fc-0242ac120002")],
            speakers=[Speaker(name="Lucas Soller", bio="Daora", company="Microsoft")],
            total_slots=10,
            taken_slots=1,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=None,
            confirmation_code="123456"
        )

        assert expected_activity == activity_dto.to_entity()

    def test_from_dynamo_to_entity_2(self):
        dynamo_data = {
            'Item': {
                'activity_code': 'ULTIMA',
                'total_slots':'3',
                'description': 'Atividade pra acabar',
                'responsible_professors': [
                    {
                        'name': 'Caio Toledo',
                        'user_id': '03555624-a110-11ed-a8fc-0242ac120002',
                        'role': 'PROFESSOR'
                    }
                ],
                'accepting_new_enrollments': True,
                'delivery_model': 'IN_PERSON',
                'title': 'Última atividade',
                'is_extensive': False,
                'end_date':'45',
                'activity_type': 'SPORTS_ACTIVITY',
                'speakers': [
                    {
                        'name': 'Daniel Romanato',
                        'bio': 'Buscando descobrir o mundo',
                        'company': 'Samsung'
                    }
                ],
                'SK': 'activity#ULTIMA',
                'place': 'H332',
                'PK': 'ULTIMA',
                'stop_accepting_new_enrollments_before':'1671733012000',
                'start_date':'1671733013000',
                "entity": "activity"
            },
            'ResponseMetadata': {
                'RequestId': '167ee89a-6bde-44db-9ea7-470bf136e60e',
                'HTTPStatusCode': 200,
                'HTTPHeaders': {
                    'date': 'Thu, 02 Feb 2023 19:55:15 GMT',
                    'content-type': 'application/x-amz-json-1.0',
                    'x-amz-crc32': '1982622271',
                    'x-amzn-requestid': '167ee89a-6bde-44db-9ea7-470bf136e60e',
                    'content-length': '742',
                    'server': 'Jetty(9.4.48.v20220622)'
                },
                'RetryAttempts': 0
            }
        }

        dynamo_data['Item']['taken_slots'] = 3

        activity_dto = ActivityDynamoDTO.from_dynamo(dynamo_data['Item'])

        expected_activity = Activity(
            code="ULTIMA",
            title="Última atividade",
            description="Atividade pra acabar",
            activity_type=ACTIVITY_TYPE.SPORTS_ACTIVITY,
            is_extensive=False,
            delivery_model=DELIVERY_MODEL.IN_PERSON,
            start_date=1671733013000,
            end_date=45,
            link=None,
            place="H332",
            responsible_professors=[
                User(
                    name="Caio Toledo",
                    role=ROLE.PROFESSOR,
                    user_id="03555624-a110-11ed-a8fc-0242ac120002"
                )
            ],
            speakers=[
                Speaker(
                    name="Daniel Romanato",
                    bio="Buscando descobrir o mundo",
                    company="Samsung"
                )
            ],
            total_slots=3,
            taken_slots=3,
            accepting_new_enrollments=True,
            stop_accepting_new_enrollments_before=1671733012000,
            confirmation_code=None
        )

        assert expected_activity == activity_dto.to_entity()


