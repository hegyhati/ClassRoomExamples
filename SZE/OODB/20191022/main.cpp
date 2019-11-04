#include <iostream>
using namespace std;

#include "String.hpp"

int main(){
  String alma("alma");
  alma+=-1028;
  alma+=" masik alma";
  String korte("korte");
  //String ezer(1000,3)
  // alma + 24
  alma += korte;
  cout << alma << endl;
};
