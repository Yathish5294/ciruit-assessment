import requests
import json
import sys

# EC2 Metadata URL
IMDS_BASE_URL = "http://169.254.169.254/latest/meta-data/"

def get_metadata(version):
    headers = {}

    if version == "v2":
        # Requesting a session token for IMDSv2
        token_url = "http://169.254.169.254/latest/api/token"
        token_response = requests.put(token_url, headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"})
        token_response.raise_for_status()
        headers["X-aws-ec2-metadata-token"] = token_response.text

    try:
        instance_id = requests.get(f"{IMDS_BASE_URL}instance-id", headers=headers).text
        instance_type = requests.get(f"{IMDS_BASE_URL}instance-type", headers=headers).text
        availability_zone = requests.get(f"{IMDS_BASE_URL}placement/availability-zone", headers=headers).text

        metadata = {
            "InstanceID": instance_id,
            "InstanceType": instance_type,
            "AvailabilityZone": availability_zone
        }

        print(json.dumps(metadata, indent=4))
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching metadata: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["v1", "v2"]:
        print("Usage: python fetch_ec2_metadata.py <v1|v2>")
        sys.exit(1)

    get_metadata(sys.argv[1])
