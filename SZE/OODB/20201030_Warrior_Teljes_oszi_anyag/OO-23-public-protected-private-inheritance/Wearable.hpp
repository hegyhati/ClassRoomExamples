#ifndef DURABILITY_HPP
#define DURABILITY_HPP


class Wearable {
  public:
    Wearable(int max_durability, double weight);
    void repair();
    bool isUsable() const;
    void use();
    double getWeight() const;
  protected:
    int max_durability;
    int current_durability;
  private:
    const double weight;
};


#endif
