import boto3

# Replace the placeholders with your own values
aws_access_key_id = "AKIAZEMN2IZPEHZOE7VA"
aws_secret_access_key = "mzpLB5U5Z9rLpRZY8/2+Sdex0ds0craPghcoLGQK"
bucket_name = "01bde78a86dcc1d1fc"


s3_path_hello_world = "task1/hello-world.txt"
s3_path_s3_connect = "task1/s3_connect.py"
s3_path_string_filtering = "task2/string_filtering.py"
s3_path_s3_querysql = "task3/queries.sql"
s3_path_s3_aws_env_vars = "task4/aws_env_vars.py"
s3_path_s3_json_parsing = "task5/json_parsing.py"

# Connect to AWS S3 using the provided AWS access keys
s3 = boto3.resource("s3",
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    region_name="us-east-1")

# Upload hello-world.txt, string_filtering.py and queries.sql to the S3 paths
data_hello_world = b"Hello World\n"
data_string_filtering = b"String Fitering\n"
data_querysql = b"Queries\n"
data_aws_env_vars = b"AWS environment variables\n"
data_aws_json_parsing = b"Json Parsing\n"

s3.Object(bucket_name, s3_path_hello_world).put(Body=data_hello_world)
s3.Object(bucket_name, s3_path_string_filtering).put(Body=data_string_filtering)
s3.Object(bucket_name, s3_path_s3_querysql).put(Body=data_querysql)
s3.Object(bucket_name, s3_path_s3_aws_env_vars).put(Body=data_aws_env_vars)
s3.Object(bucket_name, s3_path_s3_json_parsing).put(Body=data_aws_json_parsing)

# Upload s3_connect.py
with open(__file__, "rb") as file:
    s3.Object(bucket_name, s3_path_s3_connect).put(Body=file)

print("Files uploaded successfully!")

# Upload both hello_world.txt and this file to the S3 paths
# s3://01bde78a86dcc1d1fc/task1/hello-world.txt and
# s3://01bde78a86dcc1d1fc/task1/s3_connect.py
