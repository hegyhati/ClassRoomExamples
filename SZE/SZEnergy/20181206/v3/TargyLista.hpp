#ifndef TARGYLISTA_HPP
#define TARGYLISTA_HPP

#include "Targy.hpp"
#include <fstream>


class TargyLista {
    struct Elem {
        Targy adat;
        Elem* next;
    };
  
    Elem* head;
  public:
    TargyLista();
    
    TargyLista(const TargyLista& other);
    ~TargyLista();
    TargyLista& operator=(const TargyLista& other);
    
    void addTargy(const Targy& t);
    bool hasTargy(const Targy& t) const ;

    Targy& getTargy(const Targy& t);

    friend std::ostream& operator<<(std::ostream& s, const TargyLista& tl);
};



#endif
