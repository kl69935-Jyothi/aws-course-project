import boto3
import json
import time
from botocore.exceptions import ClientError

# ---------- CONFIG ----------
REGION = "us-east-1"

# Use a unique bucket name every time (timestamp added so it won’t clash)
BUCKET_NAME = f"jyothi-boto3-demo-bucket-{int(time.time())}"

# Your existing Lambda function name
LAMBDA_FUNCTION_NAME = "scalable-arch-stack-UploadLogFunction-5UFhO7wV0tHJ"
# -----------------------------


def create_s3_bucket_and_upload_file():
    """Create an S3 bucket and upload a small test file using Boto3."""
    s3_client = boto3.client("s3", region_name=REGION)

    print(f"\n[1] Creating S3 bucket: {BUCKET_NAME}")
    try:
        # For us-east-1 we don’t need LocationConstraint
        s3_client.create_bucket(Bucket=BUCKET_NAME)
        print("    Bucket created successfully.")
    except ClientError as e:
        # If you re-run the script and the bucket already exists, just continue
        if e.response["Error"]["Code"] == "BucketAlreadyOwnedByYou":
            print("    Bucket already exists and is owned by you, continuing.")
        else:
            print(f"    Error creating bucket: {e}")
            return

    # Create a local file
    file_name = "boto3_test.txt"
    file_content = "This is a Boto3 test file for the course project."
    with open(file_name, "w") as f:
        f.write(file_content)

    print(f"    Uploading file '{file_name}' to bucket '{BUCKET_NAME}'...")
    s3_client.upload_file(file_name, BUCKET_NAME, file_name)
    print("    File uploaded successfully.")


def list_running_ec2_instances():
    """List running EC2 instances with basic metadata."""
    ec2_client = boto3.client("ec2", region_name=REGION)

    print("\n[2] Listing running EC2 instances...")
    response = ec2_client.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )

    running_instances = []

    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            instance_id = instance.get("InstanceId")
            instance_type = instance.get("InstanceType")
            state = instance.get("State", {}).get("Name")
            public_ip = instance.get("PublicIpAddress")
            az = instance.get("Placement", {}).get("AvailabilityZone")

            running_instances.append(
                {
                    "InstanceId": instance_id,
                    "InstanceType": instance_type,
                    "State": state,
                    "PublicIp": public_ip,
                    "AvailabilityZone": az,
                }
            )

    if not running_instances:
        print("    No running instances found.")
    else:
        for i, inst in enumerate(running_instances, start=1):
            print(
                f"    {i}. ID={inst['InstanceId']}, "
                f"Type={inst['InstanceType']}, "
                f"State={inst['State']}, "
                f"PublicIP={inst['PublicIp']}, "
                f"AZ={inst['AvailabilityZone']}"
            )

    return running_instances


def retrieve_ec2_metadata():
    """
    Retrieve EC2 'metadata' using Boto3 (instance attributes).
    This works even when running the script from your laptop.
    """
    ec2_client = boto3.client("ec2", region_name=REGION)

    print("\n[3] Retrieving EC2 metadata via describe_instances...")

    response = ec2_client.describe_instances()
    for reservation in response.get("Reservations", []):
        for instance in reservation.get("Instances", []):
            instance_id = instance.get("InstanceId")
            instance_type = instance.get("InstanceType")
            state = instance.get("State", {}).get("Name")
            private_ip = instance.get("PrivateIpAddress")
            public_ip = instance.get("PublicIpAddress")
            az = instance.get("Placement", {}).get("AvailabilityZone")
            launch_time = str(instance.get("LaunchTime"))

            print(f"    Instance ID: {instance_id}")
            print(f"      Type:      {instance_type}")
            print(f"      State:     {state}")
            print(f"      PrivateIP: {private_ip}")
            print(f"      PublicIP:  {public_ip}")
            print(f"      AZ:        {az}")
            print(f"      Launched:  {launch_time}\n")


def invoke_lambda_function():
    """Invoke the S3-logging Lambda function using Boto3."""
    lambda_client = boto3.client("lambda", region_name=REGION)

    print(f"\n[4] Invoking Lambda function: {LAMBDA_FUNCTION_NAME}")

    # Build a small S3-style event similar to the console test
    test_event = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": BUCKET_NAME},
                    "object": {"key": "boto3_test.txt", "size": 123},
                }
            }
        ]
    }

    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType="RequestResponse",
            Payload=json.dumps(test_event),
        )
        print("    Lambda invoke status code:", response.get("StatusCode"))

        payload_bytes = response["Payload"].read()
        payload_str = payload_bytes.decode("utf-8")
        print("    Lambda response payload:", payload_str)
    except ClientError as e:
        print(f"    Error invoking Lambda: {e}")


def main():
    print("=== AWS Interaction via Python Boto3 ===")
    create_s3_bucket_and_upload_file()
    list_running_ec2_instances()
    retrieve_ec2_metadata()
    invoke_lambda_function()
    print("\nAll Boto3 operations completed.")


if __name__ == "__main__":
    main()
