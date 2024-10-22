# test_model.py

import sys
import ctypes

# Load the shared object file
lib = ctypes.CDLL("./simple_model.so")

# Define the argument and return types for the compute_square function
lib.compute_square.argtypes = [ctypes.c_longlong]
lib.compute_square.restype = ctypes.c_longlong

def compute_square_in_c(input_number):
    result = lib.compute_square(input_number)
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python your_python_script.py <integer>")
        sys.exit(1)

    # Convert the command-line argument to a long long integer
    input_number = int(sys.argv[1])

    # Call the C function and print the result
    result = compute_square_in_c(input_number)
    print(f"The square of {input_number} is {result}")
