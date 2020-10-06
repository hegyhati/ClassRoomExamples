#ifndef MASODIK
#define MASODIK

#include <string>

struct Warrior {
    std::string name;
    int hp;
    int dmg;
};

bool isAlive(const Warrior& w);
std::string toString(const Warrior& w);
void attack(const Warrior& attacker, Warrior& defender);
void printCombatStatus(const Warrior& w1, const Warrior& w2);

#endif
