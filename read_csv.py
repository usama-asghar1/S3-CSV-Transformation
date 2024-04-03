import boto3
import pandas as pd

s3_client = boto3.client('s3')

# read csv as df from s3 bucket
bucket_name = 'data-eng-resources'
s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/fish-market.csv'
)

fish_df = pd.read_csv(s3_object['Body'])
