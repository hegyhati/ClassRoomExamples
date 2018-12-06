#include "Hallgato.hpp"

Hallgato::Hallgato(std::string nev, std::string neptun)
  :nev(nev),neptun(neptun) {}
  
std::string Hallgato::getNev() const { return nev; }

std::string Hallgato::getNeptun() const { return neptun; }
