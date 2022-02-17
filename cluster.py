from messages import CLUSTER_INVALID_INSTANCES_CONFIG, CLUSTER_INVALID_ROOT_CONFIG
import boto3
import os


class EMRCluster:

    def __init__(self, config: dict) -> None:
        region = os.environ['aws_region']
        emr = boto3.client('emr', region_name=region)
        self.load_config(config)
        self.create_cluster(emr)


    def load_config(self, config):
        try:
            # Required configs
           self.name = config['Name']
           self.log_uri_s3 = config['LogUri']
           self.release_label = config['ReleaseLabel']
           self.instances = self.parse_instances(config['Instances'])
           self.job_flow_role = config['JobFlowRole']
           self.service_role = config['ServiceRole']
        except KeyError:
            print(CLUSTER_INVALID_ROOT_CONFIG)

        # Optional configs
        self.visible_to_all_users = bool(config.get('VisibleToAllUsers', True))
        self.steps = config.get('Steps', [])
        self.applications = config.get('Applications', [])
        self.tags = config.get('Tags', [])


    def parse_instances(self, instances: dict) -> dict:
        try:
            instances["TerminationProtected"] = bool(instances["TerminationProtected"])
            instances["KeepJobFlowAliveWhenNoSteps"] = bool(instances["KeepJobFlowAliveWhenNoSteps"])
            groups = instances.get('InstanceGroups', [])
            
            for instance in groups:
                instance['InstanceCount'] = int(instance['InstanceCount'])

            instances['InstanceGroups'] = groups
            return instances
        except KeyError:
            print(CLUSTER_INVALID_INSTANCES_CONFIG)


    def create_cluster(self, emr_client) -> str:
        cluster_id = emr_client.run_job_flow(
            Name = self.name,
            LogUri = self.log_uri_s3,
            ReleaseLabel = self.release_label,
            Applications = self.applications,
            Instances = self.instances,
            Steps = self.steps,
            VisibleToAllUsers = self.visible_to_all_users,
            JobFlowRole = self.job_flow_role,
            ServiceRole = self.service_role,
            Tags = self.tags
        )
        print(f"Cluster created. ID: {cluster_id}")
        return cluster_id
    
    
    def add_steps(emr_client, cluster_id: str, steps: list) -> None:
        if not steps:
            print(f'No steps were passed to cluster: {cluster_id}')

        action = emr_client.add_job_flow_steps(JobFlowId=cluster_id, Steps=steps)
        print(f"Added step(s): {action}")

