#include "Point2D.hpp"
#include <iostream>

Point2D::Point2D(double x, double y) : x(x), y(y) {
    std::cerr << "Point2D(double x, double y)\n";
}

Point2D::Point2D(const Point2D& other) : x(other.x), y(other.y) {
    std::cerr << "Point2D(const Point2D& other)\n";
}

Point2D& Point2D::operator= (const Point2D& other) {
    std::cerr << "Point2D& operator= (const Point2D& other)\n";
    x = other.x;
    y = other.y;
    return *this;
}

Point2D Point2D::operator+(const Point2D& other) const {
    return Point2D(x+other.x, y+other.y);
}


Point2D Point2D::operator*(double constant) const {
    return Point2D(constant * x, constant * y);
}
Point2D& Point2D::operator*=(double constant){
    x*=constant;
    y*=constant;
    return *this;
}



double Point2D::getX() const { return x; }
double Point2D::getY() const { return y; }


Point2D operator*(double constant, const Point2D& point){
    return Point2D(constant*point.getX(), constant*point.getY());
}

std::ostream& operator<<(std::ostream& s, const Point2D& P){
    return s << "(" << P.getX() << "," << P.getY() << ")";     
}