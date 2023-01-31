import json

from src.modules.enroll_activity.app.enroll_activity_presenter import lambda_handler



class Test_EnrollActivityPresenter:
       def test_enroll_activity_presenter(self):
              # event = {
              # "version": "2.0",
              # "routeKey": "$default",
              # "rawPath": "/my/path",
              # "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
              # "cookies": [
              #        "cookie1",
              #        "cookie2"
              # ],
              # "headers": {
              #        "header1": "value1",
              #        "header2": "value1,value2"
              # },
              # "queryStringParameters": {
              #        'query_params': "value1"
              # },
              # "requestContext": {
              #        "accountId": "123456789012",
              #        "apiId": "<urlid>",
              #        "authentication": None,
              #        "authorizer": {
              #        "iam": {
              #               "accessKey": "AKIA...",
              #               "accountId": "111122223333",
              #               "callerId": "AIDA...",
              #               "cognitoIdentity": None,
              #               "principalOrgId": None,
              #               "userArn": "arn:aws:iam::111122223333:user/example-user",
              #               "userId": "AIDA..."
              #        }
              #        },
              #        "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
              #        "domainPrefix": "<url-id>",
              #        "external_interfaces": {
              #        "method": "POST",
              #        "path": "/my/path",
              #        "protocol": "HTTP/1.1",
              #        "sourceIp": "123.123.123.123",
              #        "userAgent": "agent"
              #        },
              #        "requestId": "id",
              #        "routeKey": "$default",
              #        "stage": "$default",
              #        "time": "12/Mar/2020:19:03:58 +0000",
              #        "timeEpoch": 1583348638390
              # },
              # "body": '{"user_id": "0355573c-a110-11ed-a8fc-0242ac120002", "code": "COD1468"}',
              # "pathParameters": None,
              # "isBase64Encoded": None,
              # "stageVariables": None
              # }

              event = {'resource': '/mss-activity/enroll-activity', 'path': '/mss-activity/enroll-activity', 'httpMethod': 'POST', 'headers': None, 'multiValueHeaders': None, 'queryStringParameters': None, 'multiValueQueryStringParameters': None, 'pathParameters': None, 'stageVariables': None, 'requestContext': {'resourceId': 'e47982', 'resourcePath': '/mss-activity/enroll-activity', 'httpMethod': 'POST', 'extendedRequestId': 'e9YYYFhKGjQFRWg=', 'requestTime': '18/Jan/2023:22:08:15 +0000', 'path': '/mss-activity/enroll-activity', 'accountId': '264055331071', 'protocol': 'HTTP/1.1', 'stage': 'test-invoke-stage', 'domainPrefix': 'testPrefix', 'requestTimeEpoch': 1674079695163, 'requestId': 'd3879c1d-a8e5-4fe7-a60a-1314c95bc9da', 'identity': {'cognitoIdentityPoolId': None, 'cognitoIdentityId': None, 'apiKey': 'test-invoke-api-key', 'principalOrgId': None, 'cognitoAuthenticationType': None, 'userArn': 'arn:aws:iam::264055331071:user/Bruno', 'apiKeyId': 'test-invoke-api-key-id', 'userAgent': 'aws-internal/3 aws-sdk-java/1.12.358 Linux/5.4.225-139.416.amzn2int.x86_64 OpenJDK_64-Bit_Server_VM/25.352-b10 java/1.8.0_352 vendor/Oracle_Corporation cfg/retry-mode/standard', 'accountId': '264055331071', 'caller': 'AIDAT26XMTD7XPTLJWEJT', 'sourceIp': 'test-invoke-source-ip', 'accessKey': 'ASIAT26XMTD7YYAXOOEC', 'cognitoAuthenticationProvider': None, 'user': 'AIDAT26XMTD7XPTLJWEJT'}, 'domainName': 'testPrefix.testDomainName', 'apiId': '4swgp6kxi8'}, 'body': '{"user_id": "0355573c-a110-11ed-a8fc-0242ac120002", "code": "COD1468"}', 'isBase64Encoded': False}

              response = lambda_handler(event, None)

              assert response["statusCode"] == 200
              assert json.loads(response["body"])['message'] == 'the enrollment was enrolled'

       def test_enroll_activity_presenter_in_queue(self):
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
              "body": '{"user_id": "4d1d64ae-a110-11ed-a8fc-0242ac120002", "code": "ECM2345"}',
              "pathParameters": None,
              "isBase64Encoded": None,
              "stageVariables": None
              }

              response = lambda_handler(event, None)

              assert response["statusCode"] == 200
              assert json.loads(response["body"])['message'] == 'the enrollment was in queue'

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
              "body": '{"user_id": "0355535e-a110-11ed-a8fc-0242ac120002"}',
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
              "body": '{"user_id": "0355535e-a110-11ed-a8fc-0242ac120002", "code": 3}',
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
              "body": '{"user_id": "d61dbf66-a10f-11ed-a8fc-0242ac120002", "code": "ECM2345"}',
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
              "body": '{"user_id": "0355573c-a110-11ed-a8fc-0242ac120002", "code": "CODIGO_INEXISTENTE"}',
              "pathParameters": None,
              "isBase64Encoded": None,
              "stageVariables": None
              }

              response = lambda_handler(event, None)
              
              assert response["statusCode"] == 404
              assert json.loads(response["body"]) == 'No items found for Activity'
