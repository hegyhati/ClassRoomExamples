#include <iostream>
#include "priolist.hpp"

void PrioList::debug_list() const {
    std::cout << "Head of list: "<< head << "length: " << length() << "\n";
    for (LL_item *tmp  = head; tmp != nullptr; tmp = tmp -> next) {
        std::cout << " - LL_item at " << tmp << " value: " << tmp->value << " next: " << tmp -> next << "\n";
    }
}
