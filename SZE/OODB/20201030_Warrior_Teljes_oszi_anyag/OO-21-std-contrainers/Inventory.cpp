#include "Inventory.hpp"

Inventory::Inventory(double weightlimit) : weightlimit(weightlimit) {}

double Inventory::getTotalWeight() const {
  double totalWeight=0;
  for(auto& sword: swords)
    totalWeight+=sword.getWeight();
  return totalWeight;  
}

int Inventory::count() const { return swords.size(); }

bool Inventory::put(const Sword& sword) {
  if(getTotalWeight()+sword.getWeight()>weightlimit) {
    return false;
  } else {
    swords.push_back(sword);
    return true;
  }
}

const Sword& Inventory::get(int index) const { return swords.at(index); }

Sword Inventory::drop(int index) {
  Sword sword(swords.at(index));
  swords.erase(swords.begin()+index);
  return sword;
}

void Inventory::clear(){ swords.clear();}

