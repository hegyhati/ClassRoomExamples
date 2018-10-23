#ifndef CHARPLOTTER_HPP
#define CHARPLOTTER_HPP

#include<list>
using namespace std;
#include "Shape.hpp"

class CharPlotter {
  public: 
    void plot(const list<Shape*>& shapes,
              const Point& tl, const Point& br,
              int width, int height) const;
};

#endif
