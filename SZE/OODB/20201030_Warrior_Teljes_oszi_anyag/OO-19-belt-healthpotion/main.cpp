#include <iostream>
#include <string>
using namespace std;

#include "Belt.hpp"
#include "HealthPotion.hpp"

int main(int argc, char** argv){
  Belt b;
  b.put(HealthPotion{12});
  b.put(HealthPotion{22});
  b.put(HealthPotion{32});
  b.put(HealthPotion{42});
  b.put(HealthPotion{52});
  b.put(HealthPotion{62});

  try {
    while (true) {
      for(int i=0; i<b.count(); i++)
        cout<<i<<". potion: "<<b.watch(i).health_points<<endl;
      
      b.get(3);
    } 

  } catch (Belt::WrongIndexException e) {
    cout << "empty\n";
  }

  return 0;
}
