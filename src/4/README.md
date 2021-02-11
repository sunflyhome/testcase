# Cloudformation Template s3_cfn.json

# The tmplate will only work in us-west-2 as there is only AMI mapping for us-west-1

# Description

## Create S3 bucket, mc-test-repo-20210210

## Create s3 access roles and assign to an instance profile

## Create Amazon Linux 2 Ec2 instance on T2.micro with few basic settings such as security group, instance file, AMI, etc.

## run bash commands during user-data after cfn-init to create a new repo

## Copy printAweSome rpm from question 5 to s3 bucket under x86_64

### test:

wget https://mc-test-repo-20210210.s3-us-west-2.amazonaws.com/x86_64/printAweSome-1-0.x86_64.rpm
--2021-02-11 11:40:58--  https://mc-test-repo-20210210.s3-us-west-2.amazonaws.com/x86_64/printAweSome-1-0.x86_64.rpm
Resolving mc-test-repo-20210210.s3-us-west-2.amazonaws.com (mc-test-repo-20210210.s3-us-west-2.amazonaws.com)... 52.218.201.9
Connecting to mc-test-repo-20210210.s3-us-west-2.amazonaws.com (mc-test-repo-20210210.s3-us-west-2.amazonaws.com)|52.218.201.9|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2452 (2.4K) [binary/octet-stream]
Saving to: ‘printAweSome-1-0.x86_64.rpm’

printAweSome-1-0.x86_64.rpm     100%[======================================================>]   2.39K  --.-KB/s    in 0.001s  

2021-02-11 11:40:59 (2.73 MB/s) - ‘printAweSome-1-0.x86_64.rpm’ saved [2452/2452]



## Install rpm to default folder /etc/printAweSome
