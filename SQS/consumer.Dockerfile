FROM python:3.9.19-bullseye as build
WORKDIR src/aws_pracetise
COPY exercise_1 .

RUN pip install -r requirements.txt
CMD ["python", "consumer.py"]
