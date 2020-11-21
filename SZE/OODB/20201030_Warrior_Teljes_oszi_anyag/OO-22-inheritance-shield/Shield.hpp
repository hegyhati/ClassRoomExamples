#ifndef SHIELD_HPP
#define SHIELD_HPP

#include <string>
#include "Wearable.hpp"

class Shield : public Wearable{
  public:
    Shield(int defense, int durability, double weight);
    int defend();
    double getWeight() const;
    std::string toString() const;

  private:
    const int defense;
    const double weight;
};



#endif
