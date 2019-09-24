#include <iostream>
using namespace std;

#include "SVG_Export.hpp"
#include "Drawing.hpp"

int main(){
  {

    Drawing D;
    D.addCircle(10,10,10);
    D.addCircle(-10,20,32);
    D.addCircle(40,-10,20);
    saveToSVG(D,"D.svg");
  }
  return 0;
}
