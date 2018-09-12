#include <iostream>
#include "Track.hpp"
using namespace std;


int main(){
  Track test;
  test.append(1,1,0);
  test.append(4,5,30);
  test.append(6,5,40);
  test.print();
  std::cout<<"Length: "<<test.length()<<std::endl;
}
