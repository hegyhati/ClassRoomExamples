#include "Shape.hpp"
#include <sstream>

Shape::Shape(std::string sc,int sw,bool f)
  : stroke_color(sc),stroke_width(sw), fill(f) {
  if(stroke_width<0) stroke_width=0;
  if(stroke_color!="black" && stroke_color!="very very dark gray" && stroke_color!="red")
    stroke_color="black";
}


std::string Shape::getSVGStyle() const {
  std::stringstream ss;
  ss << " stroke='"<< stroke_color << "' stroke-width='"<< stroke_width <<"' fill='"<< (fill?stroke_color:"none") << "'";
  return ss.str();
}


