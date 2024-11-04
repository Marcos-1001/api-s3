import boto3
import json

def lambda_handler(event, context):
    bucket_name =  event['body']['bucket_nombre']
    dir = event['body']['directorio_nombre']
    file_name = event['body']['archivo_nombre']
    file_content = event['body']['archivo_contenido']
    try:
        s3 = boto3.client('s3',region_name='us-east-1')
        s3.put_object(Bucket=bucket_name, Key=dir+'/'+file_name, Body=file_content)
       
        
        return {
            'statusCode': 200,
            'body': json.dumps('Archivo subido con éxito')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error al subir el archivo {e}')
        }