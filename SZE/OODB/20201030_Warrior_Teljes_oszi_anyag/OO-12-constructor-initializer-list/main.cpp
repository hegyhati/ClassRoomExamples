#include <iostream>
#include <string>
using namespace std;

#include "Warrior.hpp"
#include "Battle.hpp"


int main(int argc, char** argv){
  Warrior warrior1("Blue", argv[1]);
  Warrior warrior2("Red", argv[2]);

  figthTilDeath(warrior1,warrior2);
  return 0;
}
