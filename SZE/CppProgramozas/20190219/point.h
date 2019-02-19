#ifndef POINT_H
#define POINT_H

#include <iostream>

class Point {
  double x;
  double y;

public:
  Point(double x = 0, double y = 0);
  double getX() const;
  void setX(double value);
  double getY() const;
  void setY(double value);

  void print() const;
  double operator-(const Point &other);
};

std::ostream &operator<<(std::ostream &s, const Point &p);

#endif // POINT_H
