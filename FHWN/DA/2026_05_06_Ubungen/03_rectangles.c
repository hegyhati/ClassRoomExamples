/*

The same as before, but implement a single comparison based sorting algorithm (something different from the previous 2), that expects a comparator function pointer.

comparators should return -1 if the first argument is smaller, 0 if equal, and +1 if the right argument is smaller

*/

struct Rectangle {
    // todo
};

int area_comparator(struct Rectangle r, struct Rectangle r2) {
    // todo
}

int circumference_comparator(struct Rectangle r, struct Rectangle r2) {
    // todo
}

void sort(struct Rectangle* rectangles, int count, int(* comparator)(struct Rectangle*,struct Rectangle*)) {
    // todo
}

int main() {
    // todo

    sort(rectangles, n, area_comparator);
    sort(rectangles, n, circumference_comparator);
}