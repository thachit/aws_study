import json
import time
import boto3
import uuid
from enviroment import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, REGION_NAME, QUEUE_URL


sqs = boto3.client(
    'sqs',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=REGION_NAME
)

message_group_id = "Order123"
message_deduplication_id = str(uuid.uuid4())

response = sqs.send_message(
        QueueUrl=QUEUE_URL,
        # MessageGroupId=message_group_id,
        # MessageDeduplicationId=message_deduplication_id,
        MessageBody=(
            json.dumps({
                'name': f'Phuong',  # {int(time.time())}
                'age': 35
            })
        )
    )

message_id = response.get('MessageId', None)
print(f"Message ID = {message_id}, message_deduplication_id = {message_deduplication_id}")