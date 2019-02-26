#include <iostream>
using namespace std;

#include "Array.hpp"

class Point{
  public:
  double x;
  double y;
  Point(int lkasjdf=0) : x(0),y(0){}
};

ostream& operator << (ostream& s, const Point& p){
  s << "("<<p.x<<","<<p.y<<") ";
  return s;
}

int main(){

  Array<int> tomb(10);
  Array<double> dtomb(20);

  tomb[13]=3;
  dtomb[12]=1.26486434684;

  Array<Point> ptomb;

  cout << tomb << endl << dtomb << endl;

  cout << ptomb << endl;

}
