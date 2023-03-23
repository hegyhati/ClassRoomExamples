#ifndef WARRIOR_HPP
#define WARRIOR_HPP

#include <ostream>

class Warrior {
        const int max_hp;
        int hp;
        const int dmg;

    public:

        Warrior(int max_hp, int dmg);
        bool isDead() const ;
        void heal(int points);
        void attack (Warrior& defender) const;
        friend std::ostream& operator << (std::ostream& o, const Warrior& w);
};

#endif