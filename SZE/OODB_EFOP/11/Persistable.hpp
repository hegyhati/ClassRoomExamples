#ifndef PERSISTABLE_HPP
#define PERSISTABLE_HPP

#include <iostream>

class Persistable
{
  public:
    virtual void persist(std::ostream& s) const =0;
    virtual void loadfrom(std::istream& s) =0;
    virtual ~Persistable();
};

#endif // PERSISTABLE_HPP
