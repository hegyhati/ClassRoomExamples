#include "Wearable.hpp"


Wearable::Wearable(int max_durability, double weight) 
      : max_durability(max_durability), current_durability(max_durability), weight(weight) { }


void Wearable::repair() { 
  if(!isUsable() && max_durability>0) 
    max_durability--; 
  current_durability = max_durability; 
}

double Wearable::getWeight() const { return weight; }

bool Wearable::isUsable() const {return current_durability>0;}
void Wearable::use(){current_durability--;}
