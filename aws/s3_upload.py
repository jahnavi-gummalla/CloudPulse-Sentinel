import boto3

s3 = boto3.client("s3")

file_name = "reports/report.html"
bucket_name = "YOUR_BUCKET_NAME"
object_name = "api-test-report.html"

s3.upload_file(file_name, bucket_name, object_name)

print("Report uploaded successfully to S3")