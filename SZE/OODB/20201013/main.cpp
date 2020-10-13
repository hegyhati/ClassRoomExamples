#include <iostream>
using namespace std;

#include "Warrior.hpp"

int main(){
    std::string name;
    int hp, dmg;
    cin >> name >> hp >> dmg;

    Warrior warrior(name,hp,0,dmg);

    while(warrior.isAlive()){
        cin >> name >> hp >> dmg;
        Warrior enemy(name,hp,0,dmg);
        cout<< "Kezdodik\n";
        printCombatStatus(warrior,enemy);
        
        while (warrior.isAlive() && enemy.isAlive()){
            warrior.attack(enemy);
            printCombatStatus(warrior,enemy);
            if(enemy.isAlive()) {
                enemy.attack(warrior);
                printCombatStatus(warrior,enemy);
            }
        }
    }

    return 0;
}
