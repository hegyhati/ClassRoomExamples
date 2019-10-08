#ifndef DRAWING_HPP
#define DRAWING_HPP


#define BORDER 10

#include "Shape.hpp"
#include <string>

class Drawing {
    Shape* shapes[10];
    unsigned int counter;
  public:
    Drawing();
    ~Drawing();
    bool addShape(Shape * newShape);
    
    void saveToSVG(std::string filename) const;
};



#endif
