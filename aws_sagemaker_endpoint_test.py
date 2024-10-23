import boto3
import json


# Initialize a session using your AWS credentials
session = boto3.Session()
runtime = session.client('sagemaker-runtime', region_name='us-east-2')

# Replace with your endpoint name
endpoint_name = 'simple-model-endpoint'

# Replace 'number' with the actual input you want to test
number = 999999  # Example input

payload = json.dumps({'input_number': number})


# Invoke the endpoint
try:
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,  # Your endpoint name
        ContentType='application/json',  # Assuming your model handles plain text
        Accept='text/plain',  # Expect response in plain text
        Body=payload  # Send the number as a plain string
    )

    # Read and decode the response
    result = response['Body'].read().decode('utf-8')  # Decode response
    print("Prediction result:", result)

except Exception as e:
    print("Error:", str(e))
