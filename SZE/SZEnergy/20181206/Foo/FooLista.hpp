#ifndef FooLISTA_HPP
#define FooLISTA_HPP

#include "Foo.hpp"
#include <fstream>


class FooLista {
    struct Elem {
        Foo adat;
        Elem* next;
    };
  
    Elem* head;
  public:
    FooLista();
    
    FooLista(const FooLista& other);
    ~FooLista();
    FooLista& operator=(const FooLista& other);
    
    void addFoo(const Foo& t);
    bool hasFoo(const Foo& t) const ;

    Foo& getFoo(const Foo& t);

    friend std::ostream& operator<<(std::ostream& s, const FooLista& tl);
};



#endif
