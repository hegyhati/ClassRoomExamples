#include "Warrior.hpp"

Warrior::Warrior(const std::string& name, int hp, int mana, int dmg, int hpw)
: name("Warrior "+ name), hp(hp), mana(mana), dmg(dmg), hpw(hpw), right_hand_weapon(nullptr){}

bool Warrior::isAlive() const{
    return hp > 0;
}

std::string Warrior::toString() const {
    return name + "(" + std::to_string(hp) + "), DMG="+ std::to_string(dmg);
}

void Warrior::attack(Warrior& defender) const {
    defender.hp -= dmg+(right_hand_weapon ? right_hand_weapon->use() : 0);
}

void Warrior::heal(Warrior& other) {
    if(mana>0){
        other.hp += hpw;
        mana--;
    } 
}

std::string Warrior::getName() const {return name;}



#include <iostream>
void printCombatStatus(const Warrior& w1, const Warrior& w2) {
    std::cout << w1.toString() << " / " << w2.toString() << std::endl;
}   

