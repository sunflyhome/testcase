# Cloudformation Template s3_cfn.json

# The tmplate will only work in us-west-2 as there is only AMI mapping for us-west-1

# Description

## Create S3 bucket, mc-test-repo-20210210

## Create s3 access roles and assign to an instance profile

## Create Amazon Linux 2 Ec2 instance on T2.micro with few basic settings such as security group, instance file, AMI, etc.

## run bash commands during user-data after cfn-init to create a new repo

## Copy printAweSome rpm from question 5 to s3 bucket under x86_64

## Install rpm to default folder /etc/printAweSome
