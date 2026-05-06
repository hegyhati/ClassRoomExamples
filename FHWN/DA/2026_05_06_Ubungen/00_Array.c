/*

It is often cumbersome to always pass the size of an array with the pointer. 
Moreover, if a function should return an array, it cannot return both of them.

Make a header file, that provides a struct and some associated functions for later use, that can make our lives easier.

*/


typedef struct Array {
    // TODO
} Array;

Array new_array(int size){
    // todo
}

void delete_array(Array* parray) {
    // todo
}

Array copy(Array array) {
    // todo
}

Array slice(Array array, int left_idx, int right_idx)- {
    // todo
}

// why are we passing pointer to the delete function?