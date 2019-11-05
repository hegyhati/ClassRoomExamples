#include <iostream>
#include <string>
using namespace std;

class Whatever {
    int foo;
    double bar;
  public:
    Whatever(int foo=0, double bar=0.0): foo(foo), bar(bar){}
    int getFoo() const {return foo;}
    void print() const { cout << " ["<<foo<<","<<bar<<"> "; }
};


#include "LL_template.hpp"

int main(){
  LL list; 
  int foo; double bar;
  do{
    cin >> foo >> bar;
    if(foo!=0) list.push_back(Whatever(foo,bar));
  } while (foo!=0);


  while(!list.empty()) {
    list.front()->print();
    list.pop_front();
  }
  
  cout << endl;

  return 0;
}
