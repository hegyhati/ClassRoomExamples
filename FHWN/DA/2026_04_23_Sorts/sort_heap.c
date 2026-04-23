#include "sort_common.h"

static inline int parent(int node_idx) { return (node_idx-1)/2; }
static inline int left_child (int node_idx) {return 2*node_idx+1; }
static inline int right_child (int node_idx) {return 2*node_idx+2; }



static inline int fix_triangle(int* numbers, int heapsize, int node_idx) {        
    int max_idx = node_idx;    
    int left_idx = left_child(node_idx);
    int right_idx = right_child(node_idx);
    if ( left_idx < heapsize && numbers[left_idx] > numbers[max_idx] ) max_idx = left_idx;
    if ( right_idx < heapsize && numbers[right_idx] > numbers[max_idx] ) max_idx = right_idx;  
    if (max_idx != node_idx) swap(numbers,node_idx,max_idx);
    return max_idx;
}
void heapify(int* numbers, int heapsize, int node_idx) {
    int max_idx;
    while ( (max_idx = fix_triangle(numbers, heapsize, node_idx)) != node_idx ) {
        node_idx = max_idx;
    }
}

void build_heap(int *numbers, int size) {
    for (int idx = size/2; idx >= 0; --idx) 
        heapify(numbers, size, idx);
}


void heap_sort(int *numbers, int size) {
    build_heap(numbers, size);
    for (int i = 0; i<size; ++i){
        swap(numbers,0,size-1-i);
        heapify(numbers, size-1-i, 0);
    }
}