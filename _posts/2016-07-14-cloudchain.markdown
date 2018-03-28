---
layout: post
title: cloudchain
date: 2016-07-14 07:45:09
tags: sysadmin, aws, work
---

Today, the team I'm a part of at TargetSmart is releasing our [first open source project][1], a bit of Python I like to call "cloudchain". cloudchain is designed to make it easy to store and retrieve secrets using AWS. cloudchain relies on the AWS Identity and Access Management (IAM) [Key Management Service][2] (KMS) to securely store and manage access to encryption keys, and stores the encrypted secret in a [DynamoDB][3] table.

Part of the reason, if not the biggest reason, we are open sourcing this project is to request feedback from the community. cloudchain itself is only a few lines of glue plugging together a few AWS services, but its *the idea itself* that I'd like vetted. We are using this in a few projects internally, and so far it's worked out. However, I know that there are things I haven't thought of, and ways to improve the process, so I'm hoping others will be able to look at the project with fresh eyes and see things we haven't. 

There are three steps in the process. First, cloudchain retrieves an encryption key from KMS and uses it to encrypt the plain text secret. The boto3 library used returns a dictionary with a "Ciphertext" entry containing the encrypted key. cloudchain then base64 encodes the encrypted key into a string, and saves that string to a DynamoDB table named, by default, "safedb". 

## Setup

`pip install cloudchain`

A new encryption key should be created in KMS. Using the console makes this easy, and sets up permissions to the key using IAM users or Roles. IAM users should be given permission individually, while instances launching in AWS should be identified by a role. 

A new DynamoDB table should be created as well. Run this command using the AWS CLI tools:


	aws dynamodb create-table \
	--table-name safedb \
	--attribute-definitions \
	AttributeName=Service,AttributeType=S \
	AttributeName=Username,AttributeType=S \
	--key-schema \
	AttributeName=Service,KeyType=HASH \
	AttributeName=Username,KeyType=RANGE \
	--provisioned-throughput \
	ReadCapacityUnits=1,WriteCapacityUnits=1 



This will create the DynamoDB table with two attributes: Service and Username. cloudchain assumes that the combination of a service and a username will require a unique secret. The first time a secret is written to the table the third "Secret" attribute is created. 

## Configuration

The cloudchain cli, `cchain`, looks for a configuration file at `~/.cchainrc`. This should be a standard Python ConfigParser compatible file with the following format:

	[dynamo]
	region_name = us-east-1
	endpoint_url = https://dynamodb.us-east-1.amazonaws.com
	tablename = safedb

	[IAMKMS]
	keyalias = alias/key

The "keyalias" should be the name of the KMS encryption key created during the setup, prefixed by "alias/". The "endpoint_url" should point at the closest HTTPS endpoint, or at localhost if using a local development environment. 

## Import cloudchain as a Module

Both the `test.py` unit tests and the `cchain` cli import `cloudchain.py`. After importing, cloudchain expects four variables to be set:

* region_name
* endpoint_url
* tablename 
* keyalias

Reasonable defaults are mentioned in the configuration section above, but the `keyalias` must be unique. 

After importing, cloudchain can be called on to encrypt and decrypt secrets:

To Encrypt:

`cloudchain.savecreds(args['service'], args['user'], args['save'])`

To Decrypt: 
`cloudchain.readcreds(args['service'], args['user'])`

Where:

* service = The service name the username and secret are associated with
* user = The username
* save = The unencrypted secret to encrypt

## Command Line Use

The command line script supports five arguments:

	  -h, --help            show this help message and exit
	  -u USER, --user USER  User name
	  -e SERVICE, --service SERVICE
							Service or application
	  -s SAVE, --save SAVE  Save password to the safe
	  -r, --read            Read password from the safe


* The `--save` and `--read` arguments are mutually exclusive, and cannot be used at the same time. 
* `--save` expects the unencrypted secret as an argument, and requires both `--user` and `--service` flags.
* `--user` expects the username as an argument.
* `--service` expects the service name as an argument.
* `--read` requires no arguments, and requires both `--user` and `--service` flags.



### Examples

To save a secret:

`./cchain -u testuser --service testservice --save testsecreet` 

To retrieve a secret:

`./cchain -u testuser --service testservice --read`


We hope this is useful, and that we can continue to make cloudchain better, easier to use, and more secure as development continues. 


[1]: https://github.com/targetsmart-devops/cloudchain
[2]: https://aws.amazon.com/kms/?tag=duckduckgo-osx-20
[3]: https://aws.amazon.com/dynamodb/
