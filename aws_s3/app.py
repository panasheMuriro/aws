import boto3
from botocore.exceptions import NoCredentialsError

# Configure Boto3 to use LocalStack's S3 endpoint
s3_client = boto3.client('s3', endpoint_url='http://localhost:4566')

# Bucket and file names
bucket_name = 'local-s3-bucket'
file_name = 'example.txt'

# Create a bucket
try:
    # s3_client.create_bucket(Bucket=bucket_name)
    # print(f"Bucket '{bucket_name}' created.")
    
    # Create a simple file
    with open(file_name, 'w') as f:
        f.write("Hello, this is a test file for LocalStack S3.")
    
    # Upload the file
    s3_client.upload_file(file_name, bucket_name, file_name)
    print(f"File '{file_name}' uploaded to bucket '{bucket_name}'.")
    
    # List objects in the bucket
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        print(f"Objects in '{bucket_name}':")
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("No objects in the bucket.")
    
    # Download the file
    s3_client.download_file(bucket_name, file_name, f"downloaded_{file_name}")
    print(f"File '{file_name}' downloaded from bucket '{bucket_name}'.")
    
    # Delete the file
    s3_client.delete_object(Bucket=bucket_name, Key=file_name)
    print(f"File '{file_name}' deleted from bucket '{bucket_name}'.")
    
    # Delete the bucket
    s3_client.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted.")

except NoCredentialsError:
    print("Credentials not found.")
except Exception as e:
    print(f"An error occurred: {e}")


    """
    OUTPUT
    
    File 'example.txt' uploaded to bucket 'local-s3-bucket'.
Objects in 'local-s3-bucket':
example.txt
File 'example.txt' downloaded from bucket 'local-s3-bucket'.
File 'example.txt' deleted from bucket 'local-s3-bucket'.
Bucket 'local-s3-bucket' deleted.

    """