cmake_minimum_required(VERSION 3.10)

# Project name
project(SimpleModel)

# Set the C standard
set(CMAKE_C_STANDARD 99)

# Add the executable for the main program
add_executable(simple_model main_program.c simple_model.c)

# Add the executable for the test program
add_executable(test_simple_model test_simple_model.c simple_model.c)

# Enable testing
enable_testing()

# Add a test
add_test(NAME TestComputeSquare COMMAND test_simple_model)

# Rename the custom target from 'test' to 'run_tests' to avoid conflict with the reserved name
add_custom_target(run_tests
    COMMAND ${CMAKE_CTEST_COMMAND} --output-on-failure
    DEPENDS test_simple_model
)
