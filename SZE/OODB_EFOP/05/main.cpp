#include <iostream>
using namespace std;

#include "DateTime.hpp"




int main(){
  Date d1(1998,3,21);
  cout << d1 << endl;

  Time t1(36000);
  Time t2(1,5,4);

  cout <<"t1: "<<t1<<endl;
  cout <<"t2: "<<t2<<endl;
  
  if (t1>t2){
    cout << "t1 is longer than t2 by"<<t1-t2<<endl;
  }
  
  
  return 0;
}
