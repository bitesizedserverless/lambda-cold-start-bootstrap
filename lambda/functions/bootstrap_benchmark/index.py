"""Function to benchmark the Lambda bootstrap and handler."""

import time
from math import sin, cos, radians


def lambda_handler(_event, context):
    """Run the main lambda function."""
    print("# In handler")
    print(f"** Lambda configured with {context.memory_limit_in_mb} MB of memory")
    benchmark(phase="Handler")
    print("# Handler done")


def benchmark(phase):
    """Run a CPU benchmark and time the results."""
    start_time = time.time()
    bench_cpu()
    print(f"## {phase} - CPU benchmark duration: {time.time() - start_time}")


def bench_cpu():
    """Run a CPU intensive operation using only standard libraries."""
    product = 1.0
    for _ in range(1, 10000, 1):
        for dex in list(range(1, 360, 1)):
            angle = radians(dex)
            product *= sin(angle) ** 2 + cos(angle) ** 2
    return product


print("# In bootstrap")
benchmark(phase="Bootstrap")
