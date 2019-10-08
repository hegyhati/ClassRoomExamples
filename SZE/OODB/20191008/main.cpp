#include <iostream>
#include <string>
using namespace std;

#include "Drawing.hpp"

int main(){
    Drawing D;
    D.addCircle(10,10,10);
    D.addCircle(-10,20,32);
    D.addCircle(40,-10,20);
    D.addRectangle(0,0,10,10);
    D.addRectangle(-50,-50,100,100);    
    D.saveToSVG("D.svg");
        
  return 0;
}

