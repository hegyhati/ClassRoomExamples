#include "Konyvtar.h"
#include <algorithm>

unsigned int Konyvtar::db(std::string szerzo, std::string cim) const {
  unsigned int darab=0;
  for(auto k:konyvek)
    if(k->getSzerzo()==szerzo and k->getCim()==cim)
      darab++;
  return darab;
}


const Konyv* Konyvtar::operator[](unsigned int idx) const {
  return (idx<konyvek.size()) ? konyvek[idx] : nullptr;
}


void Konyvtar::rendez() {
  std::sort(konyvek.begin(),konyvek.end(),[](Konyv* a, Konyv* b) {
    return *a < *b;
  });
}


std::list<const Konyv*> Konyvtar::operator[](std::string sorozatnev) const {
  std::list<const Konyv*> toReturn;
  Kotet * pk;
  for(auto k:konyvek) {
    pk=dynamic_cast<Kotet*>(k);
    if(pk!=nullptr && pk->getSorozatnev()==sorozatnev) 
      toReturn.push_back(pk);
  }
  return toReturn;
}


