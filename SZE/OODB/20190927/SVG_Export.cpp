#include "SVG_Export.hpp"
#include <fstream>
#include <iostream>

#define BORDER 10

void saveToSVG(const Drawing D, std::string filename){
  std::ofstream output(filename);

  double minx=D.getMinX();
  double miny=D.getMinY();
  double maxx=D.getMaxX();
  double maxy=D.getMaxY(); 

  std::cerr<< minx <<" "<< miny <<" "<< maxx <<" "<< maxy << std::endl;
 
  output << "<svg  viewBox=\""
         << minx - BORDER <<" "<< miny - BORDER <<" "<< maxx-minx + 2*BORDER <<" "<< maxy-miny + 2*BORDER
         << "\">" << std::endl;

  for(unsigned int cc=0; cc < D.counter; cc++)
    output << "  <circle cx=\""<<D.circles[cc]->getCenterX()<<"\" cy=\""<<D.circles[cc]->getCenterY()<<"\" r=\""<<D.circles[cc]->getRadius()<<"\" stroke=\"black\" stroke-width=\"1\" fill=\"none\"/>"<<std::endl;
    
  output << "</svg> " << std::endl;

  output.close();
}
