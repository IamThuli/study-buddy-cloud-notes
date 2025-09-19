
import boto3
import json

s3 = boto3.client('s3')
BUCKET = "study-buddy-notes-thuli"

def lambda_handler(event, context):
    note_id = event["queryStringParameters"].get("note_id")
   
    obj = s3.get_object(Bucket=BUCKET, Key=note_id)
    note_text = obj['Body'].read().decode('utf-8')
   
    return {
        "statusCode": 200,
        "body": json.dumps({"note": note_text})
    }
