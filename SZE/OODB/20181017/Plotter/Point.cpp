#include "Point.hpp"
#include <cmath>

Point::Point(double x, double y) :x(x),y(y) {}

double Point::operator-(const Point& other) const {
  return sqrt( (x-other.x)*(x-other.x) + (y-other.y)*(y-other.y) );
}
