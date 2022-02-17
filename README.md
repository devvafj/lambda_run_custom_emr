# Lambda Run Custom EMR
Creates AWS EMR Clusters with stored configs using a lambda function.

## Requirements on Lambda
- A Lambda Function created on AWS
- A DynamoDB table to store your cluster configs
- The Lambda Function Role needs access to the following AWS Services: EMR, DynamoDB

## Getting Started
1. Create a DynamoDB table to store your cluster configs. Use a field named Id as the partition key
2. Create your Lambda Function and give the necessary policies to the Lambda Function Role
3. If you don't know what policies to use, copy the content of the file: `inline_lambda_policies.json` and attach it as an inline policy to your Function Role on AWS IAM
4. Copy all the .py files to your Lambda function directory on Editor
5. Create the following environment variables on Lambda:
   - aws_region: Region where your AWS resources are located, e.g. 'us-east-1' 
   - clusters_table_name: Your DynamoDB table name, created on step 1 e.g. 'data-platform-emr-clusters'
   - config_id: The value of the Id field in your DynamoDB table, representing the cluster config you want to use e.g. 'e28594727f084163ae5e2263b4358706'