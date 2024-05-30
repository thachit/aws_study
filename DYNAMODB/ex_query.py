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

response = users_stable.query(
    IndexName='email-index',
    KeyConditionExpression=Key("email").eq("thach.nguyen+19892024052002@elsanow.io")
)

users = response.get('Items')

p(users[0])


