#include "Point.hpp"

#include <cmath>

double Point::distanceFromOrigin() const {
  return sqrt (x*x+y*y);
}

double Point::distance (const Point& other) const {
  return sqrt((x-other.x)*(x-other.x)+(y-other.y)*(y-other.y));
}
