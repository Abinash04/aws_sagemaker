import sys
import ctypes
from flask import Flask, request, Response, jsonify

# Load the shared object file
lib = ctypes.CDLL("./simple_model.so")

# Define the argument and return types for the compute_square function
lib.compute_square.argtypes = [ctypes.c_longlong]
lib.compute_square.restype = ctypes.c_longlong

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    status = 200
    return Response(response="Healthy", status=status, mimetype='text/plain')

@app.route('/invocations', methods=['POST'])
def predict():
    try:
        data = request.get_json()  # Get JSON data
        input_number = data['input_number']  # Extract the input number
        result = lib.compute_square(input_number)  # Call the C function
        return jsonify({f"Square of {input_number}": result})  # Return the result as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)  # Run Flask app
