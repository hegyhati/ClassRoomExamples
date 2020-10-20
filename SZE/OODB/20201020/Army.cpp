#include "Army.hpp"

Army::Army(): warriors(nullptr) {}

void Army::enlist(Warrior warrior) {
    WLI* new_Warrior = new WLI{warrior,nullptr};
    if (warriors == nullptr) warriors=new_Warrior;
    else {        
        WLI* tmp = warriors;
        while(tmp->next!=nullptr) tmp=tmp->next;
        tmp->next = new_Warrior;
    }
}

int Army::headcount() const {
    int size=0;    
    for(WLI* tmp = warriors; tmp!=nullptr; tmp=tmp->next)  ++ size;
    return size;
}

bool Army::isGoodPosition(int position) const {
    return position >= 0 && position < headcount();
}

WLI* Army::getWLItem(int position) const {
    if (!isGoodPosition(position)) return nullptr;
    WLI* tmp = warriors;
    for(int i=0; i<position; i++) tmp=tmp->next;
    return tmp;
}

Warrior Army::getWarrior(int position) const {
    if (getWLItem(position)==nullptr) return Warrior("",0,0);
    return getWLItem(position)->warrior;
}

bool Army::dismiss(int position) {
    if (!isGoodPosition(position)) return false;
    else {
        if(position==0) {
            warriors=warriors->next;
        }
        else {
            WLI* tmp = getWLItem(position-1);
            tmp->next = tmp->next->next;
        }
        return true;
    }
}
