import boto3
import json

def lambda_handler(event, context):
    bucket_name =  event['body']['nombre']
    try:
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.create_bucket(Bucket=bucket_name, ObjectOwnership='BucketOwnerPreferred',
                         CreateBucketConfiguration={
                             'LocationConstraint': 'us-east-1'
                         })
        

        s3.put_public_access_block(
            Bucket=bucket_name,
            PublicAccessBlockConfiguration={
                'BlockPublicAcls': False,
                'IgnorePublicAcls': False,
                'BlockPublicPolicy': False,
                'RestrictPublicBuckets': False
            }
        )
        s3.put_bucket_acl(
            ACL='public-read-write',
            Bucket=bucket_name            
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Bucket creado con éxito')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error al crear el bucket {e}')
        }