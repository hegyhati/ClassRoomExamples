#ifndef ITEM_HPP
#define ITEM_HPP

class Item {
  public:
    Item(double weight) : weight(weight) {}
    double getWeight() const { return weight; }
  private:
    const double weight;
};

#endif
