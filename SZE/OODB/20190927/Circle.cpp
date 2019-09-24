#include "Circle.hpp"
#include <iostream>

// Peter
Circle::Circle(const double x, const double y, const double r)
  : center(x,y), radius(r) {
  if(radius<0) {
    std::cerr << "Circle radius negative. Set to 0 as fallback." << std::endl;
    radius=0;
  }
}

Coordinate Circle::getCenter() const {return center;}
double Circle::getRadius() const {return radius;}
double Circle::getCenterX() const {return center.getX();}
double Circle::getCenterY() const {return center.getY();}

// Gergo
#include <iostream>
void testCircle() {
  {
    Circle C(0,0,20);
    std::cout <<"Circle C(0,0,20);"<<std::endl
              <<" center="<<C.getCenterX()<<","<<C.getCenterY()<<std::endl
              <<" center="<<C.getCenter().getX()<<","<<C.getCenter().getY()<<std::endl
              <<" radius="<<C.getRadius()<<std::endl;
  }
  {    
    Circle C(3,-3,6);
    std::cout <<"Circle C(3,-3,6);"<<std::endl
              <<" center="<<C.getCenterX()<<","<<C.getCenterY()<<std::endl
              <<" center="<<C.getCenter().getX()<<","<<C.getCenter().getY()<<std::endl
              <<" radius="<<C.getRadius()<<std::endl;
  }
  {    
    Circle C(2,1,-6);
    std::cout <<"Circle C(2,1,-6);"<<std::endl
              <<" center="<<C.getCenterX()<<","<<C.getCenterY()<<std::endl
              <<" center="<<C.getCenter().getX()<<","<<C.getCenter().getY()<<std::endl
              <<" radius="<<C.getRadius()<<std::endl;
  }
}
