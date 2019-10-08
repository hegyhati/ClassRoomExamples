#ifndef SHAPE_HPP
#define SHAPE_HPP

#include <string>

class Shape {
  protected:
    std::string stroke_color;
    int stroke_width;
    bool fill;
    std::string getSVGStyle() const;
  public:
    Shape(std::string sc="black",int sw=1,bool f=false);
};



#endif
