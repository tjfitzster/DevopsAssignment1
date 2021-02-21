# Student: TJ Fitzpatrick
# Student Number: 20027865
# Assignment 1. 
# Dev Ops Module


# create an EC2 instance
# launch the EC2 instance.
import boto3
import sys

aws_access_key_id_input1 = sys.argv[1]
aws_secret_access_key_input2 = sys.argv[2]

ec2 = boto3.resource('ec2', 'eu-west-1', aws_access_key_id=aws_access_key_id_input1, aws_secret_access_key=aws_secret_access_key_input2)
instance = ec2.create_instances(
    ImageId='ami-0fc970315c2d38f01',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.nano')
