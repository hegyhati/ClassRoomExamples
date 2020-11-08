#include "Sword.hpp"


Sword::Sword(int damage, int durability, double weight) 
: damage(damage), max_durability(durability), current_durability(durability), weight(weight) {}

int Sword::use() {
  if (current_durability>0) {
    --current_durability;
    return damage;
  } else return 0;
}

void Sword::repair() {current_durability=max_durability;}


double Sword::getWeight() const { return weight; }

std::string Sword::toString() const {
  return "Sword DMG: "+std::to_string(damage)
    +" DUR: "+std::to_string(current_durability)+"/"+std::to_string(max_durability)
    +" WEIGHT: "+std::to_string(weight);
}
