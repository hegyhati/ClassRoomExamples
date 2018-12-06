#include "Hallgato.hpp"

Hallgato::Hallgato(std::string nev, std::string neptun)
  :nev(nev),neptun(neptun) {}
  
std::string Hallgato::getNev() const { return nev; }

std::string Hallgato::getNeptun() const { return neptun; }

bool Hallgato::operator ==(const Hallgato& other) const {return neptun == other.neptun; }


std::ostream& operator<<(std::ostream& s, const Hallgato& h) {
  s<< h.getNev()<<" ("<<h.getNeptun()<<")";
  return s;
}
