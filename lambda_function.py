from cluster import EMRCluster
from dynamo import ddb_deserialize
import os
import boto3


def lambda_handler(event, context):
    region = os.environ['aws_region']
    clusters_table_name = os.environ['clusters_table_name']
    config_id = os.environ['config_id']
    
    dynamodb = boto3.client('dynamodb', region_name=region)
    
    response = dynamodb.get_item(
        TableName=clusters_table_name,
        Key={'Id': {'S': config_id } }
    )
    item = ddb_deserialize(response['Item'])

    EMRCluster(config=item)