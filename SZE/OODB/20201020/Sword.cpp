#include "Sword.hpp"


Sword::Sword(int dmg, int dur, double weight) 
: dmg(dmg),durability(dur), weight(weight){}

int Sword::use() {
    if(durability>0){
        durability--;
        return dmg;        
    } else return 0;
}

std::string Sword::toString() const {
    return "Sword(DMG:" + std::to_string(dmg)+",DUR:"+std::to_string(durability)+")";
}

double Sword::getWeight() const { return weight; }
