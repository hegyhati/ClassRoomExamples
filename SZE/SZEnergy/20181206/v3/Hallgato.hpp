#ifndef HALLGATO_HPP
#define HALLGATO_HPP

#include <string>

class Hallgato{
    std::string nev;
    std::string neptun;
  public:
    Hallgato(std::string nev="", std::string neptun="");
    std::string getNev() const;
    std::string getNeptun() const;
};

#endif
