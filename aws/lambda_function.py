import json
import requests
import boto3
from datetime import datetime

s3 = boto3.client("s3")
sns = boto3.client("sns")

BUCKET_NAME = "YOUR_BUCKET_NAME"

TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

def lambda_handler(event, context):

    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    result = {
        "status_code": response.status_code,
        "response_time": response.elapsed.total_seconds(),
        "timestamp": str(datetime.utcnow())
    }

    file_name = "/tmp/report.json"

    with open(file_name, "w") as file:
        json.dump(result, file)

    s3.upload_file(
        file_name,
        BUCKET_NAME,
        "lambda-report.json"
    )

    if response.status_code != 200:

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="API Monitoring Alert",
            Message="API endpoint failed health check"
        )

    return {
        "statusCode": 200,
        "body": result
    }