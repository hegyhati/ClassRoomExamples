#include "Warrior.hpp"

#include <iostream>

Warrior readWarrior(){
  Warrior warrior;
  std::cin >> warrior.name >> warrior.health_points >> warrior.damage >> warrior.defense;
  return warrior;
}

void printWarrior(const Warrior& warrior){
  std::cout << warrior.name << " ["
    <<" HP:  "<<warrior.health_points
    <<" DMG: "<<warrior.damage
    <<" DEF: "<<warrior.defense
    <<"]";
}

void die(Warrior& warrior){
  warrior.health_points=0;
  warrior.damage=0;
  warrior.defense=0;
  warrior.name += " DEAD ";
}

void attack(const Warrior& attacker, Warrior& defender){  
    int actual_damage=attacker.damage-defender.defense;
    if (actual_damage>0) {
      defender.health_points-=actual_damage; 
      if (!isAlive(defender)) die(defender);
    }
}

bool isAlive(const Warrior& warrior){
  return warrior.health_points > 0;
}
