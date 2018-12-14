#ifndef KOTET_H
#define KOTET_H

#include <string>
#include "Konyv.h"

class Kotet : public Konyv {
    std::string sorozatnev;
    int kotetszam;
  public:
    Kotet(std::string szerzo, std::string cim, int ev, std::string sorozatnev, int kotetszam):
      Konyv(szerzo,cim,ev),sorozatnev(sorozatnev),kotetszam(kotetszam){}
    std::string getSorozatnev() const {return sorozatnev;}
    int getKotetszam() const {return kotetszam;}
    virtual std::string toString() const override {return sorozatnev + "/" + std::to_string(kotetszam) + ": " + Konyv::toString();}
};

#endif
