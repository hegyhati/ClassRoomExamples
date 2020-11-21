#include "Wearable.hpp"


Wearable::Wearable(int max_durability, double weight) 
      : Item(weight), max_durability(max_durability), current_durability(max_durability) { }


void Wearable::repair() { 
  if(!isUsable() && max_durability>0) 
    max_durability--; 
  current_durability = max_durability; 
}

bool Wearable::isUsable() const {return current_durability>0;}
void Wearable::use(){current_durability--;}
