#ifndef DURABILITY_HPP
#define DURABILITY_HPP

#include "Item.hpp"

class Wearable : public Item{
  public:
    void repair();
    bool isUsable() const;
    void use();
    Wearable& operator += (int repair){
      current_durability+=repair;
      if (current_durability>max_durability)
        current_durability=max_durability;
      return *this;
    }

  protected:
    Wearable(int max_durability, double weight);
    int max_durability;
    int current_durability;
};

#endif
