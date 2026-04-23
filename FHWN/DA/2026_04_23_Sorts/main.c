#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#include "sorts.h"
#include "test.h"


int main(int argc, char** argv) {
    if ( argc<2 ) return -1;

    const int size = atoi(argv[1]);
    int *numbers = get_random_array(size);
    int *copy = malloc(size*sizeof *copy);
    print_array(numbers,size);

    memcpy(copy,numbers,size*sizeof(int));
    heap_sort(copy,size);
    printf("HEAP SORT: %s\n", is_ordered(copy,size) ? "OK" : "FAIL");
    print_array(copy,size);
    
    memcpy(copy,numbers,size*sizeof(int));
    shaker_sort(copy,size);
    printf("SHAKER SORT: %s\n", is_ordered(copy,size) ? "OK" : "FAIL");
    print_array(copy,size);
    
    free(numbers);
    free(copy);


    // Test all algorithms on a lot of sizes

    const int sizes [] = {
        10, 20, 30, 40, 50, 60, 70, 80, 90,
        100, 200, 300, 400, 500, 600, 700, 800, 900,
        1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
        10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000,
        // 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000,
        // 1000000
    };
    const size_t size_count = sizeof sizes / sizeof *sizes;
    test_and_log_algorithms(all_algorithms, algorithm_count, sizes, size_count);

    return 0;
}