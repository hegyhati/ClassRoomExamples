#include <stdlib.h>


int main(int argc, char** argv) {
    int size = atoi(argv[1]);
    int* fibonacci = (int*) malloc ((2 + size) * sizeof(int));
    fibonacci[0] = 1;
    fibonacci[1] = 1;
    for(int i = 2; i < size+2; ++i) {
        fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];
    }
}
