#ifndef CIRCLE_HPP
#define CIRCLE_HPP


// Peter
#include "Coordinate.hpp"
#include "Shape.hpp"
#include <string>

class Circle : public Shape{
    Coordinate center;
    double radius;
  public:
    Circle(const double x, const double y, const double r, std::string sc="black",int sw=1,bool f=false);
    Coordinate getCenter() const;
    double getRadius() const;
    double getCenterX() const;
    double getCenterY() const;
    std::string toSVG() const;
};

// Gergo
void testCircle();
void testCircle2();

#endif
