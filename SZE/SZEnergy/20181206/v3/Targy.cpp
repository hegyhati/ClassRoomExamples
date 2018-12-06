#include "Targy.hpp"


Targy::Targy(std::string nev, std::string neptun, int kredit)
  :nev(nev),neptun(neptun),kredit(kredit) {}
  
std::string Targy::getNev() const { return nev; }
std::string Targy::getNeptun() const { return neptun; }

void Targy::addHallgato(Hallgato h) {
  hallgatok.addHallgato(h);
}

bool Targy::hasHallgato(Hallgato h) const {      
  return hallgatok.hasHallgato(h);
} 


std::ostream& operator<<(std::ostream& s, const Targy& t) {
  s<< t.getNev()<<" ("<<t.getNeptun()<<")";
  return s;
}
