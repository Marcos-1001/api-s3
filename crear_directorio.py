import boto3
import json

def lambda_handler(event, context):
    bucket_name =  event['body']['bucket_nombre']
    dir_name = event['body']['directorio_nombre']
    try:
        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket_name, Key=dir_name+'/')


        return {
            'statusCode': 200,
            'body': json.dumps('Directorio creado con éxito')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error al crear el directorio {e}')
        }