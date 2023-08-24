# Use the official Python 3.9 image from DockerHub
FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libportaudio2 \
    portaudio19-dev \
    python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# This command runs when the container starts
CMD [ "/bin/bash" ]
