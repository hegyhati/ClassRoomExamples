#ifndef SQUARE_HPP
#define SQUARE_HPP

#include "Rectangle.hpp"

class Square : public Rectangle {
  public:
    Square(double tlx, double tly, double d, std::string sc="black",int sw=1,bool f=false) : Rectangle(tlx,tly,d,d,sc,sw,f){}
};


#endif
