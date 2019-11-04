#include <iostream>
#include <string>
using namespace std;

class FooException{
  public:
    string functioncallpath;
    string errormessage;
};

class BarException{};

void f(string s){
  s += " -> f()";
  cout << s <<endl;
  if(s.length()>21) {
    cerr << "ERROR" <<endl;
    throw FooException{s,"Too long call path"};
  }
}

void h(string s) {
  s += " -> h()";
  cout << s <<endl;
  if(s.length()%2==0) throw BarException();
  f(s);
}

void g(string s) {
  s += " -> g()";
  cout << s <<endl;
  f(s);
  h(s);
  f(s);  
}

int exceptiontest(){
  try {
    g("main()");
  } catch (FooException e) {
    cerr << "Hupp hupp Foo"<<endl
    << "\tError message: " << e.errormessage << endl
    << "\tPath: "<<e.functioncallpath << endl;
  } catch (BarException e) {
    cerr << "Hupp hupp Bar"<<endl;
  }
  cout << "Sikeres program vege" <<endl;
  return 0;
}

