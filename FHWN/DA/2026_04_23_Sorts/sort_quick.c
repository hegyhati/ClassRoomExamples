#include "sort_common.h"

int partition(int *numbers, int from_idx, int until_idx) {
    const int pivot = numbers[until_idx];
    int first_not_smaller_idx = from_idx;
    for (int next_idx = from_idx; next_idx < until_idx; ++next_idx)
        if (numbers[next_idx] < pivot) 
            swap(numbers,next_idx,first_not_smaller_idx++);
    swap(numbers,until_idx,first_not_smaller_idx);


    return first_not_smaller_idx;
}

void quick_sort_rec(int *numbers, int from_idx, int until_idx) {
    if ( from_idx >= until_idx ) return;
    int pivot_idx = partition(numbers, from_idx, until_idx);
    quick_sort_rec(numbers, from_idx, pivot_idx-1);
    quick_sort_rec(numbers, pivot_idx+1, until_idx);
}

void quick_sort(int *numbers, int size) {
    quick_sort_rec(numbers, 0, size-1);
}