#include <stdio.h>
#include <stdlib.h>


int* read_cli_numbers(int argc, char** argv){
    const int size = argc-1;
    int * numbers = malloc(size * sizeof(int));
    for (int i=0; i<size; ++i)
        numbers[i] = atoi(argv[i+1]);
    return numbers;
}

void print_array(int size, int* numbers) {
    for (int i=0; i<size; ++i)
        printf("%5d", i);
    printf("\n");
    for (int i=0; i<size; ++i)
        printf("%5d", numbers[i]);
    printf("\n");    
}

void swap(int* numbers, int idx1, int idx2) {
    int tmp = numbers[idx1];
    numbers[idx1] = numbers[idx2];
    numbers[idx2] = tmp;
}


void heapify(int heapsize, int* numbers, int parent) {
    while (1) {
        int maxidx = parent;
        int left = 2 * parent + 1;
        int right = 2 * parent + 2;
        if (left < heapsize && numbers[left] > numbers[maxidx]) maxidx = left;
        if (right < heapsize && numbers[right] > numbers[maxidx]) maxidx = right;
        if (maxidx != parent) {
            swap(numbers, parent, maxidx);
            parent = maxidx;
        } else break;
    }
}

void build_heap(int heapsize, int* numbers) {
    for (int i=heapsize/2-1; i>=0; --i) 
        heapify(heapsize, numbers, i);
}

void heap_sort(int size, int* numbers) {
    int heapsize = size;
    build_heap(size,numbers);
    while (heapsize > 0) {
        swap(numbers, 0, heapsize-1);
        --heapsize;
        heapify(heapsize, numbers, 0);
    }
}

int main(int argc, char** argv) {
    const int size = argc-1;
    int* numbers = read_cli_numbers(argc, argv);

    print_array(size, numbers);
    printf("\n");
    heap_sort(size, numbers);
    print_array(size, numbers);
    
    free(numbers);
    return 0;
}