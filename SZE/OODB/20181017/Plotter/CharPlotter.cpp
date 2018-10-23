#include "CharPlotter.hpp"
#include <iostream>


void CharPlotter::plot(const list<Shape*>& shapes,
              const Point& tl, const Point& br,
              int width, int height) const{
  char pixel;
  double pixelwidth=(br.x-tl.x)/width;
  double pixelheight=(tl.y-br.y)/height;
  for (int y=0; y<height;y++){
    for (int x=0; x<width; x++) {
      pixel=' ';
      for(const auto& it: shapes)
        if(it->contains(Point(tl.x+(x+0.5)*pixelwidth,tl.y-(y+0.5)*pixelheight)))
          pixel=it->getSymbol();
      cout << pixel;
    }
    cout<<endl;
  }   
}
