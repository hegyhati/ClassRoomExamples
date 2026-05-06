/*

Same thing, but the signatures are different

*/


typedef struct Array {
    // TODO
} Array;


Array new_array(int size){
    // todo
}

int get(const Array* const parray, int idx) {
    // todo
}

void set(Array* const parray, int idx, int value) {
    // todo
}

void delete(Array* const parray) {
    // todo
}

void print(const Array* const parray) {
    // todo
}

Array copy(const Array* const parray) {
    // todo
}

Array slice(const Array* const array, int left_idx, int right_idx) {
    // todo
}

// why are we passing pointer to the delete function?

# define SIZE 10

int main() {
    Array f = new_array(SIZE);
    set(&f,0,1);
    set(&f,1,1);
    for (int i=2; i<SIZE; ++i)
        set(&f,i,get(&f,i-1)+get(&f,i-2));
    Array f2 = copy(&f);
    Array half = slice(&f,0,SIZE/2);
    delete_array(&f);
    delete_array(&f2);
    delete_array(&half);    
}