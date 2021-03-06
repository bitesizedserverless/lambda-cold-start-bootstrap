"""Project setup."""

import setuptools

with open(file="README.md", encoding="utf-8") as fp:
    long_description = fp.read()

setuptools.setup(
    name="Lambda Cold Starts and Bootstrap Code",
    version="0.0.1",
    description="Bite-Sized Serverless: Lambda Cold Starts and Bootstrap Code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bite-Sized Serverless",
    package_dir={"": "lambda_cold_start_bootstrap"},
    packages=setuptools.find_packages(where="lambda_cold_start_bootstrap"),
    install_requires=[
        "aws-cdk.aws_lambda==1.120.0",
        "aws-cdk.aws_s3==1.120.0",
        "aws-cdk.core==1.120.0",
        "black==21.6b0",
        "pylint==2.10.2",
        "python-dotenv==0.17.0",
        "stringcase==1.2.0",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)
