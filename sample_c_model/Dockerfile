# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

COPY requirements.txt .

# Install necessary dependencies (for example, build tools)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script and the shared object (.so) file into the container
COPY simple_model.so .
COPY main_program.py .

EXPOSE 8080

# Set the Python script as the entrypoint
ENTRYPOINT ["python3", "main_program.py"]
