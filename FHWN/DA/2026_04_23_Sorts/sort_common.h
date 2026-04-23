#ifndef SORT_COMMON_H
#define SORT_COMMON_H

static inline void swap(int* numbers, int idx1, int idx2) {
    int tmp = numbers[idx1];
    numbers[idx1] = numbers[idx2];
    numbers[idx2] = tmp;
}

#endif