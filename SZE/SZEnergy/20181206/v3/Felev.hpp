#ifndef FELEV_HPP
#define FELEV_HPP

#include "TargyLista.hpp"
#include <string>
#include <fstream>


class Felev{
    int ev;
    std::string evszak;
    TargyLista targyak;

  public:
    
    Felev(int ev, std::string evszak);
      
    int getEv() const;
    std::string getEvszak() const;
    
    void addTargy(const Targy& t);    
    bool hasTargy(const Targy& t) const;
    bool assignHallgato(const Targy& t, const Hallgato& h);
    void printTargyak(std::ostream& s) const;
};

std::ostream& operator<<(std::ostream& s, const Felev& f);


#endif
