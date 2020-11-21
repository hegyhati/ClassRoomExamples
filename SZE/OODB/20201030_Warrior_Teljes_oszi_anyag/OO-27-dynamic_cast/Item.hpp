#ifndef ITEM_HPP
#define ITEM_HPP

#include <string>

class Item {
  public:
    Item(double weight) : weight(weight) {}
    virtual ~Item(){}
    double getWeight() const { return weight; }
    virtual std::string toString() const { return "Item ["+std::to_string(weight)+" kg]";}
  private:
    const double weight;
};

#endif
