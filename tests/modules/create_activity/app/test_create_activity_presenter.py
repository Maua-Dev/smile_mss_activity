import json
from src.modules.create_activity.app.create_activity_presenter import lambda_handler

import pytest
class Test_CreateActivityPresenter:

    def test_create_activity(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims":
                        {
                            "sub": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
                            "name": "João Vilas",
                            "custom:role": "ADMIN",
                        }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": '{"code": "ZYX321", "title": "Clean Architecture code review!", "description": "Reviewing IMT student\'s codes", "activity_type": "LECTURES", "is_extensive": false, "delivery_model": "IN_PERSON", "start_date": 1671246000000, "duration": 90, "link": null, "place": "H331", "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"], "speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "total_slots": 100, "accepting_new_enrollments": true, "stop_accepting_new_enrollments_before": 1671246000030}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 201
        assert json.loads(response["body"])["message"] == "the activity was created"

    def test_create_activity_presenter_no_items_found(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims":
                        {
                            "sub": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
                            "name": "João Vilas",
                            "custom:role": "ADMIN",
                        }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": '{"code": "CODIGO_NOVO", "title": "Clean Architecture code review!", "description": "Reviewing IMT student\'s codes", "activity_type": "LECTURES", "is_extensive": false, "delivery_model": "IN_PERSON", "start_date": 1669141012, "duration": 90, "link": null, "place": "H331", "responsible_professors": ["ZERO", "03555624-a110-11ed-a8fc-0242ac120002"], "speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "total_slots": 100, "accepting_new_enrollments": true, "stop_accepting_new_enrollments_before": 1666451811}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == 'Professores responsáveis não encontrados'


    def test_create_activity_presenter_missing_parameter(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims":
                        {
                            "sub": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
                            "name": "João Vilas",
                            "custom:role": "ADMIN",
                        }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": '{"title": "Clean Architecture code review!", "description": "Reviewing IMT student\'s codes", "activity_type": "LECTURES", "is_extensive": false, "delivery_model": "IN_PERSON", "start_date": 1669141012, "duration": 90, "link": null, "place": "H331", "responsible_professors": ["ZERO", "03555624-a110-11ed-a8fc-0242ac120002"], "speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "total_slots": 100, "accepting_new_enrollments": true, "stop_accepting_new_enrollments_before": 1666451811}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == 'Parâmetro ausente: code'

    def test_create_activity_presenter_entity_error(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims":
                        {
                            "sub": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
                            "name": "João Vilas",
                            "custom:role": "ADMIN",
                        }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": '{"code": 1, "title": "Clean Architecture code review!", "description": "Reviewing IMT student\'s codes", "activity_type": "LECTURES", "is_extensive": false, "delivery_model": "IN_PERSON", "start_date": 1669141012, "duration": 90, "link": null, "place": "H331", "responsible_professors": ["03555624-a110-11ed-a8fc-0242ac120002"], "speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "total_slots": 100, "accepting_new_enrollments": true, "stop_accepting_new_enrollments_before": 1666451811}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == 'Parâmetro inválido: code'


    def test_create_activity_presenter_duplicated_items(self):
            event = {
                "version": "2.0",
                "routeKey": "$default",
                "rawPath": "/my/path",
                "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
                "cookies": [
                    "cookie1",
                    "cookie2"
                ],
                "headers": {
                    "header1": "value1",
                    "header2": "value1,value2"
                },
                "queryStringParameters": {
                    "parameter1": "1"
                },
                "requestContext": {
                    "accountId": "123456789012",
                    "apiId": "<urlid>",
                    "authentication": None,
                    "authorizer": {
                        "claims":
                            {
                                "sub": "d61dbf66-a10f-11ed-a8fc-0242ac120002",
                                "name": "João Vilas",
                                "custom:role": "ADMIN",
                            }
                    },
                    "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                    "domainPrefix": "<url-id>",
                    "external_interfaces": {
                        "method": "POST",
                        "path": "/my/path",
                        "protocol": "HTTP/1.1",
                        "sourceIp": "123.123.123.123",
                        "userAgent": "agent"
                    },
                    "requestId": "id",
                    "routeKey": "$default",
                    "stage": "$default",
                    "time": "12/Mar/2020:19:03:58 +0000",
                    "timeEpoch": 1583348638390
                },
                "body": '{"code": "ECM2345", "title": "Clean Architecture code review!", "description": "Reviewing IMT student\'s codes", "activity_type": "LECTURES", "is_extensive": false, "delivery_model": "IN_PERSON", "start_date": 1669141012, "duration": 90, "link": null, "place": "H331", "responsible_professors": ["ZERO", "03555624-a110-11ed-a8fc-0242ac120002"], "speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "total_slots": 100, "accepting_new_enrollments": true, "stop_accepting_new_enrollments_before": 1666451811}',
                "pathParameters": None,
                "isBase64Encoded": None,
                "stageVariables": None
            }

            response = lambda_handler(event, None)

            assert response["statusCode"] == 400
            assert json.loads(response["body"]) == 'Já existe uma atividade com esse código'

    def test_create_activity_presenter_forbidden_not_admin(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                    "claims":
                        {
                            "sub": "0355535e-a110-11ed-a8fc-0242ac120002",
                            "name": "Bruno Soller",
                            "custom:role": "STUDENT",
                        }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": '{"code": "ZYX321", "title": "Clean Architecture code review!", "description": "Reviewing IMT student\'s codes", "activity_type": "LECTURES", "is_extensive": false, "delivery_model": "IN_PERSON", "start_date": 1669141012, "duration": 90, "link": null, "place": "H331", "responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"], "speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "total_slots": 100, "accepting_new_enrollments": true, "stop_accepting_new_enrollments_before": 1666451811}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)

        assert response["statusCode"] == 403
        assert json.loads(response["body"]) == "Apenas administradores podem criar atividades"
