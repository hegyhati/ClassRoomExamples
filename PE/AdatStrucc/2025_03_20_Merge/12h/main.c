struct LLItem{
    struct LLItem *next;
    int value;
};


int main() {
    struct LLItem *h1;
    struct LLItem *h2;

    // ket lista feltoltese

    struct LLItem *merged = NULL;
    struct LLItem *last;

    while (h1!=NULL && h2!=NULL) {
        if (h1->value < h2->value) {
            if (merged == NULL) {
                merged = h1; 
                last = h1;
            } else {
                last -> next = h1;
                last = last -> next;
            }
            h1 = h1 -> next;
        } else {            
            if (merged == NULL) {
                merged = h2; 
                last = h2;
            } else {
                last -> next = h2;
                last = last -> next;
            }
            h2 = h2 -> next;
        }
    }

}

// TODO 
// edge case
// final merge if one is empty