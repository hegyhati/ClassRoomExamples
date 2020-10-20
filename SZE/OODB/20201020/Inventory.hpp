#ifndef INVENTORY_HPP
#define INVENTORY_HPP

#include "Sword.hpp"

struct SWLI {
    Sword sword;
    SWLI* next;
}; 

class Inventory {
    public:
        Inventory(int maxweight);
        bool put(Sword sword);
        bool drop(int position);
        int size() const;
        Sword getSword(int position) const;

    private:
        int free_capacity;
        SWLI* swords;

        bool isGoodPosition(int position) const;
        SWLI* getSWLItem(int position) const;
};

#endif
