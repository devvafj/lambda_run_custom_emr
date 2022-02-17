# Lambda Run Custom EMR

Creates AWS EMR Clusters with stored configs using a lambda function.

## Requirements on Lambda
- A Lambda Function created on AWS
- A DynamoDB table to store your cluster configs
- The Lambda Function Role needs access to the following AWS Services: EMR, DynamoDB
- An EC2 Key Pair to pass to EMR

## Getting Started

1. Create a DynamoDB table to store your cluster configs. Use a field named Id as the partition key
2. On AWS EC2 service, create a Key Pair, save the file and note the Key Pair name. You'll need to pass this name in the cluster config
3. For the a sample test, you can copy and paste the content of file: `utils/sample_cluster_config.json` as an item of your DynamoDB table
4. Change in the config the Ec2KeyName value to the Key Pair name created on step 2
5. Change the config the Ec2SubnetId value to a valid Subnet Id for your account (you can discover subnet-id when you try to create
   an EMR Cluster manually in the Network section).
6. Create your Lambda Function and give the necessary policies to the Lambda Function Role
7. If you don't know what policies to use, attach the policy `AmazonEMRFullAccessPolicy_v2` on IAM to the Lambda Function Role and copy the content of the file: `utils/inline_lambda_policies.json` and attach it too as an inline policy
8. Copy all the .py files to your Lambda Function directory on Editor
9. Create the following environment variables on Lambda:
   - aws_region: Region where your AWS resources are located, e.g. 'us-east-1'
   - clusters_table_name: Your DynamoDB table name, created on step 1 e.g. 'data-platform-emr-clusters'
   - config_id: The value of the Id field in your DynamoDB table, representing the cluster config you want to use e.g. 'd8a4606020664173b3064946a0d52b2c' if you used the `sample_cluster_config.json` file.
  