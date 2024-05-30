import time

import boto3
from boto3.dynamodb.conditions import Key, Attr
from pprint import pprint as p
from enviroment import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME
from data import STUDENTS

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

student_stable = dynamodb.Table('student')

## Insert Item
for student in STUDENTS:
    item = student_stable.put_item(
        Item=student
    )
    time.sleep(0.1)

## Query Student có id = st-01, name = 'Linh'
# response = student_stable.get_item(
#     Key={
#         'id': 'st-01',
#         'name': 'Thach'
#     }
# )
#
# student = response.get('Item')
# p(student)


## Scan student có name = 'Phuong'
# response = student_stable.scan(
#     FilterExpression=boto3.dynamodb.conditions.Attr('name').eq('Phuong')
# )
#
# students = response.get('Items')
# p(students)


## Scan student có is_married = True
# response = student_stable.scan(
#     FilterExpression=boto3.dynamodb.conditions.Attr('is_married').eq(False)
# )
#
# students = response
# p(students)

## Update Student có id = st-01: birthday = 1993/05/06
# response = student_stable.update_item(
#     Key={
#         'id': 'st-01',
#     },
#     UpdateExpression='SET is_married = :val1',
#     ExpressionAttributeValues={
#         ':val1': True
#     }
# )
#
# p(response)

## Delete Student có id = st-03
# response = student_stable.delete_item(
#     Key={
#         'id': 'st-01'
#     }
# )
#
# p(response)
