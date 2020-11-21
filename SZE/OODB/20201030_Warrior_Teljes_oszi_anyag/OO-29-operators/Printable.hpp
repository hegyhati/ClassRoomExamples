#ifndef PRINTABLE_HPP
#define PRINTABLE_HPP

#include <ostream>
#include <string>

class Printable {
  public:
    virtual std::string toString() const =0;
};

inline std::ostream& operator<<(std::ostream& s, const Printable& p){
  s << p.toString();
  return s;
}

#endif
