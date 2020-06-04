#!/usr/bin/env python
# Python version 3.8+

"""AWS-Cognito-Token
Usage:
    aws-cognito-token.py (--username=STRING --poolid=STRING --appid=STRING)
                         [--password=STRING]
                         [--output=PATH]
                         [--save]

    aws-cognito-token.py (-h | --help)
    aws-cognito-token.py (-v | --version)

Options:
    -h --help           Show this screen.
    -v --version        Show version.
    
    --password=STRING   Specify the password in plaintext.
    --output=PATH       Optional path to write token output to.
    --save              Should credentials be saved

Description:
    Prints Access and ID tokens derived from a AWS Cognito basic authentication.

Requirements:
    Python 3.8+, docopt, boto3
"""

from getpass import getpass

import os

import boto3
from docopt import docopt

def authenticate(username: str, password: str, user_pool_id: str, app_client_id: str) -> None:
    client = boto3.client("cognito-idp")

    resp = client.admin_initiate_auth(
        UserPoolId=user_pool_id,
        ClientId=app_client_id,
        AuthFlow="ADMIN_NO_SRP_AUTH",
        AuthParameters={
            "USERNAME": username,
            "PASSWORD": password
        }
    )

    print("Log in success")
    print("Access token:", resp["AuthenticationResult"]["AccessToken"])
    print("ID token:", resp["AuthenticationResult"]["IdToken"])

def cli():
    args = docopt(__doc__, version="AWS-Cognito-Token 0.1")

    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Handle arguments.
    username = args["--username"]
    pool_id = args["--poolid"]
    app_id = args["--appid"]

    # Handle password either hidden or explicit. 
    password = args["--password"] or getpass("Password: ")

    output = args["--output"] or None

    authenticate(username, password, pool_id, app_id)

if __name__ == "__main__":
    cli()
