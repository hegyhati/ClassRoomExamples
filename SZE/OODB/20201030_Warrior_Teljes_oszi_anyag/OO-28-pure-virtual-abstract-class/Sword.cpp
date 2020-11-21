#include "Sword.hpp"

Sword::Sword(int damage, int durability, double weight) 
: Wearable(durability,weight), damage(damage) {} 

int Sword::attack() {
  if (isUsable()) {
    use(); 
    return damage;
  } else return 0;
}

std::string Sword::toString() const {
  return "Sword DMG: "+std::to_string(damage)
    +" DUR: "+std::to_string(current_durability)+"/"+std::to_string(max_durability)
    +" WEIGHT: "+std::to_string(getWeight());
}
