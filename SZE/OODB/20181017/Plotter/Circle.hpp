#ifndef CIRCLE_HPP
#define CIRCLE_HPP

#include "Shape.hpp"

class Circle : public Shape{
    const Point center;
    const double radius;
  public:
    Circle(double x, double y, double r, char symbol='c');
    Circle(Point c, double r, char symbol='c');
    ~Circle();
    virtual bool contains(const Point&) const;
};

#endif
