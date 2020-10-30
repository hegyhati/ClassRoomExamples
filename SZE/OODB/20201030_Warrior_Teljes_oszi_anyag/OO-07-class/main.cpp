#include <iostream>
using namespace std;

#include "Warrior.hpp"
#include "Battle.hpp"


int main(){
  Warrior warrior1,warrior2;
  warrior1.readFromKeyboard();
  warrior2.readFromKeyboard();
  figthTilDeath(warrior1,warrior2);
  return 0;
}
