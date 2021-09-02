import os
import boto3


s3_client = boto3.client("s3")
S3_BUCKET = os.environ.get("S3_BUCKET")


def lambda_handler(event, _context):
    s3_key: str = event["s3_key"]
    body: str = event["body"]

    s3_client.put_object(Key=s3_key, Bucket=S3_BUCKET, Body=body.encode())
