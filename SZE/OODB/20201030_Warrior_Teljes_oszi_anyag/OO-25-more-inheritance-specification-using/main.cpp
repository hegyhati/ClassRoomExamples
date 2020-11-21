#include <iostream>
#include <string>
using namespace std;

#include "Sword.hpp"
#include "SpellBook.hpp"


int main(int argc, char** argv){
    SpellScroll scroll;
    SpellBook::Spell spell("Abrakadabra");
    scroll.writeSpell(spell);


    Sword s(1,2,3.2);
    while (s.isUsable())
      cout << s.attack() << " - " <<s.getWeight()<< endl; 

  return 0;
}
