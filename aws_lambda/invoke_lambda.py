import boto3
import json

# Initialize a Lambda client (using LocalStack's endpoint)
lambda_client = boto3.client('lambda', endpoint_url='http://localhost:4566')

# Prepare the event data
event = {'name': 'Panashe'}

# Invoke the Lambda function
response = lambda_client.invoke(
    FunctionName='hello-world',
    Payload=json.dumps(event),
)

# Read and print the response
response_payload = json.loads(response['Payload'].read().decode())
print("Lambda response:", response_payload)
