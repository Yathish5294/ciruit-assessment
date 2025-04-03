# Use Alpine Linux as base image
FROM alpine:latest

# Install Python and requests library using apk
RUN apk add --no-cache python3 py3-requests

# Set the working directory
WORKDIR .

# Copy script into the container
COPY fetch_EC2_Metadata.py .

# Set the entrypoint
ENTRYPOINT ["python3", "fetch_EC2_Metadata.py"]
