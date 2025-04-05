# Use Alpine Linux as base image
FROM alpine:latest

# Install Python and dependencies, install localstack, clean up
RUN apk add --no-cache \
        python3 py3-pip gcc musl-dev python3-dev libffi-dev openssl-dev make \
    && pip3 install --break-system-packages localstack \
    && apk del gcc musl-dev python3-dev libffi-dev openssl-dev make py3-pip

# Set the working directory
WORKDIR /app

# Copy script into the container
COPY fetch_EC2_Metadata.py .

# Expose localstack default port
EXPOSE 4566

# Default to shell entrypoint
CMD ["/bin/sh"]

