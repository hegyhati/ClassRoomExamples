#include "Point.hpp"
#include <cmath>
#include <iostream>


double Point::distanceFrom(const Point& other) const{
  return sqrt((x-other.x)*(x-other.x)+(y-other.y)*(y-other.y));
}


Point::Point(double x, double y, double t)
  : x(x), y(y), t(t) {}

void Point::print() const {
  std::cout<<"("<<x<<","<<y<<")["<<t<<"]"<<std::endl;
}

void Point::set(double x, double y, double t) {
  this->x=x;
  this->y=y;
  this->t=t;
}
