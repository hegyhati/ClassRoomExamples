#ifndef SORTS_H
#define SORTS_H

// O(n^2)
void shaker_sort(int *numbers, int size);
void bubble_sort(int *numbers, int size);
void insertion_sort(int *numbers, int size);
void selection_sort(int *numbers, int size);

// O(nlogn)
void heap_sort(int *numbers, int size);
void quick_sort(int *numbers, int size);
void merge_sort(int *numbers, int size);
void wasteful_merge_sort(int *numbers, int size);


typedef void (*sort_function)(int*, int);

typedef struct {
    const char* name;
    sort_function function;
} algorithm;

static const algorithm all_algorithms[] = {
    { "Heap sort", heap_sort },
    { "Shaker sort", shaker_sort },
    { "Bubble sort", bubble_sort },
    { "Insertion sort", insertion_sort },
    { "Selection sort", selection_sort },
    { "Quick sort", quick_sort },
    { "Merge sort", merge_sort },
    { "Wasteful merge sort", wasteful_merge_sort },
};

static const int algorithm_count = sizeof(all_algorithms) / sizeof(all_algorithms[0]);

#endif