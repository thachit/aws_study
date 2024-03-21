import time
import boto3
from pprint import pprint as p

from enviroment import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, QUEUE_URL

sqs = boto3.client(
    'sqs',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

while True:
    print("====================Get Message===============")
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL
    )
    # print(response)
    messages = response.get('Messages', [])
    for message in messages:
        body = message.get('Body')
        message_id = message.get('MessageId')
        receipt_handle = message.get('ReceiptHandle')
        print(f"\nMessage ID = {message_id}, body = {body}")

        print("*** Delete Message")
        sqs.delete_message(
            QueueUrl=QUEUE_URL,
            ReceiptHandle=receipt_handle
        )

    time.sleep(5)