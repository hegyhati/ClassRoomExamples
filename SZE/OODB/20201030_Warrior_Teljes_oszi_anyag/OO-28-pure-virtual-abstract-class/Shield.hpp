#ifndef SHIELD_HPP
#define SHIELD_HPP

#include <string>
#include "Wearable.hpp"

class Shield : public Wearable {
  public:
    Shield(int defense, int durability, double weight);
    int defend();
    std::string toString() const override;

  private:
    const int defense;
};



#endif
