#include "Inventory.hpp"

Inventory::Inventory(int maxweight) : free_capacity(maxweight), swords(nullptr) {}

bool Inventory::put(Sword sword) {
    if(sword.getWeight() > free_capacity) return false;
    else {
        free_capacity-=sword.getWeight();
        SWLI* new_sword = new SWLI{sword,nullptr};
        if (swords == nullptr) swords=new_sword;
        else {        
            SWLI* tmp = swords;
            while(tmp->next!=nullptr) tmp=tmp->next;
            tmp->next = new_sword;
        }
        return true;
    }
}

int Inventory::size() const {
    int size=0;    
    for(SWLI* tmp = swords; tmp!=nullptr; tmp=tmp->next)  ++ size;
    return size;
}

bool Inventory::isGoodPosition(int position) const {
    return position >= 0 && position < size();
}

SWLI* Inventory::getSWLItem(int position) const {
    if (!isGoodPosition(position)) return nullptr;
    SWLI* tmp = swords;
    for(int i=0; i<position; i++) tmp=tmp->next;
    return tmp;
}

Sword Inventory::getSword(int position) const {
    if (getSWLItem(position)==nullptr) return Sword(0,0);
    return getSWLItem(position)->sword;
}

bool Inventory::drop(int position) {
    if (!isGoodPosition(position)) return false;
    else {
        if(position==0) {
            free_capacity += swords->sword.getWeight();
            swords=swords->next;
        }
        else {
            SWLI* tmp = getSWLItem(position-1);
            free_capacity += tmp->next->sword.getWeight();
            tmp->next = tmp->next->next;
        }
        return true;
    }
}
