#include "Inventory.hpp"

Inventory::Inventory() : swords(nullptr) {}

double Inventory::getTotalWeight() const {
  double totalWeight=0;
  for(InventoryItem* tmp=swords;tmp!=nullptr; tmp=tmp->next) totalWeight+=tmp->sword.getWeight();
  return totalWeight;
  
}

int Inventory::count() const {
  int count=0;  
  for(InventoryItem* tmp=swords;tmp!=nullptr; tmp=tmp->next) count++;
  return count;
}

void Inventory::put(const Sword& sword) {
  swords = new InventoryItem{sword,swords};
}

Sword& Inventory::get(int index) const {
  if (index<0 || index>=count()) throw WrongIndexException();
  InventoryItem* tmp;
  for(tmp=swords;index>0;--index) tmp=tmp->next;
  return tmp->sword;
}

Sword Inventory::drop(int index) {return Sword(0,0,0);}
