#ifndef POINT_HPP
#define POINT_HPP

class Point {
  public: 
    const double x;
    const double y;
    Point(double x, double y);
    double operator-(const Point& other) const;
};





#endif
