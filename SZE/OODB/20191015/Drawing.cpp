#include "Drawing.hpp"
#include <fstream>

Drawing::Drawing(){}


void Drawing::addShape(Shape* newShape){  
 shapes.push_back(newShape);
}


Drawing::~Drawing(){
  for(std::list<Shape*>::iterator it=shapes.begin(); it!=shapes.end(); it++)  
    delete *it;
}

void Drawing::saveToSVG(std::string filename) {
  std::ofstream output(filename);

  double minx=-100;
  double miny=-100;
  double maxx=300;
  double maxy=300; 

  output << "<svg  viewBox=\""
         << minx - BORDER <<" "<< miny - BORDER <<" "<< maxx-minx + 2*BORDER <<" "<< maxy-miny + 2*BORDER
         << "\">" << std::endl;

  for(auto& shape: shapes)  
    output << shape->toSVG() <<std::endl;
    
  output << "</svg> " << std::endl;

  output.close();
}









