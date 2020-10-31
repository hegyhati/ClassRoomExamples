#include <iostream>
#include <string>
using namespace std;

#include "Warrior.hpp"
#include "Battle.hpp"


int main(){
  std::string name;
  int hp,dmg,def;

  cin >> name >> hp >> dmg >> def;
  Warrior warrior1(name,hp,dmg,def);
  cin >> name >> hp >> dmg >> def;
  Warrior warrior2(name,hp,dmg,def);


  figthTilDeath(warrior1,warrior2);
  return 0;
}
