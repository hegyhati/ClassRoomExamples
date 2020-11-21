#ifndef SWORD_HPP
#define SWORD_HPP

#include <string>
#include "Wearable.hpp"

class Sword : public Wearable {
  public:
    Sword(int damage, int durability, double weight);
    int attack();
    std::string toString() const override;
  
  private:
    const int damage;
};

#endif

