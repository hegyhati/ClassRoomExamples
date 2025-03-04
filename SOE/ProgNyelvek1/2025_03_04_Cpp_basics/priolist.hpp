struct PrioList{
    struct LL_item {
        int value;
        LL_item* next;
    };
    
    LL_item* head;

    PrioList();
    ~PrioList();

    void push_front(int value);
    bool is_empty() const;
    void push_increasing(int value);
    int pop_front();
    void debug_list() const;
    int length() const ;
};