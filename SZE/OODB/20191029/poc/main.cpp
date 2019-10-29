#include <iostream>
#include <string>
using namespace std;

class Foo{
    static int count;
    string name;
  public:
    Foo(string name):name(name) {
      cerr<< "Creating "<<name<<endl;
      count++;}
    ~Foo(){ cerr<< "Destroying "<<name<<endl; count--;}
    static int getFooCount() {return count;} 
};

int Foo::count = 0;

void pfc(){
  cerr << "Number of Foo objects in the memory: "
       << Foo::getFooCount() << endl;
}

int main(){
  pfc();
  {
    Foo a("a");
    pfc();
  }
  pfc();
  Foo b("b");
  pfc();

  
  return 0;
}
