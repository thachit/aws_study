import json
import time
import boto3
from enviroment import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, QUEUE_URL


sqs = boto3.client(
    'sqs',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)


response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        DelaySeconds=0,
        MessageBody=(
            json.dumps({
                'name': f'Phuong',  # {int(time.time())}
                'age': 35
            })
        )
    )

message_id = response.get('MessageId', None)
print(message_id)