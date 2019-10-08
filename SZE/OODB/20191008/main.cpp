#include <iostream>
#include <string>
using namespace std;


#include "Circle.hpp"
#include "Rectangle.hpp"
#include "Square.hpp"
#include "Drawing.hpp"

int main(){
    Drawing D;
    D.addShape(new Circle(-33,20,5));
    D.addShape(new Rectangle(0,0,50,30));  
    D.addShape(new Rectangle(3,12,34,12,"red",2,true));  
    D.addShape(new Rectangle(4,12,-12,122,"csinirozsaszin"));    
    D.addShape(new Square(14,-20,33,"red",8)); 
    D.saveToSVG("D.svg");

    Circle c(10,10,10);
    cout<<c.toSVG()<<endl;
    Shape& s=c;
    cout<<s.toSVG()<<endl;
    
  return 0;
}

