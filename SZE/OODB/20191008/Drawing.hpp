#ifndef DRAWING_HPP
#define DRAWING_HPP


#define BORDER 10

#include "Circle.hpp"
#include "Rectangle.hpp"
#include <string>

class Drawing {
    Circle* circles[10];
    unsigned int ccounter;
    Rectangle* rectangles[10];
    unsigned int rcounter;
  public:
    Drawing();
    ~Drawing();
    bool addCircle(const double x, const double y, const double r);
    bool addRectangle(const double x, const double y, const double w, const double h);
    
    void saveToSVG(std::string filename);

    double getMinX() const;
    double getMinY() const;
    double getMaxX() const;
    double getMaxY() const;
};



#endif
