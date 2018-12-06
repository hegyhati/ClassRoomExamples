#ifndef TARGY_HPP
#define TARGY_HPP

#include "Lista.hpp"
#include "Hallgato.hpp"
#include <string>
#include <fstream>

class Targy{
    std::string nev;
    std::string neptun;
    int kredit;
    // elofeltetelek
    Lista<Hallgato> hallgatok;
    
  public:
    Targy(std::string nev="", std::string neptun="", int kredit=0);
      
    std::string getNev() const;
    std::string getNeptun() const;
    
    void addHallgato(Hallgato h);    
    bool hasHallgato(Hallgato h) const;

    bool operator ==(const Targy& other) const;
    
};

std::ostream& operator<<(std::ostream& s, const Targy& t);

#endif
