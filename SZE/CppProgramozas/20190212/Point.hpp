#ifndef POINT_HPP
#define POINT_HPP

class Point {
    double x;
    double y;

  public:
  
    void setX(double x){this->x=x;}
    void setY(double y){this->y=y;}

    Point(double x=0, double y=0):x(x),y(y){}
    
    double distanceFromOrigin() const;
    double distance (const Point& other) const;
};
  
#endif
