#ifndef HALLGATOLISTA_HPP
#define HALLGATOLISTA_HPP

#include "Hallgato.hpp"

class HallgatoLista {
    struct Elem {
        Hallgato adat;
        Elem* next;
    };
  
    Elem* head;
  public:
    HallgatoLista();
    
    HallgatoLista(const HallgatoLista& other) ;
    ~HallgatoLista();
    HallgatoLista& operator=(const HallgatoLista& other);
    
    void addHallgato(const Hallgato& h);
    bool hasHallgato(const Hallgato& h) const;
};



#endif
