#include "Drawing.hpp"
#include <fstream>

Drawing::Drawing():counter(0){}


bool Drawing::addShape(Shape* newShape){
  if(counter==10) return false;
  shapes[counter]=newShape;
  counter++;
  return true;
}

Drawing::~Drawing(){
  for(unsigned int c=0; c<counter; c++)
    delete shapes[c];
}

void Drawing::saveToSVG(std::string filename) const{
  std::ofstream output(filename);

  double minx=-100;
  double miny=-100;
  double maxx=300;
  double maxy=100; 

  output << "<svg  viewBox=\""
         << minx - BORDER <<" "<< miny - BORDER <<" "<< maxx-minx + 2*BORDER <<" "<< maxy-miny + 2*BORDER
         << "\">" << std::endl;

  for(unsigned int c=0; c < counter; c++)
    output << shapes[c]->toSVG() <<std::endl;
    
  output << "</svg> " << std::endl;

  output.close();
}









