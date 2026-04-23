#include "sort_common.h"


void shaker_sort(int *numbers, int size) {
    int good_small_idx = -1;
    int good_large_idx = size;
    int idx=0;
    while (good_small_idx < good_large_idx) {
        for(;idx<good_large_idx-1;++idx) 
            if (numbers[idx] > numbers[idx+1]) 
                swap(numbers, idx, idx+1);
        --good_large_idx;
        --idx;
        for(;idx>good_small_idx;--idx) 
            if (numbers[idx] > numbers[idx+1]) 
                swap(numbers, idx, idx+1);
        ++good_small_idx;
        ++idx;
    }
}
