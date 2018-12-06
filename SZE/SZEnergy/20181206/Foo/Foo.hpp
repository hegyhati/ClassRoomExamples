#ifndef FOO_HPP
#define FOO_HPP

#include <fstream>
using namespace std;

class Foo{
  public:
    int x;
    Foo(int x=0);
    bool operator==(const Foo& other);
};

ostream& operator<<(ostream& s, const Foo& f);


#endif
