#include <iostream>
using namespace std;


class Foo{
  public:
    int bar;
    Foo():bar(0){
      cerr << this << ": Foo::Foo()"<<endl;}
    Foo(int b):bar(b){
      cerr << this << ": Foo::Foo(int)"<<endl;}
    Foo(const Foo& other) : bar(other.bar) {
      cerr << this << ": Foo::Foo(const Foo&)"<<endl;}
    Foo& operator=(const Foo& other){
      cerr << this << ": Foo::operator=(const Foo&)"<<endl;
      bar=other.bar;
      return *this;}
    void print() const {      
      cerr << this << ": Foo::print() - bar="<<bar<<endl;}
};

class Array {
  public:
    int size;
    int* values;

    Array(int size)
      :size(size), values(new int[size]){}

    void insert(int idx, int value) {
      if (idx>=0 && idx < size)
        values[idx]=value;
      else {
        cerr<<"Out of array index\n";
      }
    }
      
    int get(int idx){
      if (idx>=0 && idx < size)
        return values[idx];
      else {
        cerr<<"Out of array index\n";
        return -1;
      }
    }

    void print(){
      cerr<<this<<":"<<endl;
      for(int i=0;i<size;++i)
        cerr<<" ["<<i<<"]: "<<values[i]<<endl;
    }

};

int main () {
  cerr << "main() start" << endl;
  Array a(5);
  a.insert(2,5);
  a.insert(0,3);
  a.insert(32,32);
  a.print();

  Array b(35);
  
  a.print();
  b.print();
  b=a;

  
  a.print();
  b.print();

  b.insert(1,323232);
  
  a.print();
  b.print();
  

  cerr << "main() ends" << endl;
  return 0;
}

void testFoo(){
  Foo f1(3);
  Foo f2;
  Foo f3(f1);

  f1.print();
  f2.print();
  f3.print();

  cerr <<"f2=f1"<<endl;
  f2=f1; 
  

  f1.print();
  f2.print();
  f3.print();
}
