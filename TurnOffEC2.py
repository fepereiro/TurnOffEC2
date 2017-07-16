from __future__ import print_function

import boto3

def toggle_instance(instance):
    ec2 = boto3.resource("ec2", region_name="eu-west-1")
    instance = ec2.Instance(instance["InstanceId"])
    instance.stop()
    print('Instance stopped.')

def lambda_handler(event, context):
    print('Looking for instances.')
    ec2_client = boto3.client("ec2", region_name="eu-west-1")
    description = ec2_client.describe_instances( Filters=[ { 'Name': 'tag-key', 
        'Values': ['env'] },
        { 'Name': 'tag-value', 'Values' : ['dev'] }])

    for reservation in description["Reservations"]:
        for instance in reservation["Instances"]:
            print('Instance: {}'.format(instance["InstanceId"]))
            toggle_instance(instance)
