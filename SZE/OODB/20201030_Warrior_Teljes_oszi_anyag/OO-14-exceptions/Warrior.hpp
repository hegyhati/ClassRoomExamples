#ifndef WARRIOR_HPP
#define WARRIOR_HPP

#include <string>
#include "FileNotFoundException.hpp"

class Warrior {
  public:

    struct BadFileFormatException {
      std::string filename;
    };

    Warrior(const std::string& team, const std::string& name, int health_points, int damage=0, int defense=0);
    std::string toString() const;
    void attack(Warrior& defender) const;
    bool isAlive() const;
    std::string getTeam() const;
    
    static int getAliveWarriorCount() {return alive;}
    static Warrior parseFromFile(const std::string& team, const std::string& filename);

  private:
    static int alive;
    const std::string team;
    const std::string name;
    int health_points;
    int damage;
    int defense;

    void die();
};




#endif 
