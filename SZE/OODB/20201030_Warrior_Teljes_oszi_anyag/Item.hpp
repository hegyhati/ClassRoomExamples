#ifndef ITEM_HPP
#define ITEM_HPP

#include "Printable.hpp" 
#include <string>

class Item : public Printable {
  public:
    Item(double weight) : weight(weight) {}
    virtual ~Item(){}
    double getWeight() const { return weight; }
    //virtual std::string toString() const override { return "Item ["+std::to_string(weight)+" kg]";}
  private:
    const double weight;
};

#endif
