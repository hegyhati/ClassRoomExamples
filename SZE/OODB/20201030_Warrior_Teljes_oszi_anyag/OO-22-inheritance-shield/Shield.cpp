#include "Shield.hpp"


Shield::Shield(int defense, int durability, double weight) 
: Wearable(durability), defense(defense), weight(weight) {}

int Shield::defend() {
  if (isUsable()) {
    use();
    return defense;
  } else return 0;
}

double Shield::getWeight() const { return weight; }

std::string Shield::toString() const {
  return "Shield DEF: "+std::to_string(defense)
    +" DUR: "+std::to_string(current_durability)+"/"+std::to_string(max_durability)
    +" WEIGHT: "+std::to_string(weight);
}
