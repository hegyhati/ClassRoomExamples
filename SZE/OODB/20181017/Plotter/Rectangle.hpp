#ifndef RECTANGLE_HPP
#define RECTANGLE_HPP

#include "Shape.hpp"

class Rectangle : public Shape{
    const double xmin;
    const double xmax;
    const double ymin;
    const double ymax;
  public:
    Rectangle(double xmin, double xmax, double ymin, double ymax, char symbol='r');
    Rectangle(Point p1, Point p2, char symbol='r');
    ~Rectangle();
    virtual bool contains(const Point&) const;
};

#endif
