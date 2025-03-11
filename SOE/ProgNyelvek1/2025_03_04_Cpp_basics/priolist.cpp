#include "priolist.hpp"

PrioList::PrioList(){
    head = nullptr;
}

PrioList::PrioList(const PrioList& other){
    head = nullptr;
    for (LL_item* tmp = other.head; tmp != nullptr; tmp = tmp -> next) {
        push_front(tmp->value); // note: reverse
    }
}


void PrioList::push_front(int value) {
    LL_item *pnew_item = new LL_item;  
    pnew_item->value = value;
    pnew_item->next = head;
    head = pnew_item;
}

bool PrioList::is_empty() const {
    return head == nullptr;
}

void PrioList::push_increasing(int value) {
    if ( is_empty() || head->value >= value) {
        push_front(value);
        return;
    }

    LL_item *pcurrent = head;
    while (1) {
        if (pcurrent -> value < value && ( pcurrent->next == nullptr || pcurrent->next->value >= value))
            break;
        pcurrent = pcurrent->next;
    }
    LL_item *new_item = new LL_item;
    new_item->value = value;
    new_item->next = pcurrent->next;
    pcurrent->next = new_item;
}


int PrioList::pop_front(){
    if (is_empty()) return -1;
    int value = head->value;
    LL_item *second = head->next;
    delete head;
    head = second;
    return value;
}

PrioList::~PrioList() {
    while (!is_empty())
        pop_front();
}

int PrioList::length() const {
    int length = 0;
    for(LL_item* tmp = head; tmp != nullptr; tmp=tmp->next)
        length++;
    return length;
}