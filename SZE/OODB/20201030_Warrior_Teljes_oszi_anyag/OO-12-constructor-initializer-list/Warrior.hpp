#ifndef WARRIOR_HPP
#define WARRIOR_HPP

#include <string>

class Warrior {
  public:
    Warrior(const std::string& team, const std::string& name, int health_points, int damage=0, int defense=0);
    Warrior(const std::string& team, const std::string& filename);
    std::string toString() const;
    void attack(Warrior& defender) const;
    bool isAlive() const;
    std::string getTeam() const;

  private:
    const std::string team;
    std::string name;
    int health_points;
    int damage;
    int defense;

    void die();
};



#endif 
