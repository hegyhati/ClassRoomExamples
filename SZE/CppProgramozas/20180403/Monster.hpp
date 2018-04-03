#ifndef MONSTER_HPP
#define MONSTER_HPP

#include "Entity.hpp"

class Monster : public Entity {
    private:
        int speed;
        int HP;
    public:
        Monster(int x, int y, int speed, int HP);
        bool attack(double damage);
        bool move();
};


#endif
