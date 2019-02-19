#include "point.h"
#include <cmath>

double Point::getX() const { return x; }

void Point::setX(double value) { x = value; }

double Point::getY() const { return y; }

void Point::setY(double value) { y = value; }

double Point::operator-(const Point &other) {
  return sqrt((x - other.x) * (x - other.x) + (y - other.y) * (y - other.y));
}

Point::Point(double x, double y) : x(x), y(y) {}

std::ostream &operator<<(std::ostream &s, const Point &p) {
  s << "(" << p.getX() << "," << p.getY() << ")";
  return s;
}
