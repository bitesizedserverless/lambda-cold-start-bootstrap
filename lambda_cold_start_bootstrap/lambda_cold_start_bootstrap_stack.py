"""Module for the main LambdaColdStartsAndBootstrapCode Stack."""

# Standard library imports
# -

# Related third party imports
# -

# Local application/library specific imports
from aws_cdk import core as cdk, aws_lambda as lambda_, aws_s3 as s3


class LambdaColdStartsAndBootstrapCodeStack(cdk.Stack):
    """The LambdaColdStartsAndBootstrapCode Stack."""

    def __init__(
        self,
        scope: cdk.Construct,
        construct_id: str,
        config: dict,
        **kwargs,
    ) -> None:
        """Construct a new LambdaColdStartsAndBootstrapCodeStack."""
        super().__init__(scope, construct_id, **kwargs)

        # Create the bootstrap Lambda function
        self.bootstrap_function = lambda_.Function(
            scope=self,
            id="BootstrapLambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.asset("lambda/functions/bootstrap_benchmark"),
            handler="index.lambda_handler",
            timeout=cdk.Duration.seconds(config["lambda_timeout"]),
        )
        # Create a simple S3 Bucket which will be removed when the CloudFormation
        # stack is deleted.
        demo_s3_bucket = s3.Bucket(
            scope=self, id="DemoBucket", removal_policy=cdk.RemovalPolicy.DESTROY
        )

        # Create a simple S3 Lambda function
        self.simple_s3_function = lambda_.Function(
            scope=self,
            id="SimpleLambdaFunction",
            runtime=lambda_.Runtime.PYTHON_3_8,
            code=lambda_.Code.asset("lambda/functions/s3_hello_world"),
            handler="index.lambda_handler",
            timeout=cdk.Duration.seconds(config["lambda_timeout"]),
            environment={"S3_BUCKET": demo_s3_bucket.bucket_name},
        )

        # Grant the Simple S3 function permissions to write to the S3 bucket
        demo_s3_bucket.grant_write(self.simple_s3_function)
