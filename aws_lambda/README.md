
# Create a Simple Lambda Function
First, let's create a Python Lambda function. Create a file called lambda_function.py:

```
def lambda_handler(event, context):
    name = event.get('name', 'World')
    return {
        'statusCode': 200,
        'body': f"Hello, {name}!"
    }
```
This Lambda function simply takes an event (which could contain a name) and returns a greeting.

## Create an IAM Role for Lambda
Lambda functions require an IAM role with basic Lambda execution permissions. Create a simple role for LocalStack Lambda using the AWS CLI:

```
awslocal iam create-role --role-name lambda-execution-role --assume-role-policy-document file://trust-policy.json

```
Create a trust-policy.json file with the following content:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```
Now, attach the basic execution policy to this role:

```
awslocal iam attach-role-policy --role-name lambda-execution-role --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```
## Deploy Lambda to LocalStack
Use the AWS CLI to create and deploy your Lambda function to LocalStack. First, zip the Python file into a package:

```
zip function.zip lambda_function.py
```
Now, create the Lambda function using the awslocal CLI tool:

```
awslocal lambda create-function --function-name hello-world \
--zip-file fileb://function.zip --handler lambda_function.lambda_handler \
--runtime python3.8 --role arn:aws:iam::000000000000:role/lambda-execution-role
```

This command will deploy the function to LocalStack's Lambda service.
To invoke the Lambda function programmatically, you can use Boto3 in a Python script.

Create a Python file called invoke_lambda.py:

```

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
```

Run the script:

```
python invoke_lambda.py
```
You should see the following output:

```
Lambda response: {'statusCode': 200, 'body': 'Hello, Panashe!'}
```