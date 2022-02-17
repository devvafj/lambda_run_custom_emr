

CLUSTER_INVALID_ROOT_CONFIG = """
One or more keys weren't founded in config JSON (root level):\n
- Name (string)\n 
- LogUri (string)\n
- ReleaseLabel (string)\n
- Instances (dict)\n
- JobFlowRole (string)\n
- ServiceRole (string) \n
For more details, see the run_job_flow request syntax in documentation:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.run_job_flow
"""

CLUSTER_INVALID_INSTANCES_CONFIG = """
"One or more keys weren't founded inside 'Instances' key.\n
- TerminationProtected (string bool)\n
- KeepJobFlowAliveWhenNoSteps (string bool)\n
- InstanceGroups (dict)\n 
- InstanceCount (string int) inside each InstanceGroups"
For more details, see the run_job_flow request syntax in documentation:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/emr.html#EMR.Client.run_job_flow
"""