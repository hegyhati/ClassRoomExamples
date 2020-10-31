#include "Warrior.hpp"
#include <fstream>

Warrior::Warrior(const std::string& name, int health_points, int damage, int defense){
  this->name=name;
  this->health_points=health_points;
  this->damage=damage;
  this->defense=defense;
}

Warrior::Warrior(const std::string& filename) {
  std::ifstream file(filename);
  if(file.is_open()){
    file >> name >> health_points >> damage >> defense;
    file.close();
  }
}

std::string Warrior::toString() const {
  return
    name 
    + " ["
    + " HP:  " + std::to_string(health_points)
    + " DMG: " + std::to_string(damage)
    + " DEF: " + std::to_string(defense)
    + "]";
}

void Warrior::die(){
  health_points=0;
  damage=0;
  defense=0;
  name += " DEAD ";
}

void Warrior::attack(Warrior& defender) const {  
    if (int actual_damage=damage-defender.defense; actual_damage>0) {
      defender.health_points-=actual_damage; 
      if (!defender.isAlive()) defender.die();
    }
}

bool Warrior::isAlive() const {
  return health_points > 0;
}
