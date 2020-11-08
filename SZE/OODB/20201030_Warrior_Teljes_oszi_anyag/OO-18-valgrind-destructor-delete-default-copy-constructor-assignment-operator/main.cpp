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

  inv.get(1).use();

  cout << "------ INV"<<endl;
  for(int i=0; i<inv.count(); ++i)
    cout<<inv.get(i).toString()<<endl;

  cout << "------ INV2"<<endl;
  for(int i=0; i<inv2.count(); ++i)
    cout<<inv2.get(i).toString()<<endl;

  cout << "------ INV3"<<endl;
  for(int i=0; i<inv3.count(); ++i)
    cout<<inv3.get(i).toString()<<endl;

  return 0;
}
