#include "Rectangle.hpp"


Rectangle::Rectangle(double xmin, double xmax, double ymin, double ymax, char s)
  :Shape(s),xmin(xmin),xmax(xmax),ymin(ymin),ymax(ymax){}
  
Rectangle::Rectangle(Point p1, Point p2, char s)
  :Shape(s),
   xmin(p1.x<p2.x?p1.x:p2.x),xmax(p1.x>p2.x?p1.x:p2.x),
   ymin(p1.y<p2.y?p1.y:p2.y),ymax(p1.y>p2.y?p1.y:p2.y) {}
   
Rectangle::~Rectangle(){}

bool Rectangle::contains(const Point& p) const {
  return 
    p.x >= xmin &&
    p.x <= xmax &&
    p.y >= ymin &&
    p.y <= ymax;
}
