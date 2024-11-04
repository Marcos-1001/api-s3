import boto3
import json

def lambda_handler(event, context):
    bucket_name =  event['body']['nombre']
    try:
        s3 = boto3.client('s3')
        s3.create_bucket(Bucket=bucket_name, ObjectOwnership='BucketOwnerPreferred')
        s3.put_bucket_acl(
            Bucket=bucket_name,
            ACL='public-read-write'
        )
        
        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )

        
        return {
            'statusCode': 200,
            'body': json.dumps('Bucket creado con éxito')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error al crear el bucket')
        }