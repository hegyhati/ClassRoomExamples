#ifndef CIRCLE_HPP
#define CIRCLE_HPP


// Peter
#include "Coordinate.hpp"

class Circle{
    Coordinate center;
    double radius;
  public:
    Circle(const double x, const double y, const double r);
    Coordinate getCenter() const;
    double getRadius() const;
    double getCenterX() const;
    double getCenterY() const;
};

// Gergo
void testCircle();

#endif
