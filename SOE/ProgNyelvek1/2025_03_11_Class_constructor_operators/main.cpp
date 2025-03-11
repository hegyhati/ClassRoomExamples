#include "Point2D.hpp"
#include <iostream>
using std::cerr;


int main() {

    cerr << "A(1,2): ";
    Point2D A(1,2);
    cerr << "B(-3.5, 5.6): ";
    Point2D B(-3.5, 5.6);
    cerr << "Point2D C = A;";
    Point2D C = A; // -> Copy constructor
    cerr << "Point2D E(B): "; 
    Point2D E(B); // -> Copy constructor
    cerr << "Point2D D: ";
    Point2D D;
    cerr << "D = B: ";
    D = B;
    cerr << (A) << "\n";
    cerr << (B) << "\n";
    cerr << (C) << "\n";
    cerr << (D) << "\n";
    cerr << (A*4+B*2+4*C*6+D) << "\n";
    return 0;
}


void foo(int a){
}