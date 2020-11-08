#ifndef SWORD_HPP
#define SWORD_HPP

#include <string>

class Sword{
  public:
    Sword():damage(0),max_durability(0),current_durability(0),weight(0){}
    Sword(int damage, int durability, double weight);
    int use();
    void repair();
    double getWeight() const;
    std::string toString() const;
  
  private:
    int damage;
    int max_durability;
    int current_durability;
    double weight;
};

#endif




