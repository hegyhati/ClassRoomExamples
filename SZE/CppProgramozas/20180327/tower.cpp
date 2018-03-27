#include "tower.hpp"
#include <iostream>

Tower::Tower(int x, int y, double r, double dmg)
    :x(x),y(y),r(r),dmg(dmg) {}

void Tower::testPrint(){
    std::cout
        << "(" << x <<","<<y<<")"
        << "\tr="<< r<<"\tdmg:"<< dmg<<std::endl;    
    }

