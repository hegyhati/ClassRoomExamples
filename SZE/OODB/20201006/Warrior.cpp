#include "Warrior.hpp"
#include <iostream>

void inputFromTerminal(Warrior& w){
    std::cin >> w.name >> w.hp >> w.dmg;
}

bool isAlive(const Warrior& w){
    return w.hp > 0;
}

std::string toString(const Warrior& w){
    return w.name + "(" + std::to_string(w.hp) + "), DMG="+ std::to_string(w.dmg);
}

void attack(const Warrior& attacker, Warrior& defender){
    defender.hp -= attacker.dmg;
}

void printCombatStatus(const Warrior& w1, const Warrior& w2) {
    std::cout << toString(w1) << " / " << toString(w2) << std::endl;
}   
