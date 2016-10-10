# About
This script shows how to use AWS Security Token Service (STS) to grant temporary access for calling APIs.

# Prerequisites
* Python 3.5+
* Boto3 (pip3 install boto3)
* Your AWS Access Key ID and Secret Access Key
* IAM Role

# IAM Role Trust Relationship Configuration
To use the permissions from the IAM Role for your IAM Account:

1. Go to the IAM Role you want to use
2. Edit Trust Relationship
3. Add these lines:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "elasticbeanstalk.amazonaws.com",
          "ec2.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/test-user-0001"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

4. test-user-0001, EC2, and Elastic Beanstalk can now use the permissions from the IAM Role

# Reference
http://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_modify.html
