#include <iostream>
#include <string>
using namespace std;

#include "Inventory.hpp"
#include "Sword.hpp"


int main(int argc, char** argv){

  Inventory inv(6);
  inv.put(Sword(0,3,1.2));
  inv.put(Sword(1,3,3.4));
  inv.put(Sword(2,3,0.3));
  inv.put(Sword(3,3,1.2));
  inv.put(Sword(4,3,3.4));
  inv.put(Sword(5,3,0.3));

  cout << "------ INV"<<endl;
  for(int i=0; i<inv.count(); ++i)
    cout<<inv.get(i).toString()<<endl;

  
  Inventory inv2(inv);
  inv.clear();

  cout << "------ INV"<<endl;
  for(int i=0; i<inv.count(); ++i)
    cout<<inv.get(i).toString()<<endl;

  cout << "------ INV2"<<endl;
  for(int i=0; i<inv2.count(); ++i)
    cout<<inv2.get(i).toString()<<endl;


  return 0;
}
