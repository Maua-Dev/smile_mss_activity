import json

from src.modules.enroll_activity.app.enroll_activity_presenter import lambda_handler



class Test_EnrollActivityPresenter:
       def test_enroll_activity_presenter(self):
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
                     "iam": {
                            "accessKey": "AKIA...",
                            "accountId": "111122223333",
                            "callerId": "AIDA...",
                            "cognitoIdentity": None,
                            "principalOrgId": None,
                            "userArn": "arn:aws:iam::111122223333:user/example-user",
                            "userId": "AIDA..."
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
              "body": '{"user_id": "80fb", "code": "COD1468"}',
              "pathParameters": None,
              "isBase64Encoded": None,
              "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 200
              assert json.loads(response["body"])['message'] == 'the enrollment has been done'

       def test_enroll_activity_presenter_400_user_id_missing(self):
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
                            "iam": {
                                   "accessKey": "AKIA...",
                                   "accountId": "111122223333",
                                   "callerId": "AIDA...",
                                   "cognitoIdentity": None,
                                   "principalOrgId": None,
                                   "userArn": "arn:aws:iam::111122223333:user/example-user",
                                   "userId": "AIDA..."
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
                     "body": '{"code": "ELET355"}',
                     "pathParameters": None,
                     "isBase64Encoded": None,
                     "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 400
              assert json.loads(response["body"]) == "Field user_id is missing"

       def test_enroll_activity_presenter_400_code_missing(self):
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
                     "iam": {
                            "accessKey": "AKIA...",
                            "accountId": "111122223333",
                            "callerId": "AIDA...",
                            "cognitoIdentity": None,
                            "principalOrgId": None,
                            "userArn": "arn:aws:iam::111122223333:user/example-user",
                            "userId": "AIDA..."
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
              "body": '{"user_id": "b16f"}',
              "pathParameters": None,
              "isBase64Encoded": None,
              "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 400
              assert json.loads(response["body"]) == "Field code is missing"
       def test_enroll_activity_presenter_400_user_id_invalid(self):
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
                     "iam": {
                            "accessKey": "AKIA...",
                            "accountId": "111122223333",
                            "callerId": "AIDA...",
                            "cognitoIdentity": None,
                            "principalOrgId": None,
                            "userArn": "arn:aws:iam::111122223333:user/example-user",
                            "userId": "AIDA..."
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
              "body": '{"user_id": "123", "code": "ELET355"}',
              "pathParameters": None,
              "isBase64Encoded": None,
              "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 400
              assert json.loads(response["body"]) == "Field user_id is not valid"

       def test_enroll_activity_presenter_400_code_invalid(self):
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
                     "iam": {
                            "accessKey": "AKIA...",
                            "accountId": "111122223333",
                            "callerId": "AIDA...",
                            "cognitoIdentity": None,
                            "principalOrgId": None,
                            "userArn": "arn:aws:iam::111122223333:user/example-user",
                            "userId": "AIDA..."
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
              "body": '{"user_id": "b16f", "code": 3}',
              "pathParameters": None,
              "isBase64Encoded": None,
              "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 400
              assert json.loads(response["body"]) == "Field code is not valid"

       def test_enroll_activity_presenter_403_forbidden_action(self):
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
                     "iam": {
                            "accessKey": "AKIA...",
                            "accountId": "111122223333",
                            "callerId": "AIDA...",
                            "cognitoIdentity": None,
                            "principalOrgId": None,
                            "userArn": "arn:aws:iam::111122223333:user/example-user",
                            "userId": "AIDA..."
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
              "body": '{"user_id": "db43", "code": "ECM2345"}',
              "pathParameters": None,
              "isBase64Encoded": None,
              "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 403
              assert json.loads(response["body"]) == 'That action is forbidden for this Enrollment'

       def test_enroll_activity_presenter_404_no_items_found_activity(self):
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
                     "iam": {
                            "accessKey": "AKIA...",
                            "accountId": "111122223333",
                            "callerId": "AIDA...",
                            "cognitoIdentity": None,
                            "principalOrgId": None,
                            "userArn": "arn:aws:iam::111122223333:user/example-user",
                            "userId": "AIDA..."
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
              "body": '{"user_id": "80fb", "code": "CODIGO_INEXISTENTE"}',
              "pathParameters": None,
              "isBase64Encoded": None,
              "stageVariables": None
              }

              response = lambda_handler(event, None)
              assert response["statusCode"] == 404
              assert json.loads(response["body"]) == 'No items found for Activity'