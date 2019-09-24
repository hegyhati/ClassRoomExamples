#ifndef DRAWING_HPP
#define DRAWING_HPP

#include "Circle.hpp"
#include <string>

class Drawing {
    Circle* circles[10];
    unsigned int counter;
  public:
    Drawing();
    ~Drawing();
    bool addCircle(const double x, const double y, const double r);
    friend void saveToSVG(const Drawing D, std::string filename);

    double getMinX() const;
    double getMinY() const;
    double getMaxX() const;
    double getMaxY() const;
};



#endif
