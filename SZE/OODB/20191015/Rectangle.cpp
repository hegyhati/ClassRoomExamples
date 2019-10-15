#include "Rectangle.hpp"
#include <sstream>
#include <string>
#include <iostream>


Rectangle::Rectangle(double tlx, double tly, double w, double h, std::string sc,int sw,bool f)
  : Shape(sc,sw,f), topleftcorner(tlx,tly), width(w>=0?w:0), height(h>=0?h:0){}


std::string Rectangle::toSVG() const {
  std::stringstream ss;
  ss << "<rect x='"<<topleftcorner.getX()<<"' y='"<<topleftcorner.getY()<<"' width='"<<width<<"' height='"<<height<< "'" <<getSVGStyle() << "/>";
  return ss.str();
}


void testRectangle(){
  Rectangle r1(0,0,50,30);  
  Rectangle r2(3,12,12,12,"red",2,true);  
  Rectangle r3(4,12,-12,12,"csinirozsaszin");

  std::cout  << r1.toSVG() << std::endl
        << r2.toSVG() << std::endl
        << r3.toSVG() << std::endl;
}
