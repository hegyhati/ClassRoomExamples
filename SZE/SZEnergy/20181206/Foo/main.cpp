#include <iostream>
using namespace std;

#include "FooLista.hpp"
#include "Foo.hpp"

int main(){
  Foo a(3);
  Foo b(4);

  FooLista l;
  l.addFoo(a);
  l.addFoo(a);
  l.addFoo(b);
  l.addFoo(a);
  l.addFoo(b);

  cout << l;
  
}
