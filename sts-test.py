#!/usr/bin/env python3

import boto3

def list_objects(*args):
	try:
		s3 = boto3.resource(
			's3',
			aws_access_key_id=access_key_id,
			aws_secret_access_key=secret_access_key,
			aws_session_token=session_token
		)
		bucket = s3.Bucket('my-bucket')
		objects = []
		
		for object in bucket.objects.all():
			objects.append(object.key)

		return(objects)	
	except:
		raise

def get_temporary_credentials():
	try:
		sts = boto3.client('sts')
		response = sts.assume_role(
			RoleArn = 'arn:aws:iam::123456789012:role/MyRole',
			RoleSessionName = 'sts-test_jpdoria',
			DurationSeconds = 900
		)

		return(
			response['Credentials']['AccessKeyId'],
			response['Credentials']['SecretAccessKey'],
			response['Credentials']['SessionToken']
		)
	except:
		raise

if __name__ == '__main__':
	access_key_id, secret_access_key, session_token = get_temporary_credentials()

	print(list_objects(access_key_id, secret_access_key, session_token))