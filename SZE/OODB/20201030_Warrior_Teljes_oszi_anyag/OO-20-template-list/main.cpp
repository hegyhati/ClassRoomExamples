#include <iostream>
#include <string>
using namespace std;

#include "List.hpp"
#include "HealthPotion.hpp"

int main(int argc, char** argv){

  List<HealthPotion> my_int_list;
  my_int_list.put(HealthPotion{18682});
  my_int_list.put(HealthPotion{14652});
  my_int_list.put(HealthPotion{14562});
  my_int_list.put(HealthPotion{14562});
  my_int_list.put(HealthPotion{144562});
  my_int_list.put(HealthPotion{12});
  
  try {
    while (true) {
      for(int i=0; i<my_int_list.count(); i++)
        cout<<i<<". potion: "<<my_int_list.get(i).health_points<<endl;
      
      my_int_list.pop(3);
      cout << endl;
    } 

  } catch (WrongIndexException e) {
    cout << "Could not access element at index "<<e.index<<".\n";
  }

  return 0;
}
