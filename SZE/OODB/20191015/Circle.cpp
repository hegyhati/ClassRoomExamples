#include "Circle.hpp"
#include <iostream>
#include <sstream>

// Peter
Circle::Circle(const double x, const double y, const double r, std::string sc,int sw,bool f)
  : Shape(sc,sw,f), center(x,y), radius(r){
  if(radius<0) {
    std::cerr << "Circle radius negative. Set to 0 as fallback." << std::endl;
    radius=0;
  }
}

Coordinate Circle::getCenter() const {return center;}
double Circle::getRadius() const {return radius;}
double Circle::getCenterX() const {return center.getX();}
double Circle::getCenterY() const {return center.getY();}



std::string Circle::toSVG() const {
  std::stringstream ss;
  ss << "<circle cx='" << center.getX() << "' cy='" << center.getY() << "' r='" << radius << "'" << getSVGStyle() << "/>";
  return ss.str();
}





// Gergo
#include <iostream>
void testCircle() {
  {
    Circle C(0,0,20);
    std::cout <<"Circle C(0,0,20);"<<std::endl
              <<" center="<<C.getCenterX()<<","<<C.getCenterY()<<std::endl
              <<" center="<<C.getCenter().getX()<<","<<C.getCenter().getY()<<std::endl
              <<" radius="<<C.getRadius()<<std::endl;
  }
  {    
    Circle C(3,-3,6);
    std::cout <<"Circle C(3,-3,6);"<<std::endl
              <<" center="<<C.getCenterX()<<","<<C.getCenterY()<<std::endl
              <<" center="<<C.getCenter().getX()<<","<<C.getCenter().getY()<<std::endl
              <<" radius="<<C.getRadius()<<std::endl;
  }
  {    
    Circle C(2,1,-6);
    std::cout <<"Circle C(2,1,-6);"<<std::endl
              <<" center="<<C.getCenterX()<<","<<C.getCenterY()<<std::endl
              <<" center="<<C.getCenter().getX()<<","<<C.getCenter().getY()<<std::endl
              <<" radius="<<C.getRadius()<<std::endl;
  }
}

void testCircle2(){  
  Circle c1(10,82,30);
  Circle c2(12,12,12,"red",2,true);  
  Circle c3(12,12,12,"csinirozsaszin");
  std::cout<<c1.toSVG()<<std::endl;
  std::cout<<c2.toSVG()<<std::endl;
  std::cout<<c3.toSVG()<<std::endl;
}

