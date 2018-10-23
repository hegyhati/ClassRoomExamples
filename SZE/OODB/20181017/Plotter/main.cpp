#include <iostream>
#include <list>
using namespace std;

#include "Point.hpp"
#include "Circle.hpp"
#include "Rectangle.hpp"
#include "CharPlotter.hpp"

int main(){
    
  list<Shape*> shapes;
  shapes.push_back(new Circle(0,0,8,'*'));
  shapes.push_back(new Rectangle(-108,5,3,5,'='));
  shapes.push_back(new Circle(-10,10,12,'O'));
  CharPlotter plotter;
  plotter.plot(shapes, Point(-10,10), Point(0,0), 80, 40); 
  plotter.plot(shapes, Point(-20,20), Point(10,-10), 80, 40); 
  for(auto& it: shapes)
    delete it;
}
