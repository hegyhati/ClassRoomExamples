/*
    Csinalj egy Polynom osztalyt, mely egy polinom fuggvenyt ir le.
    Mukodjon vele minden az alabbi main-bol:
*/

int main() {
    Polynom f(3, {1,2,3}); // 3x^2 + 2x + 1
    Polynom g(2, {0,1});  // x^2

    Polynom h = f*g;
    Polynom dh = h.derivate();
    

    std::cout << dh.at(5);
    // advanced:
    std::cout << dh(5);
    return 0;
}