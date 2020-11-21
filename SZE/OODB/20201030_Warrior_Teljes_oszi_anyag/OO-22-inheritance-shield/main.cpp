#include <iostream>
#include <string>
using namespace std;

#include "Sword.hpp"


int main(int argc, char** argv){

    Sword s(1,2,3);
    while (s.isUsable())
      cout << s.attack() << endl;
      
  return 0;
}
