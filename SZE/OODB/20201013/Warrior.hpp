#ifndef MASODIK
#define MASODIK

#include <string>
#include "Sword.hpp"

class Warrior {
    public:
        Warrior(const std::string& name, int hp, int mana, int dmg=0, int hpw=0);
        bool isAlive() const;
        std::string toString() const;
        void attack(Warrior& defender) const;
        void heal(Warrior& other);
        std::string getName() const;
    
    private:
        const std::string name;
        int hp;
        int mana;
        const int dmg;
        const int hpw;
        mutable Sword* right_hand_weapon;
};


void printCombatStatus(const Warrior& w1, const Warrior& w2);

#endif

