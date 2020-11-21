#include <iostream>
#include <string>
using namespace std;

#include "Inventory.hpp"
#include "Sword.hpp"
#include "Shield.hpp"
#include "SpellBook.hpp"


int main(int argc, char** argv){
  Inventory inv(12);

  inv.put(new Sword(12,3,3.5));
  inv.put(new SpellScroll());
  inv.put(new Shield(12,12,5.5));

  for(int i=0; i<inv.count(); ++i){
    cout << inv.get(i).toString() << endl;       
  }
    

  return 0;
}
