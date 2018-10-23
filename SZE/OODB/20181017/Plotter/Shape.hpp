#ifndef SHAPE_HPP
#define SHAPE_HPP

#include "Point.hpp"

class Shape{
  private:
    const char symbol;
  public:
    virtual bool contains(const Point&) const =0;
    Shape(char symbol='#'):symbol(symbol){}
    virtual ~Shape(){}
    char getSymbol() const {return symbol;}
};

#endif
