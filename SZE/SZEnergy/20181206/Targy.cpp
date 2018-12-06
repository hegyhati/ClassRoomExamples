#include "Targy.hpp"


Targy::Targy(std::string nev, std::string neptun, int kredit)
  :nev(nev),neptun(neptun),kredit(kredit) {}
  
std::string Targy::getNev() const { return nev; }
std::string Targy::getNeptun() const { return neptun; }

void Targy::addHallgato(Hallgato h) {
  hallgatok.add(h);
}

bool Targy::hasHallgato(Hallgato h) const {      
  return hallgatok.has(h);
}

bool Targy::operator ==(const Targy& other) const {return neptun == other.neptun; }


std::ostream& operator<<(std::ostream& s, const Targy& t) {
  s<< t.getNev()<<" ("<<t.getNeptun()<<")";
  return s;
}
