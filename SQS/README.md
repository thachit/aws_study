
# Build Docker Image
docker build -t aws_sqs_consumer -f consumer.Dockerfile .
docker build -t aws_sqs_producer -f producer.Dockerfile .

# RUN Docker
docker run -d --env-file <ENV FLE> --name aws_sqs_consumer_1.0 <CONTAINER IMAGE ID>


# Pull Docker from Docker Hub
docker pull thachit/aws_sqs_producer:lasted
docker pull thachit/aws_sqs_consumer:lasted