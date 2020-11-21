#ifndef PRINTABLE_HPP
#define PRINTABLE_HPP

#include <iostream>
#include <string>

class Printable {
  public:
    virtual std::string toString() const =0;
    void print() const {
      std::cout << toString() << std::endl;
    }
};
#endif
