#include "uint_list.h"
#include "stdlib.h"

bool hasItem(LLNode *head, unsigned item) {
    while (head != NULL)
        if (head->item == item)
            return true;
        else
            head = head->next;
    return false;
}

bool addItem(LLNode **phead, unsigned item, bool unique) {
    if (unique && hasItem(*phead, item)) return false;
    LLNode *tmp = (LLNode *)malloc(sizeof(LLNode));
    tmp->item = item;
    tmp->next = (*phead);
    *phead = tmp;
    return true;
}

void freeList(LLNode **phead) {
    LLNode *tmp;
    while (*phead != NULL) {
        tmp = *phead;
        (*phead) = (*phead)->next;
        free(tmp);
    }
}