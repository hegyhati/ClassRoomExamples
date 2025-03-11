/*
    Irj meg egy Complex nevu osztalyt, amiben complex szamokat lehet tarolni, es tudunk azzal szamolni. Az alabbi main forduljon le vele.
*/

#include <iostream>
using namespace std;
#include "complex.hpp"

int main() {
    Complex c1(2,-3);
    Complex c2(3);

    Complex c3 = c2;

    double real, imaginary;
    cin >> real >> imaginary;
    Complex c4(real,imaginary);

    if (c1 == c4) {
        cout << "Yeppee\n";
    }

    cout << c1 + c2 * (c2 - 3*c3 ) << "\n";
    return 0;
}