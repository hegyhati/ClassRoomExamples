#ifndef DURABILITY_HPP
#define DURABILITY_HPP


class Wearable {
  public:
    void repair();
    bool isUsable() const;
    void use();
    double getWeight() const;
  protected:
    Wearable(int max_durability, double weight);
    int max_durability;
    int current_durability;
  private:
    const double weight;
};


#endif
