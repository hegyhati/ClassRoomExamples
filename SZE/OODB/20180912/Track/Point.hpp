#ifndef POINT_HPP
#define POINT_HPP

class Point{
  private:
    double x;
    double y;
    double t;

  public:  
    Point(double x=0, double y=0, double t=0);
    double distanceFrom(const Point& other) const;
    void print() const;
    void set(double x=0, double y=0, double t=0);
};




#endif
