import boto3
import io
from cleaning_and_transformation import *

s3_client = boto3.client('s3')
bucket_name = 'data-eng-resources'

str_buffer = io.StringIO()
avg_species.to_csv(str_buffer)

s3_client.put_object(
    Body=str_buffer.getvalue(),
    Bucket=bucket_name,
    Key='Data401/usama.csv'
)

