import json


def post(event, context):
    body = event['body']
    print(body)
    new_body = json.loads(body)
    result = {
        "event_data": event, 
        "body": new_body
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }
    return response

def get(event, context):
    print(event)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
