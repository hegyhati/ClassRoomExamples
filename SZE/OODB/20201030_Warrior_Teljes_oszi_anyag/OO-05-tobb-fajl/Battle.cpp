#include "Battle.hpp"

#include <iostream>

void printStatus(const Warrior& warrior1, const Warrior& warrior2){
  printWarrior(warrior1);
  std::cout << " --- ";
  printWarrior(warrior2);
  std::cout << std::endl;
}

void figthTilDeath(Warrior& warrior1, Warrior& warrior2) {
  while (isAlive(warrior1) && isAlive(warrior2)) {
    printStatus(warrior1,warrior2);  
    attack(warrior1,warrior2);
    if (isAlive(warrior2)) {      
      printStatus(warrior1,warrior2);  
      attack(warrior2,warrior1);
    }
  }
  printStatus(warrior1,warrior2);
}
