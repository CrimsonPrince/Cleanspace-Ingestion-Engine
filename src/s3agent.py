import boto3
from datetime import datetime

s3client = boto3.client('s3', region_name='us-east-1')
objects = s3client.list_objects(Bucket='openaq-fetches')


print(objects)
print(datetime.now().date())