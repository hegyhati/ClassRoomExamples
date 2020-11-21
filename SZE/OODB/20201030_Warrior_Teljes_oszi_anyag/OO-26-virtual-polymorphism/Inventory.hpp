#ifndef INVENTORY_HPP
#define INVENTORY_HPP


#include "Item.hpp"
#include <vector>

class Inventory {
  public:
    Inventory(double weightlimit);
    ~Inventory();

    Inventory(const Inventory&) = delete;
    Inventory& operator=(const Inventory&) = delete;

    double getTotalWeight() const;
    int count() const;
    const Item& get(int index) const;
    bool put(Item* item);
    Item* drop(int index);
    void destroy(int index);
    void clear();

  private:

    std::vector<Item*> items;
    const double weightlimit;  
};


#endif
