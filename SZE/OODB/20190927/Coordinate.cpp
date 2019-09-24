#include "Coordinate.hpp"



// Petra
Coordinate::Coordinate(const double x, const double y)
  : x(x), y(y) {}
  
double Coordinate::getX() const {return x;}
double Coordinate::getY() const {return y;}


// Dori
#include <iostream>
void testCoordinate(){
  { 
    Coordinate A(0,0);
    std::cout << "A(0,0): x="<<A.getX()<<", y="<<A.getY()<<std::endl;
  }
  {
    Coordinate B(1,-3);
    std::cout << "B(1,-3): x="<<B.getX()<<", y="<<B.getY()<<std::endl;
  }
}
