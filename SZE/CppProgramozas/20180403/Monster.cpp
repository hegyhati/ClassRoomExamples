#include "Monster.hpp"

Monster::Monster(int x, int y, int speed, int HP)
    : Entity(x,y),speed(speed), HP(HP) {}

bool Monster::attack(double damage){
    HP-=damage;
    return HP<=0;
}

bool Monster::move() {
    x-=speed;
    return x<=0;
}
