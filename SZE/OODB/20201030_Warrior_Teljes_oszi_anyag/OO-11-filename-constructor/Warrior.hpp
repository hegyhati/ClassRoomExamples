#ifndef WARRIOR_HPP
#define WARRIOR_HPP

#include <string>

class Warrior {
  public:
    Warrior(const std::string& name, int health_points, int damage=0, int defense=0);
    Warrior(const std::string& filename);
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
