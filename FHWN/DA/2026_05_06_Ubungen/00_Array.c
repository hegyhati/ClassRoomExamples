/*

It is often cumbersome to always pass the size of an array with the pointer. 
Moreover, if a function should return a new array, it cannot return both of them.

Design the struct and implement the functions in such a way, that main should work.

Then move these into an Array.h so that it can be reused by later exercises.

*/


typedef struct Array {
    // TODO
} Array;

Array new_array(int size){
    // todo
}

int get_value(Array array, int idx) {
    // todo
}

void set_value(Array array, int idx, int value) {
    // todo
}

void delete_array(Array* parray) {
    // todo
}

void print_array(Array array) {
    // todo
}

Array copy_array(Array array) {
    // todo
}

Array slice_array(Array array, int left_idx, int right_idx) {
    // todo
}

// why are we passing pointer to the delete function?

# define SIZE 10

int main() {
    Array f = new_array(SIZE);
    set_value(f,0,1);
    set_value(f,1,1);
    for (int i=2; i<SIZE; ++i)
        set_value(f,i,get_value(f,i-1)+get_value(f,i-2));
    Array f2 = copy_array(f);
    Array half = slice_array(f,0,SIZE/2);
    delete_array(&f);
    delete_array(&f2);
    delete_array(&half);    
}