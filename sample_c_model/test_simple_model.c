#include <stdio.h>
#include "simple_model.h"

int main() {
    // Test case
    long long test_input = 4;
    long long result = compute_square(test_input);
    printf("Testing square of %lld: %lld\n", test_input, result);

    return 0;
}
