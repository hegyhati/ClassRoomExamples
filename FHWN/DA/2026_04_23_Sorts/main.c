#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#include "sorts.h"
#include "test.h"


int main(int argc, char** argv) {
    if ( argc<2 ) return -1;


    // Test selected sorts on argv[1] numbers    
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
    
    memcpy(copy,numbers,size*sizeof(int));
    quick_sort(copy,size);
    printf("QUICK SORT: %s\n", is_ordered(copy,size) ? "OK" : "FAIL");
    print_array(copy,size);
    
    memcpy(copy,numbers,size*sizeof(int));
    wasteful_merge_sort(copy,size);
    printf("WASTEFUL MERGE SORT: %s\n", is_ordered(copy,size) ? "OK" : "FAIL");
    print_array(copy,size);
    
    free(numbers);
    free(copy);


    // Test all algorithms until 10^5
    const int sizes [] = {
        10, 20, 30, 40, 50, 60, 70, 80, 90,
        100, 200, 300, 400, 500, 600, 700, 800, 900,
        1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000,
        10000
    };
    const size_t size_count = sizeof sizes / sizeof *sizes;
    test_and_log_algorithms(all_algorithms, algorithm_count, sizes, size_count);

    // Test existing nlogn algorithms until 10^8
    test_and_log_algorithms((algorithm[]){
            { "Heap sort", heap_sort },
            { "Quick sort", quick_sort },
            { "Wasteful merge sort", wasteful_merge_sort },
        },3,(int[]){10,30,100,300,1000,3000,10000,30000,100000,300000,1000000,3000000,10000000,30000000,100000000},15);

    return 0;
}