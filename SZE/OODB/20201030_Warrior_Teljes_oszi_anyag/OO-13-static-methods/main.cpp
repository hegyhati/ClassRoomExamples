#include <iostream>
#include <string>
using namespace std;

#include "Warrior.hpp"
#include "Battle.hpp"


int main(int argc, char** argv){
  Warrior warrior1 = Warrior::parseFromFile("Blue", argv[1]);
  Warrior warrior2 = Warrior::parseFromFile("Red", argv[2]);
  figthTilDeath(warrior1,warrior2);
  cout << Warrior::getAliveWarriorCount() << " warriors are still alive." << endl;
  return 0;
}
