#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_cdk_s3.aws_cdk_s3_stack import AwsCdkS3Stack


app = cdk.App()
AwsCdkS3Stack(app, "AwsCdkS3Stack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    # env=cdk.Environment(account='000000000000', region='us-east-1'),
    
    
    #    env={
    #     "account": "000000000000", # Dummy account
    #     "region": "us-east-1"      # Default LocalStack region
    # },
    # endpoint="http://localhost:4566"

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

app.synth()
