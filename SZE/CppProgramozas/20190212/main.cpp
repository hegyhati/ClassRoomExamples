#include <iostream>
using namespace std;


#include "Point.hpp"
#include "Line.hpp"

int main(){
  Point A(0,0);
  Point B=Point(3,4);


  cout << "A ket pont tavolsaga: "<<A.distance(B)<<endl;

  //Point p1;
  Line l1;

  return 0;
}
