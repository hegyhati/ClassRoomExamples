#ifndef TEST_H
#define TEST_H

#include <stdlib.h>
#include <stdbool.h>
#include "sorts.h"


void print_array(const int* const numbers, const int size);
int* get_random_array(const int size);
bool is_ordered(const int* const numbers, const int size);

void test_and_log_algorithms(const algorithm  algorithms[], const size_t algorithm_count, const int sizes[], const size_t size_count);


#endif 