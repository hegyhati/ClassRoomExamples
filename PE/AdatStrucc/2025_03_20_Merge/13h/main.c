struct LLItem{
    struct LLItem *next;
    int value;
};


int main() {
    struct LLItem *h1;
    struct LLItem *h2;

    // ket lista feltoltese

    struct LLItem *merged;

    while(h1!=NULL && h2!= NULL) {
        if (h1 -> value < h2 -> value) {
            // merged vegere h1-et
            if (merged == NULL) {
                merged = h1;
                h1 = h1 -> next;
                merged -> next = NULL;
            } else {
                struct LLItem *tmp = merged;
                while(tmp->next != NULL)
                    tmp = tmp -> next;
                tmp->next = h1;
                h1 = h1 -> next;
                tmp->next->next = NULL;
            }
        } else {
            //merged vegere h2-t
            h2 = h2 -> next;
        }
    }
    if (h1 == NULL) {
        // h2 befuzese a vegere
    } else {
        // h1 befuzese a vegere
    }
}