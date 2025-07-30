import gzip
import json
import boto3
import base64
from datetime import datetime

s3 = boto3.client('s3')
bucket_name = 'log-analyzer-hridya'  

def lambda_handler(event, context):
    data = event['awslogs']['data']
    
    # Decode & decompress logs
    compressed_payload = base64.b64decode(data)
    uncompressed_payload = gzip.decompress(compressed_payload)
    logs = json.loads(uncompressed_payload)

    # Create a folder path based on timestamp
    timestamp = datetime.utcnow()
    key = f"logs/{timestamp.year}/{timestamp.month:02d}/{timestamp.day:02d}/log-{timestamp.strftime('%H-%M-%S')}.json"

    # Upload to S3
    s3.put_object(
        Bucket=bucket_name,
        Key=key,
        Body=json.dumps(logs, indent=2),
        ContentType='application/json'
    )

    return {
        'statusCode': 200,
        'body': f"Log saved to s3://{bucket_name}/{key}"
    }
