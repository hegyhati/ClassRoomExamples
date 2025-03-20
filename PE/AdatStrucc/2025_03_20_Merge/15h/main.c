struct LLItem {
    struct LLItem * next;
    int value;
};


int main(){
    struct LLItem *h1;
    struct LLItem *h2;

    // h1, h2 lista felepitese

    struct LLItem * merged = NULL;
    while (h1 != NULL && h2 != NULL) {
        if (h1->value < h2->value) {
            struct LLItem *newItem = malloc(sizeof(struct LLItem));
            newItem -> value = h1 -> value;
            newItem -> next = NULL;
            
            if (merged == NULL) {
                merged = newItem;
            } else {
                struct LLItem * last = merged;
                while (last->next != NULL)
                    last = last -> next;
                last -> next = newItem; 
            }

            struct LLItem * tmp = h1;
            h1 = h1 -> next;
            free(tmp); 
        } else {
            struct LLItem *newItem = malloc(sizeof(struct LLItem));
            newItem -> value = h2 -> value;
            newItem -> next = NULL;

            if (merged == NULL) {
                merged = newItem;
            } else {
                struct LLItem * last = merged;
                while (last->next != NULL)
                    last = last -> next;
                last -> next = newItem; 
            }

            struct LLItem * tmp = h2;
            h2 = h2 -> next;
            free(tmp); 
        }
    }
    if (h1 == NULL) {
        struct LLItem * last = merged;
        while (last->next != NULL)
            last = last -> next;
        last -> next = h2;
        h2 = NULL;
    } else {
        struct LLItem * last = merged;
        while (last->next != NULL)
            last = last -> next;
        last -> next = h1;
        h1 = NULL;
    }
}