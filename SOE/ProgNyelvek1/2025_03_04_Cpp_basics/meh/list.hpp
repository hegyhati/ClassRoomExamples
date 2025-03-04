struct LL_item {
    int value;
     LL_item *next;
};


LL_item* new_list();
void push_front( LL_item *&phead, int value);
void push_increasing( LL_item *&phead, int value);
int pop_front( LL_item *&phead);
void erase( LL_item *&phead); // free
void debug_list( LL_item *phead);
int is_empty( LL_item *phead);
int length( LL_item *phead);

