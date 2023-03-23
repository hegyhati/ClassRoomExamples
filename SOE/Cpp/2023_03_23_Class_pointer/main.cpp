#include <iostream>
using std::cin;
using std::cout;
using std::endl;

#include "Warrior.hpp"

int main(){


    Warrior Conan(100, 4);
    Warrior Xena(80, 6);   


    cout << "Conan: " << Conan << endl;
    cout << (Conan.isDead() ? "DEAD" : "ALIVE") << endl;
    cout << "Xena: " << Xena << endl;
    cout << (Xena.isDead() ? "DEAD" : "ALIVE") << endl;

    while( !Conan.isDead() && !Xena.isDead() ) {
        Xena.attack(Conan);
        Conan.attack(Xena);
    }

    cout << "Conan: " << Conan << endl;
    cout << (Conan.isDead() ? "DEAD" : "ALIVE") << endl;
    cout << "Xena: " << Xena << endl;
    cout << (Xena.isDead() ? "DEAD" : "ALIVE") << endl;
    return 0;
}
