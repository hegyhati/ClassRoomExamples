#include <iostream>
#include <memory>
#include <set>
using namespace std;

#include "Person.hpp"
#include "Rule.hpp"
#include "Game.hpp"

int main() {
    Game game;

    game.addPerson(Person{"Apa", {"felnott", "ferfi"}});
    game.addPerson(Person{"Petike", {"gyerek", "fiu"}});
    game.addPerson(Person{"Anya", {"felnott", "no"}});  

    game.addBoatRule(AtLeastOneWithLabelRule("felnott"));
    game.addBoatRule(AtMostNRule(2));

    
    return 0;
}