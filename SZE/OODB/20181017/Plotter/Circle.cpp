#include "Circle.hpp"

Circle::Circle(double x, double y, double r, char s)
  : Shape(s), center(x,y), radius(r) {}

Circle::Circle(Point c, double r, char s)
  : Shape(s), center(c), radius(r) {}

Circle::~Circle(){}

bool Circle::contains(const Point& p) const {
  return p-center <= radius;
}
