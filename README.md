# Bite-Sized Serverless: Lambda Cold Starts and Bootstrap Code

This project contains the infrastructure used in the article Lambda Cold Starts and Bootstrap Code on Bite-Sized Serverless: https://bitesizedserverless.com/bite/lambda-cold-start-bootstrap/

The compiled CloudFormation files can be found in the `cdk.out` folder. The Python files for the Lambda functions are placed in `lambda/functions`.

To compile the CloudFormation templates yourself, follow these steps:

1. First create a `virtualenv` with `python3 -m venv .venv`.
2. Then activate the `virtualenv` with `source .venv/bin/activate`.
3. Next, install the required Python packages by running `pip install -r requirements.txt`
4. Then compile CloudFormation by running `cdk synth`. The output will be stored in `cdk.out`.

To deploy the templates, set your preferred region in `.env.aws` and your AWS Account ID in `.env.aws.dev`. Then run a `cdk deploy`.
