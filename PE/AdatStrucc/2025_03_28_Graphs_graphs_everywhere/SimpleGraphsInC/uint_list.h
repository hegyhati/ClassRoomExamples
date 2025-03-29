#ifndef UINT_LIST_H
#define UINT_LIST_H

typedef struct LLNode {
    unsigned item;
    struct LLNode *next;
} LLNode;

bool hasItem(LLNode *head, unsigned item);
bool addItem(LLNode **phead, unsigned item, bool unique);
void freeList(LLNode **phead);

#endif