#include "tower.hpp"
#include <iostream>

Tower::Tower(int x, int y, double r, double dmg)
    :x(x),y(y),r(r),dmg(dmg) {
        meh = new int;
        *meh = 3;
    }

Tower::~Tower(){
    delete meh;
}

Tower::Tower(const Tower& othertower)
    : x(othertower.x), y (othertower.y), r(othertower.r), dmg(othertower.dmg){
        meh = new int;
        *meh = *(othertower.meh);
    }

void Tower::setMeh(int mehehe) {
    *meh=mehehe;
}

void Tower::testPrint(){
    std::cout
        << "(" << x <<","<<y<<")"
        << "\tr="<< r<<"\tdmg:"<< dmg
        << "\tmeh: "<<meh<<"---->"<<*meh<<std::endl;    
    }

