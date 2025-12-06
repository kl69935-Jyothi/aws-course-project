# AWS Course Project

This project deploys a scalable AWS architecture using Terraform, CloudFormation, and Python Boto3.

---

## Architecture Components

- VPC with public + private subnets
- Application Load Balancer
- EC2 Auto Scaling Group
- Amazon RDS
- S3 Bucket
- Lambda function (triggered by S3)
- CloudWatch logging

---

## Repository Structure

terraform/
cloudformation/
boto3/
aws-architecture.png

---

## How to Deploy (Terraform)

1. Open terminal
2. Go to terraform folder

    cd terraform

3. Run

    terraform init
    terraform plan
    terraform apply

---

## How to Deploy (CloudFormation)

1. Open AWS Console
2. Go to CloudFormation
3. Click “Create stack”
4. Upload infra.yml
5. Click Deploy

---

## Run Python (Boto3 Scripts)

1. Install boto3:

    pip install boto3

2. Run script:

    python boto3/aws_interaction.py

---

## Architecture Diagram

See file: aws-architecture.png

---

## Security Groups

Security Groups control network access for ALB, EC2, and RDS.

---

## Auto Scaling

EC2 instances automatically scale inside private subnet.

---

## Infrastructure as Code

Terraform = networking and compute  
CloudFormation = higher level deployment

---

## Version Control

✔ GitHub repository  
✔ Regular commits  
✔ Incremental progress

GitHub:
https://github.com/kl69935-Jyothi/aws-course-project
