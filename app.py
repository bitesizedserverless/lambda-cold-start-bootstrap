#!/usr/bin/env python3
"""The main app. Contains all the stacks."""

# Standard library imports
# -

# Related third party imports
# -

# Local application/library specific imports
from aws_cdk import core as cdk
from config import Config
from lambda_cold_start_bootstrap.lambda_cold_start_bootstrap_stack import (
    LambdaColdStartsAndBootstrapCodeStack,
)

config = Config()

app = cdk.App()
LambdaColdStartsAndBootstrapCodeStack(
    scope=app,
    construct_id="LambdaColdStartsAndBootstrapCodeStack",
    config=config.base(),
)

app.synth()
