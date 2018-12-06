#include "Foo.hpp"

Foo::Foo(int x) : x(x) {}

bool Foo::operator==(const Foo& other) { return x==other.x;}

ostream& operator<<(ostream& s, const Foo& f){
  s<<f.x<<endl;
}
