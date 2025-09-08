#include <stdlib.h>

int main(int argc, char** argv) {
    int size = atoi(argv[1]);
    int* fibonacci = (int*) malloc (2 * sizeof(int));
    fibonacci[0] = 1;
    fibonacci[1] = 1;
    int current_size = 2;
    for(int i = 0; i < size; ++i) {
        int* f_temp = fibonacci;
        fibonacci = (int*) malloc((current_size+1) * sizeof(int));
        for(int idx=0; idx<current_size; ++idx) {
            fibonacci[idx] = f_temp[idx];
        }
        fibonacci[current_size] = fibonacci[current_size-1] + fibonacci[current_size-2];
        current_size++;
        free(f_temp);
    }
}
