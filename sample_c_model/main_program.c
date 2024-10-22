#include <stdio.h>
#include <stdlib.h>
#include "simple_model.h"

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <integer>\n", argv[0]);
        return 1;
    }

    long long input = atoll(argv[1]);
    print_result(input);

    return 0;
}
