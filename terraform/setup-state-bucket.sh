#!/bin/bash

echo "Creating S3 bucket in Floci for Terraform state..."

aws s3 mb s3://shoplocal-terraform-state \
  --endpoint-url http://localhost:4566 \
  --region us-east-1

echo "Done! Bucket created: shoplocal-terraform-state"
echo "You can now run: terraform init"

