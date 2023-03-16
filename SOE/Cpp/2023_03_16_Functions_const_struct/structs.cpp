#include <iostream>
#include <ostream>
using std::cin;
using std::cout;
using std::endl;

struct Warrior {
    int hp;
    int dmg;
};

bool isDead(const Warrior& warrior) {
    return warrior.hp == 0;
}

std::ostream& operator << (std::ostream& o, const Warrior& w) {
    return o << "HP: " << w.hp << " DMG: " << w.dmg;
}

void attack (const Warrior& attacker, Warrior& defender) {
    if ( !isDead(attacker) ){
        defender.hp -= attacker.dmg;
        if (defender.hp < 0) defender.hp = 0;
    }
}

Warrior& operator >> (const Warrior& attacker, Warrior& defender) {
    attack(attacker, defender);
    return defender;
}

int main(){
    Warrior Conan {100, 4};
    Warrior Xena {80, 6};   


    cout << "Conan: " << Conan << endl;
    cout << (isDead(Conan) ? "DEAD" : "ALIVE") << endl;
    cout << "Xena: " << Xena << endl;
    cout << (isDead(Xena) ? "DEAD" : "ALIVE") << endl;

    while( !isDead(Conan) && !isDead(Xena) ) {
        Xena >> Conan >> Xena;
    }

    cout << "Conan: " << Conan << endl;
    cout << (isDead(Conan) ? "DEAD" : "ALIVE") << endl;
    cout << "Xena: " << Xena << endl;
    cout << (isDead(Xena) ? "DEAD" : "ALIVE") << endl;
    return 0;
}
