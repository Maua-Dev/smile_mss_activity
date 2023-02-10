import json
from src.modules.delete_attendance_confirmation.app.delete_attendance_confirmation_presenter import lambda_handler

class Test_DeleteAttendanceConfirmationPresenter:
       def test_delete_attendance_confirmation_presenter(self):
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
                            "parameter1": "value1",
                     },
                     "requestContext": {
                            "accountId": "123456789012",
                            "apiId": "<urlid>",
                            "authentication": None,
                            "authorizer": {
                            "claims":
                                   {
                                          "sub": "03555624-a110-11ed-a8fc-0242ac120002",
                                          "cognito:username": "Caio Toledo",
                                          "custom:role": "PROFESSOR",
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
                     "body": '{"code": "ULTIMA"}',
                     "pathParameters": None,
                     "isBase64Encoded": None,
                     "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 200
              assert json.loads(response["body"])['message'] == "The confirmation code for the activity was deleted"

       def test_delete_attendance_confirmation_presenter_missing_code(self):
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
                            "parameter1": "value1",
                     },
                     "requestContext": {
                            "accountId": "123456789012",
                            "apiId": "<urlid>",
                            "authentication": None,
                            "authorizer": {
                            "claims":
                                   {
                                          "sub": "03555624-a110-11ed-a8fc-0242ac120002",
                                          "cognito:username": "Caio Toledo",
                                          "custom:role": "PROFESSOR",
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
                     "body": '{}',
                     "pathParameters": None,
                     "isBase64Encoded": None,
                     "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 400
              assert json.loads(response["body"]) == "Field code is missing"

       def test_delete_attendance_confirmation_presenter_missing_requester_user(self):
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
                            "parameter1": "value1",
                     },
                     "requestContext": {
                            "accountId": "123456789012",
                            "apiId": "<urlid>",
                            "authentication": None,
                            "authorizer": {

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
                     "body": '{"code": "ULTIMA"}',
                     "pathParameters": None,
                     "isBase64Encoded": None,
                     "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 400
              assert json.loads(response["body"]) == "Field requester_user is missing"

       def test_delete_attendance_confirmation_presenter_invalid_activity_code(self):
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
                            "parameter1": "value1",
                     },
                     "requestContext": {
                            "accountId": "123456789012",
                            "apiId": "<urlid>",
                            "authentication": None,
                            "authorizer": {
                            "claims":
                                   {
                                          "sub": "03555624-a110-11ed-a8fc-0242ac120002",
                                          "cognito:username": "Caio Toledo",
                                          "custom:role": "PROFESSOR",
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
                     "body": '{"code": 1}',
                     "pathParameters": None,
                     "isBase64Encoded": None,
                     "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 400
              assert json.loads(response["body"]) == "Field activity_code is not valid"

       def test_delete_attendance_confirmation_presenter_activity_not_found(self):
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
                            "parameter1": "value1",
                     },
                     "requestContext": {
                            "accountId": "123456789012",
                            "apiId": "<urlid>",
                            "authentication": None,
                            "authorizer": {
                            "claims":
                                   {
                                          "sub": "03555624-a110-11ed-a8fc-0242ac120002",
                                          "cognito:username": "Caio Toledo",
                                          "custom:role": "PROFESSOR",
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
                     "body": '{"code": "QUALQUER CODIGO"}',
                     "pathParameters": None,
                     "isBase64Encoded": None,
                     "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 404
              assert json.loads(response["body"]) == "No items found for activity"

       def test_delete_attendance_confirmation_presenter_role_not_professor(self):
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
                            "parameter1": "value1",
                     },
                     "requestContext": {
                            "accountId": "123456789012",
                            "apiId": "<urlid>",
                            "authentication": None,
                            "authorizer": {
                            "claims":
                                   {
                                          "sub": "0355535e-a110-11ed-a8fc-0242ac120002",
                                          "cognito:username": "Bruno Soller",
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
                     "body": '{"code": "555666"}',
                     "pathParameters": None,
                     "isBase64Encoded": None,
                     "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 403
              assert json.loads(response["body"]) == "That action is forbidden for this user, not professor"

       def test_delete_attendance_confirmation_presenter_activity_dont_have_confirmation_code(self):
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
                            "parameter1": "value1",
                     },
                     "requestContext": {
                            "accountId": "123456789012",
                            "apiId": "<urlid>",
                            "authentication": None,
                            "authorizer": {
                            "claims":
                                   {
                                          "sub": "03555624-a110-11ed-a8fc-0242ac120002",
                                          "cognito:username": "Caio Toledo",
                                          "custom:role": "PROFESSOR",
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
                     "body": '{"code": "ECM2345"}',
                     "pathParameters": None,
                     "isBase64Encoded": None,
                     "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 403
              assert json.loads(response["body"]) == "That action is forbidden for this confirmation_code, do not exists"

       def test_delete_attendance_confirmation_presenter_not_responsible_professor(self):
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
                            "parameter1": "value1",
                     },
                     "requestContext": {
                            "accountId": "123456789012",
                            "apiId": "<urlid>",
                            "authentication": None,
                            "authorizer": {
                            "claims":
                                   {
                                          "sub": "6bb122d4-a110-11ed-a8fc-0242ac120002",
                                          "cognito:username": "Patricia Santos",
                                          "custom:role": "PROFESSOR",
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
                     "body": '{"code": "CODIGO"}',
                     "pathParameters": None,
                     "isBase64Encoded": None,
                     "stageVariables": None
              }


              response = lambda_handler(event, None)
              assert response["statusCode"] == 403
              assert json.loads(response["body"]) == "That action is forbidden for this confirmation_code, do not exists"