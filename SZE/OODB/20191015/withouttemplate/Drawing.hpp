#ifndef DRAWING_HPP
#define DRAWING_HPP


#define BORDER 10

#include "Shape.hpp"
#include <string>

class Drawing {
    struct SLItem{
      Shape* data;
      struct SLItem* next;
    };

    struct SLItem* shapes;
    
  public:
    Drawing();
    ~Drawing();
    void addShape(Shape * newShape);
    
    void saveToSVG(std::string filename) const;
};



#endif
