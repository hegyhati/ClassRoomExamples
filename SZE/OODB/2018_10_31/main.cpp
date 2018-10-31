#include <iostream>
using namespace std;

int footimeA=0;
int footimeB=0;

class Counter {
  public:
    int id;
    static int nextid;
    Counter():id(++nextid){
      cerr<<"Creating object #"<<id<<" with constructor: ";
    }
    ~Counter(){
      cerr<<"Destroying object #"<<id<<endl;
    }
}; int Counter::nextid =0;


class A : public Counter {
    int *i;
    
  public:
    A() : i(new int[1024]){
      cerr<<"A() "<<endl;
    }
    A(const A& o) : i(new int[1024]) {
        footimeA++;
        cerr<<"A(c A&) "<<endl;
        for(int x=0;x<1024;x++)
          i[x]=o.i[x];
    }
    A& operator =(const A& o) {
      footimeA++;
      cerr<<"A=A"<<endl;
      for(int x=0;x<1024;x++)
          i[x]=o.i[x];
      return *this;
    }
    ~A(){
      delete [] i;
    }
};


void foobar(A a){
  cerr<<"void foobar(A)\n";
}

void foobar2(A& a){
  cerr<<"void foobar(A&)\n";
}

A foobar3(){
  A x;
  return x;
}

class B : public Counter {
    int *i;
    
  public:
    B() : i(new int[1024]){
      cerr<<"B() "<<endl;
    }
    B(const B& o) : i(new int[1024]) {
        footimeB++;
        cerr<<"B(c B&) "<<endl;
        for(int x=0;x<1024;x++)
          i[x]=o.i[x];
    }
    B(B&& o): i(o.i){
      cerr<<"B(B&&) "<<endl;
      o.i=nullptr;
    }
    B& operator =(const B& o) {
      footimeB++;
      cerr<<"B=B"<<endl;
      for(int x=0;x<1024;x++)
          i[x]=o.i[x];
      return *this;
    }
    B& operator =(B&& o) {
      cerr<<"B=B&&"<<endl;
      i=o.i;
      o.i=nullptr;
      return *this;
    }
    ~B(){
      delete [] i;
    }
};


void foobar(B b){
  cerr<<"void foobar(B)\n";
}

void foobar2(B& b){
  cerr<<"void foobar(B&)\n";
}

B foobar4(){
  B x;
  return x;
}

int main(){
  cerr<<"\n\n-- A a;\n";
  A a;
  cerr<<"\n\n-- foobar(a);\n";
  foobar(a);
  cerr<<"\n\n-- foobar2(a);\n";
  foobar2(a);
  cerr<<"\n\n-- a=foobar3();\n";
  a=foobar3();
  cerr<<"\n\n-- A aa(foobar3());\n";
  A aa(foobar3());
  cerr<<"\n\n-- B b;\n";
  B b;
  cerr<<"\n\n-- foobar(b);\n";
  foobar(b);
  cerr<<"\n\n-- foobar2(b);\n";
  foobar2(b);
  cerr<<"\n\n-- b=foobar4();\n";
  b=foobar4();
  cerr<<"\n\n-- B bb(foobar4());\n";
  B bb(foobar4());
  cerr<<"\n\n";
  cerr<<"Time A:"<<footimeA<<"\n";
  cerr<<"Time B:"<<footimeB<<"\n";
}


void initialtest(){
  cerr<<"\n\n-- A a;\n";
  A a;
  cerr<<"\n\n-- A b(a);\n";
  A b(a);
  cerr<<"\n\n-- A c=b;\n";
  A c = b; // == A c(b)
  cerr<<"\n\n-- A d;\n";
  A d;
  cerr<<"\n\n-- d=a;\n";
  d = a;
  cerr<<"\n\n";
}
