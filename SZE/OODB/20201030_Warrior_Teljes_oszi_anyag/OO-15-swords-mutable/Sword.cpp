#include "Sword.hpp"


Sword::Sword(int damage, int durability) 
: damage(damage), max_durability(durability), current_durability(durability) {}

int Sword::use() {
  if (current_durability>0) {
    --current_durability;
    return damage;
  } else return 0;
}

void Sword::repair() {current_durability=max_durability;}
