
import boto3
import json
import uuid

s3 = boto3.client("s3")
BUCKET = "study-buddy-notes-thuli"

def lambda_handler(event, context):
    try:
        note_text = event.get("note", "").strip()

        if not note_text:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "isBase64Encoded": False,
                "body": json.dumps({"error": "Note is empty"})
            }

        # Generate unique note ID
        note_id = f"{uuid.uuid4()}.txt"

        # Save note to S3
        s3.put_object(
            Bucket=BUCKET,
            Key=note_id,
            Body=note_text.encode("utf-8"),
            ContentType="text/plain"
        )

        # ✅ Important: body must be a JSON string,
        # but API Gateway will not wrap again if you set headers+isBase64Encoded properly
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "isBase64Encoded": False,
            "body": json.dumps({"note_id": note_id})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "isBase64Encoded": False,
            "body": json.dumps({"error": str(e)})
        }
