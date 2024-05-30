import time

import boto3
from boto3.dynamodb.conditions import Key, Attr
from pprint import pprint as p
from enviroment import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

users_stable = dynamodb.Table('users')

users_data = []

response = users_stable.scan(
    FilterExpression=Attr('email').eq('thach.nguyen+19892024052002@elsanow.io'),
    Select='ALL_ATTRIBUTES'
)
users_data.extend(response.get('Items', []))


while 'LastEvaluatedKey' in response:
    response = users_stable.scan(
        FilterExpression=Attr('email').eq('thach.nguyen+19892024052002@elsanow.io'),
        Select='ALL_ATTRIBUTES',
        ExclusiveStartKey=response['LastEvaluatedKey']
    )
    count = response.get('Count', 0)
    scanned_count = response.get('ScannedCount')
    print(f"[ScannedCount] scanned_count = {scanned_count}")
    if count > 0:
        users_data.extend(response.get('Items', []))
    time.sleep(.01)

p(users_data)


