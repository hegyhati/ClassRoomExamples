#include "list.h"
#include <stdio.h>
#include <stdlib.h>

struct LL_item* new_list(){
    return NULL;
}

void push_front(struct LL_item **pphead, int value){
    struct LL_item *pnew_item = malloc(sizeof(struct LL_item));  
    pnew_item->value = value;
    pnew_item->next = (*pphead);
    (*pphead) = pnew_item;
}

void push_increasing(struct LL_item **pphead, int value) {
    if ( is_empty(*pphead) || (*pphead)->value >= value) {
        push_front(pphead,value);
        return;
    }

    struct LL_item *pcurrent = (*pphead);
    while (1) {
        if (pcurrent -> value < value && ( pcurrent->next == NULL || pcurrent->next->value >= value))
            break;
        pcurrent = pcurrent->next;
    }
    //ide kell beszurni
    struct LL_item *new_item = malloc(sizeof(struct LL_item));
    new_item->value = value;
    new_item->next = pcurrent->next;
    pcurrent->next = new_item;
}

int pop_front(struct LL_item **pphead){
    if (is_empty(*pphead)) return -1;
    int value = (*pphead)->value;
    struct LL_item *second = (*pphead)->next;
    free(*pphead);
    (*pphead) = second;
    return value;
}

void erase(struct LL_item **pphead) {
    while (!is_empty(*pphead))
        pop_front(pphead);
}

void debug_list(struct LL_item *phead){
    printf("Head of list: %p, length: %d\n Items:\n", phead, length(phead));
    while (phead != NULL) {
        printf(" - LL_item at %p: value: %d, next: %p\n", phead, phead->value, phead->next);
        phead = phead->next;
    }
}

int is_empty(struct LL_item *phead) {
    return phead == NULL;
}

int length(struct LL_item *phead){
    int length;
    for(length = 0; phead != NULL; phead=phead->next)
        length++;
    return length;
}


