#include <iostream>
#include <string>
using namespace std;

#include "Hallgato.hpp"
#include "Targy.hpp"
#include "Felev.hpp"


int main(){

  Hallgato Jani("Hollosi Janos","ABC123");
  Hallgato Erno("Horvath Erno", "XYZ987");
  Hallgato Jozsi("Szabo Jozsef", "AAA000");

  Targy CppProg("C++","GIVK-32165",4);
  CppProg.addHallgato(Jani);
  CppProg.addHallgato(Erno);  

  Targy Python("Python","GIVK-32765",2);
  
  Felev aktualis(2018,"osz");
  aktualis.addTargy(CppProg);
  aktualis.addTargy(Python);

  Targy BF("Brainfuck", "GIVK-987",10);
  aktualis.addTargy(BF);
  aktualis.assignHallgato(BF,Jozsi);

  cout<<aktualis;
    
  return 0;
}
