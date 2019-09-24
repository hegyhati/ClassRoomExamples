#include "Drawing.hpp"

Drawing::Drawing():counter(0){}

bool Drawing::addCircle(const double x, const double y, const double r){
  if(counter==10) return false;

  circles[counter]=new Circle(x,y,r);
  counter++;
  
}


Drawing::~Drawing(){
  for(unsigned int cc=0; cc<counter; cc++)
    delete circles[cc];
}

double Drawing::getMinX() const {
  if (counter==0) return 0;
  else {
    double min=circles[0]->getCenterX()-circles[0]->getRadius();
    for(unsigned int cc=1; cc<counter; cc++)
      if(circles[cc]->getCenterX()-circles[cc]->getRadius()<min)
        min = circles[cc]->getCenterX()-circles[cc]->getRadius();
    return min;
  }
}

double Drawing::getMinY() const {
  if (counter==0) return 0;
  else {
    double min=circles[0]->getCenterY()-circles[0]->getRadius();
    for(unsigned int cc=1; cc<counter; cc++)
      if(circles[cc]->getCenterY()-circles[cc]->getRadius()<min)
        min = circles[cc]->getCenterY()-circles[cc]->getRadius();
    return min;
  }
}

double Drawing::getMaxX() const {
  if (counter==0) return 0;
  else {
    double max=circles[0]->getCenterX()+circles[0]->getRadius();
    for(unsigned int cc=1; cc<counter; cc++)
      if(circles[cc]->getCenterX()+circles[cc]->getRadius()>max)
        max = circles[cc]->getCenterX()+circles[cc]->getRadius();
    return max;
  }
}

double Drawing::getMaxY() const {
  if (counter==0) return 0;
  else {
    double max=circles[0]->getCenterY()+circles[0]->getRadius();
    for(unsigned int cc=1; cc<counter; cc++)
      if(circles[cc]->getCenterY()+circles[cc]->getRadius()>max)
        max = circles[cc]->getCenterY()+circles[cc]->getRadius();
    return max;
  }
}
