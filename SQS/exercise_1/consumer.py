import time
import boto3

from enviroment import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, QUEUE_URL

SLEEP_TIME = 0.1
PROCESS_TIME_TEST = input("Input process time test: ")

PROCESS_TIME_TEST = int(PROCESS_TIME_TEST)

VISIBILITY_TIMEOUT = 22


sqs = boto3.client(
    'sqs',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

while True:
    # print("====================Get Message===============")
    response = sqs.receive_message(
        QueueUrl=QUEUE_URL,
        VisibilityTimeout=VISIBILITY_TIMEOUT
    )
    # print(response)
    messages = response.get('Messages', [])
    for message in messages:
        body = message.get('Body')
        message_id = message.get('MessageId', None)
        receipt_handle = message.get('ReceiptHandle')
        print(f"\nMessage ID = {message_id}, ReceiptHandle = {receipt_handle}, body = {body}")
        if message_id:
            time.sleep(PROCESS_TIME_TEST)

        try:
            sqs.delete_message(
                QueueUrl=QUEUE_URL,
                ReceiptHandle=receipt_handle
            )

            print("*** Delete Message successfully")
        except Exception as exc:
            print(f"*** Delete Message Failed: {str(exc)}")

    time.sleep(SLEEP_TIME)
