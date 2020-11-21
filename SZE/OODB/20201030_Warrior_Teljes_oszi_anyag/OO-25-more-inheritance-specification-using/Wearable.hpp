#ifndef DURABILITY_HPP
#define DURABILITY_HPP

#include "Item.hpp"

class Wearable : public Item{
  public:
    void repair();
    bool isUsable() const;
    void use();
  protected:
    Wearable(int max_durability, double weight);
    int max_durability;
    int current_durability;
};


#endif
