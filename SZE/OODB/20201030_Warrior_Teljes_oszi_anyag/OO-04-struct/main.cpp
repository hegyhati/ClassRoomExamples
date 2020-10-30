#include <iostream>
#include <string>

using namespace std;

struct Warrior {
  string name;
  int health_points;
  int damage;
};

Warrior readWarrior(){
  Warrior warrior;
  cin >> warrior.name >> warrior.health_points >> warrior.damage;
  return warrior;
}

void printWarrior(const Warrior& warrior){
  cout << warrior.name << " [HP: "<<warrior.health_points<<" DMG: "<<warrior.damage<<"]";
}

void printStatus(const Warrior& warrior1, const Warrior& warrior2){
  printWarrior(warrior1);
  cout << " --- ";
  printWarrior(warrior2);
  cout << endl;
}

void attack(const Warrior& attacker, Warrior& defender){
    printStatus(attacker,defender);    
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

int main(){
  Warrior warrior1,warrior2;
  warrior1=readWarrior();
  warrior2=readWarrior();

  while (isAlive(warrior1) && isAlive(warrior2)) {
    attack(warrior1,warrior2);
    if (isAlive(warrior2)) attack(warrior2,warrior1);
  }
  printStatus(warrior1,warrior2);

  return 0;
}
