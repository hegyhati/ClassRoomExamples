
#ifndef KONYVTAR_H
#define KONYVTAR_H

#include <iostream>
#include <string>
#include <vector>
#include <list>
#include "Kotet.h"
#include "Konyv.h"

class Konyvtar {
    std::vector<Konyv*> konyvek;
  public:
    ~Konyvtar() {
      for(auto& k: konyvek) 
        delete k;
    }
    void add(Konyv* k){konyvek.push_back(k);}
    void print() const {
      for(auto& k: konyvek)
        std::cout<<k->toString()<<std::endl;
    }

    /* Plusz pontokert */
    unsigned int db(std::string szerzo, std::string cim) const;
    const Konyv* operator[](unsigned int idx) const;
    void rendez();
    std::list<const Konyv*> operator[](std::string sorozatnev) const;
};

#endif
