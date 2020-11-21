#include "Sword.hpp"


Sword::Sword(int damage, int durability, double weight) 
: Wearable(durability), damage(damage), weight(weight) {}

int Sword::attack() {
  if (isUsable()) {
    use(); 
    return damage;
  } else return 0;
}

double Sword::getWeight() const { return weight; }

std::string Sword::toString() const {
  return "Sword DMG: "+std::to_string(damage)
    +" DUR: "+std::to_string(current_durability)+"/"+std::to_string(max_durability)
    +" WEIGHT: "+std::to_string(weight);
}
