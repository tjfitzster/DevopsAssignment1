# Student: TJ Fitzpatrick
# Student Number: 20027865
# Assignment 1. 
# Dev Ops Module


# create an EC2 instance
# launch the EC2 instance.
import boto3
import sys
# reading credentials from text file.
textfile = open("credentials.txt", "r")
content = textfile.read()
content_list = content.split(" ")
textfile.close()

aws_access_key_id_input1 = content_list[0]
aws_secret_access_key_input2 = content_list[1]

ec2 = boto3.resource('ec2', 'eu-west-1', aws_access_key_id=aws_access_key_id_input1, aws_secret_access_key=aws_secret_access_key_input2)
instance = ec2.create_instances(
    ImageId='ami-0fc970315c2d38f01',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.nano')
