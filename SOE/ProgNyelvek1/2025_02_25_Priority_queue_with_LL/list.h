struct LL_item {
    int value;
    struct LL_item *next;
};

struct LL_item* new_list();
void push_front(struct LL_item **pphead, int value);
void push_increasing(struct LL_item **pphead, int value);
int pop_front(struct LL_item **pphead);
void erase(struct LL_item **pphead); // free
void debug_list(struct LL_item *phead);
int is_empty(struct LL_item *phead);
int length(struct LL_item *phead);

