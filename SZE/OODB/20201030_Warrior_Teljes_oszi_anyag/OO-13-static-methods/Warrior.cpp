#include "Warrior.hpp"
#include <fstream>

int Warrior::alive=0;

Warrior::Warrior(const std::string& team, const std::string& name, int health_points, int damage, int defense) 
  : team(team), name(name), health_points(health_points), damage(damage), defense(defense) {++alive;}

Warrior Warrior::parseFromFile(const std::string& team, const std::string& filename){
  std::ifstream file(filename);
  if(file.is_open()){
    std::string name;
    int health_points, damage, defense;
    file >> name >> health_points >> damage >> defense;
    file.close();
    return Warrior(team,name,health_points,damage,defense);
  }
  return Warrior(team,"Anonymus",1);
}

std::string Warrior::toString() const {
  return
    name  + (isAlive()?"":" DEAD ") + "(" + team + ") "
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
  --alive;
}

void Warrior::attack(Warrior& defender) const {  
  if(team != defender.team) {
    if (int actual_damage=damage-defender.defense; actual_damage>0) {
      defender.health_points-=actual_damage; 
      if (!defender.isAlive()) defender.die();
    }
  }
}

bool Warrior::isAlive() const {
  return health_points > 0;
}

std::string Warrior::getTeam() const { return team; }
