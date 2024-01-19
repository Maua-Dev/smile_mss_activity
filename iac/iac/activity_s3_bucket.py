import os


from aws_cdk import (
    # Duration,
    CfnOutput, Stack, aws_cognito,
    aws_cloudfront,
    # aws_sqs as sqs,
    aws_iam,
    aws_cloudfront_origins,
    aws_s3,
    RemovalPolicy,
    aws_iam as iam,
)
from constructs import Construct

class ActivityS3Bucket(Construct):
    def __init__(self, scope: Construct) -> None:
        super().__init__(scope, "Activity_S3_Bucket")

        self.github_ref = os.environ.get("GITHUB_REF")
        self.aws_region = os.environ.get("AWS_REGION")
        self.aws_account_id = os.environ.get("AWS_ACCOUNT_ID")

        REMOVAL_POLICY = RemovalPolicy.RETAIN if 'prod' in self.github_ref else RemovalPolicy.DESTROY

        self.s3_bucket = aws_s3.Bucket(self, "Smile_Activities_S3_Bucket",
                                       versioned=True,
                                       block_public_access=aws_s3.BlockPublicAccess.BLOCK_ALL,
                                       event_bridge_enabled=False,
                                       removal_policy=REMOVAL_POLICY
                                       )

        oai = aws_cloudfront.OriginAccessIdentity(self, "Smile_Activities_OAI")
        
        self.cloudfront_distribution = aws_cloudfront.Distribution(self, "Smile_Activities_CloudFront_Distribution",
                                                                                default_behavior=aws_cloudfront.BehaviorOptions(
                                                                                    origin=aws_cloudfront_origins.S3Origin(
                                                                                        self.s3_bucket,
                                                                                        origin_access_identity=oai),
                                                                                    origin_request_policy=aws_cloudfront.OriginRequestPolicy.CORS_S3_ORIGIN,
                                                                                    viewer_protocol_policy=aws_cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
                                                                                    response_headers_policy=aws_cloudfront.ResponseHeadersPolicy.CORS_ALLOW_ALL_ORIGINS,
                                                                                    cache_policy=aws_cloudfront.CachePolicy.CACHING_OPTIMIZED,
                                                                                    allowed_methods=aws_cloudfront.AllowedMethods.ALLOW_ALL
                                                                                )
                                                                    )

        policy_statement = iam.PolicyStatement(
                            actions=["s3:GetObject"],
                            resources=[f"{self.s3_bucket.bucket_arn}/*.csv"],
                            principals=[iam.CanonicalUserPrincipal(oai.cloud_front_origin_access_identity_s3_canonical_user_id)],
                        )
        
        self.s3_bucket.add_to_resource_policy(policy_statement)

        CfnOutput(self, f"ActivityBucketName",
                       value=self.s3_bucket.bucket_name,
                       export_name=f"ActivityBucketNameValue2024")

        CfnOutput(self, f"ActivityBucketCdnUrl",
            value=f"https://{self.cloudfront_distribution.distribution_domain_name}",
            export_name=f"ActivityBucketCdnUrlValue2024")

        CfnOutput(self, 'S3RemovalPolicy',
                  value=REMOVAL_POLICY.value,
                  export_name='S3RemovalPolicyValue2024')