#include "Warrior.hpp"

#include <iostream>

void Warrior::readFromKeyboard(){
  std::cin >> name >> health_points >> damage >> defense;
}

void Warrior::printToTerminal(){
  std::cout << name << " ["
    <<" HP:  "<<health_points
    <<" DMG: "<<damage
    <<" DEF: "<<defense
    <<"]";
}

void Warrior::die(){
  health_points=0;
  damage=0;
  defense=0;
  name += " DEAD ";
}

void Warrior::attack(Warrior& defender){  
    int actual_damage=damage-defender.defense;
    if (actual_damage>0) {
      defender.health_points-=actual_damage; 
      if (!defender.isAlive()) defender.die();
    }
}

bool Warrior::isAlive(){
  return health_points > 0;
}
