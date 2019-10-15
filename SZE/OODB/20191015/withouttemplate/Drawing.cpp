#include "Drawing.hpp"
#include <fstream>

Drawing::Drawing():shapes(nullptr){}


void Drawing::addShape(Shape* newShape){  
  if(shapes==nullptr){
    shapes=new SLItem;
    shapes->data=newShape;
    shapes->next=NULL;
  } else {
    SLItem *temp=shapes;
    while(temp->next != nullptr) temp=temp->next;
    temp->next=new SLItem;
    temp->next->data=newShape;
    temp->next->next=NULL;
  }
}


Drawing::~Drawing(){
  SLItem* tempnext;
  for(SLItem* temp=shapes; temp!=nullptr; temp=tempnext){
    delete temp->data;
    tempnext=temp->next;
    delete temp;
  }
}

void Drawing::saveToSVG(std::string filename) const{
  std::ofstream output(filename);

  double minx=-100;
  double miny=-100;
  double maxx=300;
  double maxy=300; 

  output << "<svg  viewBox=\""
         << minx - BORDER <<" "<< miny - BORDER <<" "<< maxx-minx + 2*BORDER <<" "<< maxy-miny + 2*BORDER
         << "\">" << std::endl;

  for(SLItem* temp=shapes; temp!=nullptr; temp=temp->next)
    output << temp->data->toSVG() <<std::endl;
    
  output << "</svg> " << std::endl;

  output.close();
}









