#ifndef TOWER_HPP
#define TOWER_HPP

#include "Entity.hpp"

class Tower : public Entity {
    private:
        double damage;
        double range;
    public:
        Tower(int x, int y, double damage, double range);
        double getDamage() const;
        double getRange() const;        
};


#endif
