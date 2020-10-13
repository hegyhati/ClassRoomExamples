#include "Sword.hpp"


Sword::Sword(int dmg, int dur) 
: dmg(dmg),durability(dur){}

int Sword::use() {
    if(durability>0){
        durability--;
        return dmg;        
    } else return 0;
}
