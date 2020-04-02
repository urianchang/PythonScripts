# Python 3.7
import boto3

AWS_KEY_ID = ""
AWS_SECRET_KEY = ""
BUCKET = ""
PREFIX = ""
STARTAFTER = ""

# Method 1: Get all file objects
conn = boto3.resource('s3', endpoint_url=None, aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)
conn.meta.client.head_bucket(Bucket=BUCKET)
bucket = conn.Bucket(BUCKET)

obj_sum_list = bucket.objects.filter(Prefix=PREFIX)
for obj_sum in obj_sum_list:
  print(obj_sum)

# Method 2: Get file objects after a specific file
client = boto3.client('s3', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET_KEY)

# Client.list_objects_v2() can only retrieve a maximum of 1000 objects per request
obj_dict = client.list_objects_v2(Bucket=BUCKET, Prefix=PREFIX, StartAfter=STARTAFTER)
# Another way of running the query without running create client separately: conn.meta.client.list_objects_v2(Bucket=BUCKET, Prefix=PREFIX)

"""
AWS CLI:

List all file objects

```
aws s3 ls "<url>" --recursive
```

"""
