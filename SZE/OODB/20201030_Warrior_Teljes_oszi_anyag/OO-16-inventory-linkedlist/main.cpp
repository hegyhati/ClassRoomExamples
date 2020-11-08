#include <iostream>
#include <string>
using namespace std;

#include "Sword.hpp"
#include "Inventory.hpp"


int main(int argc, char** argv){
  Inventory inv;
  inv.put(Sword(12,3,1.2));
  inv.put(Sword(12,3,3.4));
  inv.put(Sword(12,3,0.3));
  cout << inv.count() << endl;
  cout << inv.getTotalWeight()<<endl;
  inv.put(Sword(12,3,1));
  inv.put(Sword(12,3,2));
  cout << inv.count() << endl;
  cout << inv.getTotalWeight()<<endl;

  inv.get(3).use();
  inv.get(3).use();

  for(int i=0; i<inv.count(); i++) {
    cout<<i<<". item: "<<inv.get(i).toString() << endl;
  }

  return 0;
}
