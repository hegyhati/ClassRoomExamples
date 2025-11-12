#include <stdio.h>

int main() {
    unsigned int number;
    scanf("%u", &number);
    do {
        printf (" -> %u", number);
        if (number%2 == 1) {
            number *= 3;
            ++number;
        } else number /= 2;
    } while (number != 1);
    printf(" -> 1\n");
    return 1;
}