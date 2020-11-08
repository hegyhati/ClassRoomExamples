#ifndef SWORD_HPP
#define SWORD_HPP

#include <string>

class Sword{
  public:
    Sword(int damage, int durability, double weight);
    int use();
    void repair();
    double getWeight() const;
    std::string toString() const;
  
  private:
    const int damage;
    const int max_durability;
    int current_durability;
    const double weight;
};

#endif
