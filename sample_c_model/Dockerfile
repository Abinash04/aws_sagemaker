# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and the shared object (.so) file into the container
COPY . .

# Install necessary dependencies (for example, build tools)
RUN apt-get update -y && apt-get install -y gcc cmake make

# Set the Python script as the entrypoint
ENTRYPOINT ["python3", "test_model.py"]
