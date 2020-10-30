#ifndef WARRIOR_HPP
#define WARRIOR_HPP

#include <string>

struct Warrior {
  std::string name;
  int health_points;
  int damage;
};

Warrior readWarrior();
void printWarrior(const Warrior& warrior);
void attack(const Warrior& attacker, Warrior& defender);
bool isAlive(const Warrior& warrior);

#endif 
