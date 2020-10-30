#include "Warrior.hpp"

#include <iostream>

Warrior readWarrior(){
  Warrior warrior;
  std::cin >> warrior.name >> warrior.health_points >> warrior.damage;
  return warrior;
}

void printWarrior(const Warrior& warrior){
  std::cout << warrior.name << " [HP: "<<warrior.health_points<<" DMG: "<<warrior.damage<<"]";
}

void attack(const Warrior& attacker, Warrior& defender){  
    defender.health_points-=attacker.damage; 
    if (defender.health_points<=0) {
      defender.damage=0;
      defender.name += " DEAD ";
      defender.health_points=0;
    }
}

bool isAlive(const Warrior& warrior){
  return warrior.health_points > 0;
}
