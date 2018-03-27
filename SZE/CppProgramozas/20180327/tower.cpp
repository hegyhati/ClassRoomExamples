#include "tower.hpp"
#include <iostream>

Tower::Tower(int x, int y, double r, double dmg)
    :x(x),y(y),r(r),dmg(dmg) {
        std::cerr<<this<<"\tTower(int,int,double,double)\n";
        meh = new int;
        *meh = 3;
    }

Tower::~Tower(){
    std::cerr<<this<<"\t~Tower()\n";
    delete meh;
}

Tower::Tower(const Tower& othertower)
    : x(othertower.x), y (othertower.y), r(othertower.r), dmg(othertower.dmg){
        std::cerr<<this<<"\tTower(const Tower&)\n";
        meh = new int;
        *meh = *(othertower.meh);
    }

void Tower::setMeh(int mehehe) {
    *meh=mehehe;
}

void Tower::testPrint(){
    std::cout
        << this
        << "\t(" << x <<","<<y<<")"
        << "\tr="<< r<<"\tdmg:"<< dmg
        << "\tmeh: "<<meh<<"---->"<<*meh<<std::endl;    
    }

