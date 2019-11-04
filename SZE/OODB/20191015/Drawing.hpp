#ifndef DRAWING_HPP
#define DRAWING_HPP


#define BORDER 10

#include "Shape.hpp"
#include <string>
#include <list>

class Drawing {
    std::list<Shape*> shapes;
  public:
    Drawing();
    ~Drawing();
    void addShape(Shape * newShape);
    
    void saveToSVG(std::string filename);
};



#endif
