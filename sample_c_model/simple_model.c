#include "simple_model.h"
#include <stdio.h>
#include <stdlib.h>

// Function to compute the square of a long long integer
long long compute_square(long long num) {
    return num * num;
}

// A function to print the result
void print_result(long long input) {
    long long output = compute_square(input);
    printf("The square of %lld is %lld\n", input, output);
}
