#include "list.hpp"
#include <cstdio>
#include <cstdlib>

LL_item* new_list(){
    return NULL;
}

void push_front(LL_item *&phead, int value){
    LL_item *pnew_item = (LL_item*) malloc(sizeof(LL_item));  
    pnew_item->value = value;
    pnew_item->next = phead;
    phead = pnew_item;
}

void push_increasing(LL_item *&phead, int value) {
    if ( is_empty(phead) || phead->value >= value) {
        push_front(phead,value);
        return;
    }

    LL_item *pcurrent = phead;
    while (1) {
        if (pcurrent -> value < value && ( pcurrent->next == NULL || pcurrent->next->value >= value))
            break;
        pcurrent = pcurrent->next;
    }
    //ide kell beszurni
    LL_item *new_item = (LL_item*) malloc(sizeof(LL_item));
    new_item->value = value;
    new_item->next = pcurrent->next;
    pcurrent->next = new_item;
}

int pop_front(LL_item *&phead){
    if (is_empty(phead)) return -1;
    int value = phead->value;
    LL_item *second = phead->next;
    free(phead);
    phead = second;
    return value;
}

void erase(LL_item *&phead) {
    while (!is_empty(phead))
        pop_front(phead);
}

void debug_list( LL_item * phead) {
    printf("Head of list: %p, length: %d\n Items:\n", phead, length(phead));
    while (phead != NULL) {
        printf(" - LL_item at %p: value: %d, next: %p\n", phead, phead->value, phead->next);
        phead = phead->next;
    }
}

int is_empty(LL_item *phead) {
    return phead == NULL;
}

int length(LL_item *phead){
    int length;
    for(length = 0; phead != NULL; phead=phead->next)
        length++;
    return length;
}


