#!/usr/bin/env python3
import os

import aws_cdk as cdk

from adjust_layer_directory import adjust_layer_directory
from iac.certificates_s3_stack import CertificatesS3Stack
from iac.iac_stack import IacStack

print("Starting the CDK")

print("Adjusting the layer directory")
adjust_layer_directory(shared_dir_name="shared", destination="lambda_layer_out_temp")
print("Finished adjusting the layer directory")


app = cdk.App()

aws_region = os.environ.get("AWS_REGION")
aws_account_id = os.environ.get("AWS_ACCOUNT_ID")
stack_name = os.environ.get("STACK_NAME")

IacStack(app, stack_name, env=cdk.Environment(account=aws_account_id, region=aws_region))
CertificatesS3Stack(app, f"{stack_name}-certificates-s3", env=cdk.Environment(account=aws_account_id, region=aws_region))

IacStack.add_dependency(target=CertificatesS3Stack, reason="The certificates bucket and cloundfront distribution are required for the API Gateway")

app.synth()
