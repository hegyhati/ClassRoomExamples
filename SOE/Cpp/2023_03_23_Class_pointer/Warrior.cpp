#include "Warrior.hpp"

Warrior::Warrior(int max_hp, int dmg) : max_hp(max_hp), hp(max_hp),  dmg(dmg){}

bool Warrior::isDead() const {
    return hp == 0;
}

void Warrior::heal(int points) {
    hp += points;
    if (hp>max_hp) hp=max_hp;
}

void Warrior::attack (Warrior& defender) const {
    if ( !isDead()   ){
        defender.hp -= dmg;
        if (defender.hp < 0) defender.hp = 0;
    }
}

std::ostream& operator << (std::ostream& o, const Warrior& w) {
    return o << "HP: " << w.hp << " DMG: " << w.dmg;
}