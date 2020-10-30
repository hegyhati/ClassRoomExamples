#ifndef WARRIOR_HPP
#define WARRIOR_HPP

#include <string>

class Warrior {
  public:
    void readFromKeyboard();
    std::string toString() const;
    void attack(Warrior& defender) const;
    bool isAlive() const;

  private:
    std::string name;
    int health_points;
    int damage;
    int defense;

    void die();
};



#endif 
