#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#include "sorts.h"
#include "test.h"

#define CSV_WIDTH 10

void print_array(const int* const numbers, const int size) {
    for(int i=0; i<size; ++i) printf("%*d ", CSV_WIDTH, numbers[i]);
    printf("\n");
}

int* get_random_array(const int size) {
    srand((unsigned)time(NULL));
    int *data = malloc( size * sizeof *data );
    for(int i=0; i<size; ++i)
        data[i] = rand() % (100 * size + 1);
    return data;
}

bool is_ordered(const int* const numbers, const int size) {
    for (int i = 0; i < size - 1; ++i)
        if (numbers[i+1] < numbers[i])
            return false;
    return true;
}

void test_and_log_algorithms(const algorithm  algorithms[], const size_t algorithm_count, const int sizes[], const size_t size_count){

    char filename[64];
    strftime(filename, sizeof filename, "log_%Y-%m-%d_%H-%M-%S.csv", localtime(&(time_t){ time(NULL) }));
    FILE *f = fopen(filename, "w");

    fprintf(f,"%*s", CSV_WIDTH, "SIZE");
    for (size_t a = 0; a < algorithm_count; ++a) 
        fprintf(f,",%*s",CSV_WIDTH, algorithms[a].name);
    fprintf(f,"\n");

    for (size_t s = 0; s < size_count; ++s) {
        const int size = sizes[s];

        fprintf(f,"%*d", CSV_WIDTH, size);
        
        const int* const original = get_random_array(size);
        int* const data = malloc(size * sizeof *data);


        for (size_t a = 0; a < algorithm_count; ++a) {
            memcpy(data, original, size * sizeof *data);
            
            const clock_t start = clock();
            algorithms[a].function(data,size);
            const clock_t end = clock();
            const double time = (double)(end-start)/CLOCKS_PER_SEC;

            if (is_ordered(data,size)) {            
                fprintf(f,",%*g",CSV_WIDTH, time);
                fflush(f);
                printf("Array of %d elements took %g seconds to be sorted by %s.\n", size, time, algorithms[a].name);
            } else {                        
                fprintf(f,",%*s",CSV_WIDTH, "FAIL");
                fflush(f);
                printf("[FAIL] Array of %d elements was not properly sorted by %s.\n", size, algorithms[a].name);
            }
        }
        fprintf(f,"\n");

        free(data);
        free((void*)original);
    }

    fclose(f);
}