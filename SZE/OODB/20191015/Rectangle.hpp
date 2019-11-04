#ifndef RECTANGLE_HPP
#define RECTANGLE_HPP

#include "Shape.hpp"
#include "Coordinate.hpp"
#include <string>

class Rectangle :public Shape {
    Coordinate topleftcorner;
    double width;
    double height;
  public:
    Rectangle(double tlx, double tly, double w, double h, std::string sc="black",int sw=1,bool f=false);    
    virtual std::string toSVG() const override;
};


void testRectangle();


#endif
