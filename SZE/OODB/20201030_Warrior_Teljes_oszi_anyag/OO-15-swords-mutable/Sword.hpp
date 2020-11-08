#ifndef SWORD_HPP
#define SWORD_HPP

class Sword{
  public:
    Sword(int damage, int durability);
    int use();
    void repair();
  
  private:
    const int damage;
    const int max_durability;
    int current_durability;
};

#endif
