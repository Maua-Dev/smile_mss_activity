import json

import pytest

from src.modules.update_activity.app.update_activity_presenter import lambda_handler


class Test_UpdateActivityPresenter:

    def test_update_activity_presenter(self):
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
                'query_params': "value1"
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
            "body": '{"code": "ECM2345", "new_title": "Clean Architecture code review!", "new_description": "Reviewing IMT student\'s codes", "new_activity_type": "LECTURES", "new_is_extensive": false, "new_delivery_model": "IN_PERSON", "new_start_date": 1669141012, "new_duration": 90, "new_link": null, "new_place": "H331", "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"], "new_speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "new_total_slots": 100, "new_accepting_new_enrollments": true, "new_stop_accepting_new_enrollments_before": 1666451811}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 200
        assert json.loads(response["body"])['message'] == 'the activity was updated'

    def test_update_activity_presenter_no_items_found(self):
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
                'query_params': "value1"
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
            "body": '{"code": "ECM23451", "new_title": "Clean Architecture code review!", "new_description": "Reviewing IMT student\'s codes", "new_activity_type": "LECTURES", "new_is_extensive": false, "new_delivery_model": "IN_PERSON", "new_start_date": 1669141012, "new_duration": 90, "new_link": null, "new_place": "H331", "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"], "new_speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "new_total_slots": 100, "new_accepting_new_enrollments": true, "new_stop_accepting_new_enrollments_before": 1666451811}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 404
        assert json.loads(response["body"]) == "No items found for Activity"

    def test_update_activity_presenter_entity_error_code_invalid(self):
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
                'query_params': "value1"
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
            "body": '{"code": 2345, "new_title": "Clean Architecture code review!", "new_description": "Reviewing IMT student\'s codes", "new_activity_type": "LECTURES", "new_is_extensive": false, "new_delivery_model": "IN_PERSON", "new_start_date": 1669141012, "new_duration": 90, "new_link": null, "new_place": "H331", "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"], "new_speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "new_total_slots": 100, "new_accepting_new_enrollments": true, "new_stop_accepting_new_enrollments_before": 1666451811}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field code is not valid"

    def test_update_activity_presenter_missing_parameter_code(self):
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
                'query_params': "value1"
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
            "body": '{"new_title": "Clean Architecture code review!", "new_description": "Reviewing IMT student\'s codes", "new_activity_type": "LECTURES", "new_is_extensive": false, "new_delivery_model": "IN_PERSON", "new_start_date": 1669141012, "new_duration": 90, "new_link": null, "new_place": "H331", "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"], "new_speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "new_total_slots": 100, "new_accepting_new_enrollments": true, "new_stop_accepting_new_enrollments_before": 1666451811}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 400
        assert json.loads(response["body"]) == "Field code is missing"

    def test_update_activity_presenter_forbidden(self):
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
                'query_params': "value1"
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
            "body": '{"code": "ECM2345", "new_title": "Clean Architecture code review!", "new_description": "Reviewing IMT student\'s codes", "new_activity_type": "LECTURES", "new_is_extensive": false, "new_delivery_model": "IN_PERSON", "new_start_date": 1669141012, "new_duration": 90, "new_link": null, "new_place": "H331", "new_responsible_professors": ["62cafdd4-a110-11ed-a8fc-0242ac120002", "03555624-a110-11ed-a8fc-0242ac120002"], "new_speakers": [{"name": "Robert Cecil Martin", "bio": "Author of Clean Architecture: A Craftsman\'s Guide to Software Structure and Design", "company": "Clean Architecture Company"}], "new_total_slots": 100, "new_accepting_new_enrollments": true, "new_stop_accepting_new_enrollments_before": 1666451811}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }

        response = lambda_handler(event, None)
        assert response["statusCode"] == 403
        assert json.loads(response["body"]) == "That action is forbidden for this update_activity, only admins can update activities"
