#include "Drawing.hpp"
#include <fstream>

Drawing::Drawing():ccounter(0){}

bool Drawing::addCircle(const double x, const double y, const double r){
  if(ccounter==10) return false;

  circles[ccounter]=new Circle(x,y,r);
  ccounter++;
  
}

bool Drawing::addRectangle(const double x, const double y, const double w, const double h){
  if(rcounter==10) return false;

  rectangles[rcounter]=new Rectangle(x,y,w,h,"red",2);
  rcounter++;  
}

Drawing::~Drawing(){
  for(unsigned int cc=0; cc<ccounter; cc++)
    delete circles[cc];
  for(unsigned int rr=0; rr<rcounter; rr++)
    delete rectangles[rr];
}






void Drawing::saveToSVG(std::string filename){
  std::ofstream output(filename);

  double minx=getMinX();
  double miny=getMinY();
  double maxx=getMaxX();
  double maxy=getMaxY(); 

  output << "<svg  viewBox=\""
         << minx - BORDER <<" "<< miny - BORDER <<" "<< maxx-minx + 2*BORDER <<" "<< maxy-miny + 2*BORDER
         << "\">" << std::endl;

  for(unsigned int cc=0; cc < ccounter; cc++)
    output << circles[cc]->toSVG() <<std::endl;
  for(unsigned int rr=0; rr < rcounter; rr++)
    output << rectangles[rr]->toSVG() <<std::endl;
    
  output << "</svg> " << std::endl;

  output.close();
}











double Drawing::getMinX() const {
  if (ccounter==0) return 0;
  else {
    double min=circles[0]->getCenterX()-circles[0]->getRadius();
    for(unsigned int cc=1; cc<ccounter; cc++)
      if(circles[cc]->getCenterX()-circles[cc]->getRadius()<min)
        min = circles[cc]->getCenterX()-circles[cc]->getRadius();
    return min;
  }
}

double Drawing::getMinY() const {
  if (ccounter==0) return 0;
  else {
    double min=circles[0]->getCenterY()-circles[0]->getRadius();
    for(unsigned int cc=1; cc<ccounter; cc++)
      if(circles[cc]->getCenterY()-circles[cc]->getRadius()<min)
        min = circles[cc]->getCenterY()-circles[cc]->getRadius();
    return min;
  }
}

double Drawing::getMaxX() const {
  if (ccounter==0) return 0;
  else {
    double max=circles[0]->getCenterX()+circles[0]->getRadius();
    for(unsigned int cc=1; cc<ccounter; cc++)
      if(circles[cc]->getCenterX()+circles[cc]->getRadius()>max)
        max = circles[cc]->getCenterX()+circles[cc]->getRadius();
    return max;
  }
}

double Drawing::getMaxY() const {
  if (ccounter==0) return 0;
  else {
    double max=circles[0]->getCenterY()+circles[0]->getRadius();
    for(unsigned int cc=1; cc<ccounter; cc++)
      if(circles[cc]->getCenterY()+circles[cc]->getRadius()>max)
        max = circles[cc]->getCenterY()+circles[cc]->getRadius();
    return max;
  }
}
