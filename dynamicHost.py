#!/usr/bin/env python
import os
import sys
import json
import boto3 

ec2client = boto3.client('ec2',region_name='us-east-1',aws_access_key_id='AKIAILGCHGILLNRWEUKA',aws_secret_access_key='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')



response = ec2client.describe_instances(
    Filters=[
        {
	    'Name': 'tag:Name',
            'Values': ['petclinic']
        }
    ]
    )
PublicIpAddress = ""
list= []
instancelist = []
header = "{\'group\': {\'hosts\': "
footer = "}}"
for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
       # host = host+"\'"+ PublicIpAddress + "\'"
        PublicIpAddress=instance["PublicIpAddress"]
        list.append(PublicIpAddress);
        #print "\'"+PublicIpAddress+"\'" 

print header        
print list
print footer
