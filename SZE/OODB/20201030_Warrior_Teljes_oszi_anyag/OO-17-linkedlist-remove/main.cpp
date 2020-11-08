#include <iostream>
#include <string>
using namespace std;

#include "Sword.hpp"
#include "Inventory.hpp"


int main(int argc, char** argv){
  Inventory inv;
  inv.put(Sword(0,3,1.2));
  inv.put(Sword(1,3,3.4));
  inv.put(Sword(2,3,0.3));
  cout << inv.count() << endl;
  cout << inv.getTotalWeight()<<endl;
  inv.put(Sword(3,3,1));
  inv.put(Sword(4,3,2));
  cout << inv.count() << endl;
  cout << inv.getTotalWeight()<<endl;

  inv.get(0).use();
  inv.get(0).use();

  for(int i=0; i<inv.count(); i++) cout<<i<<". item: "<<inv.get(i).toString() << endl;

  cout << endl << endl ; 
  try{
    while(true){
      Sword dropped = inv.drop(0);
      cout << "Dropped sword: "<<dropped.toString() << endl;
      for(int i=0; i<inv.count(); i++) cout<<i<<". item: "<<inv.get(i).toString() << endl;
      cout << endl;
    }
  } catch (Inventory::WrongIndexException e) {
    cout << "Wrong index" << endl;
  }

  return 0;
}
