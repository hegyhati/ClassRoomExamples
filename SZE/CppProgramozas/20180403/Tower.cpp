#include "Tower.hpp"

Tower::Tower(int x, int y, double damage, double range)
    :Entity(x,y), damage(damage), range(range) {}


double Tower::getDamage() const {return damage;}
double Tower::getRange() const {return range;}
