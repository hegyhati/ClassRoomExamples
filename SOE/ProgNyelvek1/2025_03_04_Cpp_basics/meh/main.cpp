#include <cstdio>
#include "list.hpp"


void test_ll () {
    LL_item *phead = new_list(); 

    push_front(phead,3);
    debug_list(phead);

    push_front(phead,4);
    debug_list(phead);

    push_front(phead,5);
    debug_list(phead);

    printf("pop element: %d", pop_front(phead));
    debug_list(phead);
    printf("pop element: %d", pop_front(phead));
    debug_list(phead);    

    erase(phead);
}


void test_priority_queue () {
    LL_item *priority_queue = new_list();
    debug_list(priority_queue);
    int number;
    do {
        printf("Add meg a kovetkezo szamot: ");
        scanf("%d", &number);
        push_increasing(priority_queue, number);
        debug_list(priority_queue);
    } while (number != 0);

    while (! is_empty(priority_queue)) {
        number = pop_front(priority_queue);
        printf("%d\n",number);
    }

    erase(priority_queue);
}

int main(){
    //test_ll();
    test_priority_queue();
    return 0;
}
