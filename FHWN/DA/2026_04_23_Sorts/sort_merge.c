#include <string.h>
#include <stdlib.h>

int* merge(int* sorted1, int size1, int* sorted2, int size2) {
    int* result = malloc( (size1+size2) * sizeof *result);
    int next1 = 0, next2 = 0, next = 0;
    while ( next < size1+size2 ){
        if (next1 == size1) result[next++] = sorted2[next2++];
        else if (next2 == size2 || sorted1[next1]<sorted2[next2]) result[next++] = sorted1[next1++];
        else result[next++] = sorted2[next2++];
    }
    free(sorted1);
    free(sorted2);
    return result;
}

typedef struct {
    int* left;
    int left_size;
    int* right;
    int right_size;
} array_pair;

array_pair split (int* numbers, int size) {
    array_pair lr;
    lr.left_size = size/2;
    lr.right_size = size - lr.left_size;
    lr.left = malloc(lr.left_size * sizeof *lr.left);
    lr.right = malloc(lr.right_size * sizeof *lr.right);
    memcpy(lr.left,numbers,lr.left_size * sizeof *lr.left);
    memcpy(lr.right,numbers+lr.left_size,lr.right_size * sizeof *lr.right);
    free(numbers);
    return lr;
}

int* wasteful_merge_sort_rec(int* numbers, int size) {
    if (size < 2) return numbers;
    array_pair lr = split(numbers, size);
    return merge(
        wasteful_merge_sort_rec(lr.left, lr.left_size),lr.left_size,
        wasteful_merge_sort_rec(lr.right,lr.right_size),lr.right_size
    );
}

void wasteful_merge_sort(int *numbers, int size) {
    int* copy = malloc (size * sizeof *copy);
    memcpy(copy, numbers, size * sizeof *copy);
    copy = wasteful_merge_sort_rec(copy, size);
    memcpy(numbers, copy, size * sizeof *copy);
    free(copy);
}
