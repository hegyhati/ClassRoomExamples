#ifndef HALLGATO_HPP
#define HALLGATO_HPP

#include <string>
#include <fstream>

class Hallgato{
    std::string nev;
    std::string neptun;
  public:
    Hallgato(std::string nev="", std::string neptun="");
    
    std::string getNev() const;
    std::string getNeptun() const;

     bool operator ==(const Hallgato& other) const;
    
};

std::ostream& operator<<(std::ostream& s, const Hallgato& h);

#endif
