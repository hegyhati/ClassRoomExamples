#ifndef SWORD_HPP
#define SWORD_HPP

#include <string>
#include "Wearable.hpp"

class Sword : public Wearable {
  public:
    Sword(int damage, int durability, double weight);
    int attack();
    double getWeight() const;
    std::string toString() const;
  
  private:
    const int damage;
    const double weight;
};

#endif

