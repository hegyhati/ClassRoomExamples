#include "Battle.hpp"

#include <iostream>

void printStatus(Warrior& warrior1, Warrior& warrior2){
  warrior1.printToTerminal();
  std::cout << " --- ";
  warrior2.printToTerminal();
  std::cout << std::endl;
}

void figthTilDeath(Warrior& warrior1, Warrior& warrior2) {
  while (warrior1.isAlive() && warrior2.isAlive()) {
    printStatus(warrior1,warrior2);  
    warrior1.attack(warrior2);
    if (warrior2.isAlive()) {      
      printStatus(warrior1,warrior2);  
      warrior2.attack(warrior1);
    }
  }
  printStatus(warrior1,warrior2);
}
