#ifndef INVENTORY_HPP
#define INVENTORY_HPP

#include "Sword.hpp"

class Inventory {
  public:
    class WrongIndexException{};
    
    Inventory();
    double getTotalWeight() const;
    int count() const;
    Sword& get(int index) const;
    void put(const Sword& sword);
    Sword drop(int index);

  private:

    struct InventoryItem {
      Sword sword;
      InventoryItem* next;
    };

    InventoryItem* swords;    

    void checkIndex(int index) const;
};


#endif
